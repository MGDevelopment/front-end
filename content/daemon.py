"""The daemon code

by Jose Luis Campanello
"""

import time
import logging
import logging.config
import traceback

import ecommerce.db.dataset
import ecommerce.queue

import tmklib.url
import tmklib.cache

import preprocess
import jobs
import documents
import work

#
# our logger
#
_logger = None


############################################
#
# job - generate
#
def jobGenerate(id, job):
    """Handle a content generation job"""

    logger.info("Processing generate Job id %s", id)

    # find the relevant documents (for the tag, if present)
    tag  = job.get("tag", "*")
    docs = documents.relevant(tag)
    logger.debug("Got relevant documents")

    # extract the lists of datasets
    datasetNames = {
        e : { docs[e][i]["dataset"] : 1 for i in range(len(docs[e])) }.keys()
        for e in docs
    }
    logger.debug("Calculated dataset names")

    # get the entities
    entities = job["entities"]
    logger.debug("Got entities")

    # get the cannonicals, if anything goes wrong, fail the job
    try:
        urls = tmklib.url.cannonicals(entities)
        logger.debug("Got cannonicals")
    except Exception as ex:
        # log an error
        err = traceback.format_exc()
        logger.error("Failed to get cannonicals, stack trace follows\n%s", err)
        # job in error
        return False

    # build the list of cannonicals
    cannonicals = { (entities[i][0], entities[i][1]) : urls[i] for i in range(len(entities)) }

    # build the list of datasets to fetch
    datasets = [ ]
    for e in range(len(entities)):

        # handy values
        (entityType, entityId) = (entities[e][0], entities[e][1])

        # sanity check
        if entityType not in datasetNames:
            datasetNames[entityType] = [ ]

        # append the datasets for this entity
        datasets.extend( [ (entityType, entityId, dataset)
                            for dataset in datasetNames[entityType] ] )

    # get the data from the database, if anything goes wrong, fail the job
    try:
        result = ecommerce.db.dataset.fetch(datasets)
    except Exception as ex:
        # log an error
        err = traceback.format_exc()
        logger.error("Failed to get datasets, stack trace follows:\n%s", err)
        # job in error
        return False
    if reduce(lambda x, y: x or y[2], result, False):
        # log an error
        failed = "\n".join( [ str( (datasets[i][0],
                                    datasets[i][1],
                                    datasets[i][2],
                                    result[i][3]) ) for i in range(len(datasets)) if result[i][2] ] )
        logger.error("Failed to get datasets. The following datasets executed with errors:\n%s", failed)
        return False

    # build handy data (key being <EntityType, EntityId, datasetName>)
    data = { }
    for d in range(len(datasets)):
        data[datasets[d]] = result[d][3]

    # do the work
    return work.do(id, entities, docs, cannonicals, data)


############################################
#
# job - cache
#
def jobCache(id, job):
    """Regenerate the cache"""

    logger.info("Processing cache Job. Begin cache reload")

    tmklib.cache.reload()

    logger.info("Processing cache Job. Terminated cache reload")

    return True


############################################
#
# job - exit
#
_terminating = False

def terminating():
    """Return terminating status"""

    return _terminating


def jobExit(id, job):
    """Mark termination"""

    global _terminating

    _terminating = True

    logger.info("Processing exit Job. Setting terminate mark")

    return True


############################################
#
# the daemon code
#
jobTypes = {
    "exit"      : jobExit,
    "cache"     : jobCache,
    "generate"  : jobGenerate
}

def daemon(config, prefix, queue):
    """The main daemon function
    
    It gets some options from the configuration and
    starts trying to pull jobs from the queue.
    """

    global logger

    # configure logging
    logging.basicConfig(level = logging.DEBUG, datefmt = '%Y-%m-%d %H:%M:%S')
    logconf = config.getMulti(prefix, "logging")
    if logconf is not None:

        # config the logging
        logging.config.dictConfig(logconf) 

        # get a logger
        logger = logging.getLogger(prefix)
    else:
        logger = logging.getLogger('')


    # get some config options
    maxrun = config.getMulti(prefix, "daemon.maxrun", 3600)
    endBy  = time.time() + maxrun

    logger.info("Daemon started - maxrun %d", maxrun)

    # initialize the work
    work.initialize(config, prefix, logger)

    # set dataset preprocessing
    ecommerce.db.dataset.setPreProcess(preprocess.preProcess)

    # start looping
    now  = time.time()
    logger.info("Daemon will end by %s", endBy)
    while not terminating() and now < endBy:

        # try to fetch a job from the queue (non blocking)
        item = queue.next()
        while item is None and now < endBy:
            time.sleep(1)
            item = queue.next()
            now  = time.time()

        # if we have a job, process it
        if item is not None:

            # decode the job
            job = jobs.decode(item.content)

            logger.info("Got job %s, job type %s", item.id, job.get("type", "unknown"))

            # get the job type and dispatch it
            jobType = job.get("type")
            if jobType not in jobTypes:
                handled = False
            else:
                tStart  = time.time()
                handled = jobTypes[jobType](item.id, job)
                tEnd    = time.time()

            # mark as done or error
            if handled:
                logger.info("Job %s processed ok", item.id)
                queue.done(item)
            else:
                logger.info("Job %s processed with ERROR", item.id)
                queue.error(item)
            logger.info("Took %3f seconds to complete job", tEnd - tStart)
        else:
            logger.debug("Job Queue empty")

        # sleep for 1 second (if queue is empty)
        if queue.isEmpty():
            logger.debug("Waiting 1 second...")
            time.sleep(1)

        # get current time
        now = time.time()

    logger.info("Daemon terminating - reason: %s",
                "command" if terminating() else "maxrun reached")

    # deinitialize the work
    work.deinitialize()

    return 0
