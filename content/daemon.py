"""The daemon code

by Jose Luis Campanello
"""

import time

import ecommerce.db.dataset
import ecommerce.queue

import tmklib.url

import preprocess
import jobs
import documents
import work


############################################
#
# job - generate
#
def jobGenerate(job):
    """Handle a content generation job"""

    # find the relevant documents (for the tag, if present)
    tag  = job.get("tag", "*")
    docs = documents.relevant(tag)

    # extract the lists of datasets
    datasetNames = {
        e : { docs[e][i]["dataset"] : 1 for i in range(len(docs[e])) }.keys()
        for e in docs
    }

    # get the entities
    entities = job["entities"]

    # get the cannonicals, if anything goes wrong, fail the job
    try:
        urls = tmklib.url.cannonicals(entities)
    except Exception as ex:
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
        # job in error
        return False
    if reduce(lambda x, y: x or y[2], result, False):
        return False

    #import pprint
    #pprint.pprint(result, open("jlc_data.py", "w"), 4)

    # build handy data (key being <EntityType, EntityId, datasetName>)
    data = { }
    for d in range(len(datasets)):
        data[datasets[d]] = result[d][3]

    # do the work
    return work.do(entities, docs, cannonicals, data)


############################################
#
# job - exit
#
_terminating = False

def terminating():
    """Return terminating status"""

    return _terminating


def jobExit(job):
    """Mark termination"""

    global _terminating

    _terminating = True

    return True


############################################
#
# the daemon code
#
jobTypes = {
    "exit"      : jobExit,
    "generate"  : jobGenerate
}

def daemon(config, prefix, queue):
    """The main daemon function
    
    It gets some options from the configuration and
    starts trying to pull jobs from the queue.
    """

    # get some config options
    maxrun = config.getMulti(prefix, "daemon.maxrun", 3600)
    endBy  = time.time() + maxrun

    # initialize the work
    work.initialize(config, prefix)

    # set dataset preprocessing
    ecommerce.db.dataset.setPreProcess(preprocess.preProcess)

    # start looping
    now  = time.time()
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

            # get the job type and dispatch it
            jobType = job.get("type")
            if jobType not in jobTypes:
                handled = False
            else:
                handled = jobTypes[jobType](job)

            # mark as done or error
            if handled:
                queue.done(item)
            else:
                queue.error(item)

        # sleep for 1 second
        time.sleep(1)

        # get current time
        now = time.time()

    # deinitialize the work
    work.deinitialize()

    return 0
