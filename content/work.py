"""The worker code

by Jose Luis Campanello
"""

import types
import Queue
import logging
import logging.config
import traceback

import workerpool
import jinja2

import ecommerce.config
import ecommerce.storage

# the worker pool
pool        = None
storages    = None
urls        = None
jinjaEnv    = None
logger      = None

#
# the job class
#
class GeneratorJob(workerpool.Job):
    """Job to generate a document and writing it to some storage"""

    def __init__(self, entityType, entityId, cannonical, doc, jobData, errqueue):

        self._entityType = entityType
        self._entityId   = entityId
        self._cannonical = cannonical
        self._doc        = doc
        self._jobData    = jobData
        self._errqueue   = errqueue

    def run(self):

        # catch errors
        try:

            # calculate the targets
            targets = self._doc["target.path"]
            if not isinstance(targets, types.ListType):
                targets = [ targets ]

            targets = self.macros(targets, { "cannonical" : self._cannonical } )

            # get the urls and augment with the needed values
            _urls = urls.copy()
            _urls["cannonical"] = self._cannonical
            _urls["urls"]       = targets[:]

            # get the template, build the params and render de document
            template    = jinjaEnv.get_template(self._doc["template"])
            parameters  = { "d" : self._jobData, "url" : _urls }
            document    = template.render(parameters).encode("utf-8")

            # save the document
            headers     = self._doc["headers"]
            targetRepo  = self._doc["target.repo"]
            if targetRepo in storages:
                # write to the repository
                storage     = storages[targetRepo]
                for target in targets:
                    storage.put(target, document, headers)
            else:
                # send an error to the queue
                self._errqueue( {
                    "EntityType" : self._entityType,
                    "EntityId"   : self._entityId,
                    "Document"   : self._doc.get("name", "uknown") } )
        except Exception as ex:
            # log an error
            err = traceback.format_exc()
            logger.error("Document %s for %s/%d failed. Stack trace follows:\n%s",
                         self._doc.get("name", "uknown"), self._entityType, self._entityId, err)
            # send an error to the queue
            self._errqueue.put( {
                "EntityType" : self._entityType,
                "EntityId"   : self._entityId,
                "Document"   : self._doc.get("name", "uknown") } )

    def macros(self, values, variables):
        """Expand the variables in the values"""

        # make a copy
        values = values[:]

        # iterate on the variables
        for v in variables:

            # replace in all values
            for i in range(len(values)):
                values[i] = values[i].replace("{{" + v + "}}", variables[v])

        return values



############################################
#
# initialize
#
def initialize(config, prefix, _logger):
    """Initialize the worker system"""

    global pool
    global storages
    global urls
    global jinjaEnv
    global logger

    # save the logger
    logger = _logger

    # create the worker pool
    threads = config.getMulti(prefix, "daemon.threads", 1)
    pool = workerpool.WorkerPool(size = threads)

    logger.info("Worker pool size %d (# threads)", threads)

    # get the storages
    storages = ecommerce.storage.getStorages(config, prefix + ".repositories")

    logger.info("Repositories: %s", ", ".join(storages.keys()))

    # prepare the base urls
    urls = config.getMulti(prefix, "urls", { })

    # jinja environment
    folder = config.getMulti(prefix, "templates.folder", "./templates")
    jinjaEnv = jinja2.Environment(loader = jinja2.FileSystemLoader(folder))

    logger.info("Templates folder: %s", folder)



############################################
#
# deinitialize
#
def deinitialize():
    """Deinitialize the worker system"""

    global pool
    global storages
    global urls
    global jinjaEnv
    global logger

    logger.info("Terminating all threads in Worker pool")

    # send the shutdown command to all workers and wait
    pool.shutdown()
    pool.wait()

    logger.info("Terminated all threads in Worker pool")

    # delete the pool, storages and urls
    pool        = None
    storages    = None
    urls        = None
    jinjaEnv    = None
    logger      = None


############################################
#
# do - execute a job
#
def do(id, entities, docs, cannonicals, data):
    """Do the document generation"""

    global pool     # not sure if modifing methods require pool to be global

    # if no pool, signal job error
    if pool is None:
        logger.error("No worker pool?")
        return False

    # error queue
    logger.debug("Created error queue")
    errqueue = Queue.Queue(0)

    # for each entity, dispatch the documents needed
    for e in range(len(entities)):

        # handy data
        entityType, entityId = entities[e][0], entities[e][1]
        cannonical           = cannonicals.get( (entityType, entityId), "")

        # iterate each document
        count = 0
        for doc in docs[entityType]:

            # get the dataset name
            dataset = doc["dataset"]

            # get the data
            jobData = data.get( (entityType, entityId, dataset), { } )

            # create the job and put it in queue
            logger.debug("Dispatching document %s for %s/%d/%s cannonical %s",
                         doc["name"], entityType, entityId, dataset, cannonical)
            job = GeneratorJob(entityType, entityId, cannonical, doc, jobData, errqueue)
            pool.put(job)

            # one more job
            count += 1

        logger.info("Job %s requires %d documents", id, count)

    # wait until all jobs are complete
    logger.info("Waiting for documents to complete")
    pool.wait()

    # figure out if job was done OK or with error
    success = True
    if not errqueue.empty():
        # job failed
        success = False

        # get the list of what went wrong
        errors = [ ]
        while not errqueue.empty():
            errors.append(errqueue.get())
        errlist = "\n".join( [ str( (err["EntityType"],
                                     err["EntityId"],
                                     err["Document"]) ) for err in errors ] )
        logger.error("%d Documents where not generated. The list follows:\n%s", len(errors), errlist)
    else:
        logger.debug("All Documents completed OK")

    return success
