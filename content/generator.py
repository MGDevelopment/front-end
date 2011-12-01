"""The content generation program

This program has two modes of operation:

1- daemon mode (single parameter with value "daemon")
2- generation mode (parameters)

DAEMON MODE
In this mode the process enters an infinite loop that tries to get
jobs from the queue and tries to execute those jobs. The loop is not
actualy infinite, as the process exits after a specified time
(content.daemon.maxrun). The goal of this is to give chance to the
system to create a new generator every now and then, but not too often.

GENERATION MODE
In this mode, the process interprets the command line arguments to do
one of the following things:
- print help (arguments: help or no arguments)
- list the queue (arguments: list)
- add jobs to the queue (arguments: add <entity type> [* | <entity ids>]...)

by Jose Luis Campanello
"""

import sys

import ecommerce.config
import ecommerce.db
from   ecommerce.queue import *

import daemon
import jobs

#########################################################
#########################################################
#
# some constants and handy functions
#
configPrefix = "content"
queuePrefix  = configPrefix + ".queue"
entityTypes  = [ "PAGE", "PROD", "SUBJ" ]
maxEntities  = 256


def getProducer():
    """Get a Producer queue instance"""

    # get the config and a producer
    config = ecommerce.config.getConfig()
    return ecommerce.queue.queue(config, queuePrefix)


def getEntityIds(type):
    """Get the list of all entities of a given type from DB"""

    # get a cursor
    conn = ecommerce.db.getConnection()
    cursor = conn.cursor()

    # execute the query
    cursor.execute("""
SELECT      EntityId
    FROM    Stage0_Delta
    WHERE   EntityType = ?
    ORDER BY EntityId
""", type)

    # fetch the ids
    elist = [ ]
    row = cursor.fetchone()
    while row is not None:
        elist.append(int(row[0]))
        row = cursor.fetchone()
    cursor.close()

    return elist


#########################################################
#########################################################
#
# COMMAND - ADD
#
def cmd_add():
    """Puts generate commands into the queue"""

    # build the list of entities
    entities = { type : [ ] for type in entityTypes }
    type     = ""
    param    = 2            # skip script name and "add" command
    while param < len(sys.argv):

        # get an entity type and check it's valid
        type = sys.argv[param]
        param += 1
        if type not in entityTypes:
            print "ERROR: entity type [%s] is not valid" % type
            return -1

        # build the list of values
        eList = [ ]
        if sys.argv[param] == "*":
            # get the list of (ALL) ids from the database
            eList = getEntityIds(type)
            param += 1
        else:
            # process the params
            while param < len(sys.argv):

                try:
                    eList.append(int(sys.argv[param]))
                    param += 1
                except ValueError:
                    break

        # attach the list to the type
        entities[type] = eList

    # get a producer
    producer = getProducer()

    # start creating jobs
    jobCount = 0
    for type in entityTypes:

        # get the list
        elist = entities[type]

        # build jobs of up to 256 entries
        jlist = [ ]
        for i in range(len(elist)):
            # append the entity
            jlist.append( [ type, elist[i] ] )

            # if max number of entities reached, send job
            if len(jlist) == maxEntities:

                # create the job
                job = jobs.encode(jobs.generate(jlist))

                # get an item, set content and make it ready
                item = producer.item()
                item.content = job
                producer.ready(item)
                jobCount += 1

                # new list
                jlist = [ ]

        # if list not empty, send job
        if len(jlist) > 0:

            # create the job
            job = jobs.encode(jobs.generate(jlist))

            # get an item, set content and make it ready
            item = producer.item()
            item.content = job
            producer.ready(item)
            jobCount += 1

    # report the number of jobs created
    print "Put %d jobs in queue" % jobCount

    return 0


#########################################################
#########################################################
#
# COMMAND - DAEMON
#
def cmd_daemon():
    """Go into daemon mode"""

    # get the config and a consumer
    config = ecommerce.config.getConfig()
    consumer = None
    try:
        consumer = ecommerce.queue.queue(config, queuePrefix, False)
    except QueueConfigurationException as ex:
        print "CONFIG: %s" % ex
        return -1
    except QueueRuntimeException as ex:
        print "RUNTIME: %s" % ex
        return -1
    except QueueFolderLockException:
        # not an error, there is another daemon running
        print "WARNING: cannot start daemon, already running"
        return 0
    except Exception as ex:
        print "ERROR: %s" % ex
        return -1

    # go daemon
    return daemon.daemon(config, configPrefix, consumer)


#########################################################
#########################################################
#
# COMMAND - DELTA
#
def cmd_delta():
    print "NOT YET IMPLEMENTED!!!!"

    return 0


#########################################################
#########################################################
#
# COMMAND - EXIT
#
def cmd_exit():

    # create an exit job
    job = jobs.encode(jobs.exit())

    # get a producer
    producer = getProducer()

    # get an item, set content and make it ready
    item = producer.item()
    item.content = job
    producer.ready(item)

    print "Exit command put in queue"

    return 0


#########################################################
#########################################################
#
# COMMAND - HELP
#
def cmd_help():

    print """usage: python generator.py [parameters]
    
Where parameters can be one of:
- add job to the regeneration queue
    "add" ( <entity type> [ * | <entity id list> ] )+

- go into daemon mode
    "daemon"

- process the database delta (things that changed)
    "delta"

- cause the daemon to exit (using a job, which can take some time)
    "exit"

- print help (default option if cannot figure out what to do)
    "help"

- list the queue
    "list"
"""

    return 0


#########################################################
#########################################################
#
# COMMAND - LIST
#
def cmd_list():
    """List the job queue"""

    # get a producer
    producer = getProducer()

    # get the list of pending jobs
    jobs = producer.list()

    # print que list size and the entries
    print "Number of jobs: %d" % len(jobs)
    for j in range(len(jobs)):
        print "    job %06d - %s" % (j, jobs[j])

    return 0


#########################################################
#########################################################
#
# MAIN FUNCTION
#
commands = {
    "add"           : cmd_add,
    "daemon"        : cmd_daemon,
    "delta"         : cmd_delta,
    "exit"          : cmd_exit,
    "help"          : cmd_help,
    "list"          : cmd_list,
    "__default__"   : cmd_help
}

def main():
    """The main function"""

    # get the command
    cmd = sys.argv[1] if len(sys.argv) >= 2 else "__default__"
    if cmd not in commands:
        cmd = "__default__"

    # execute the command
    commands[cmd]()


if __name__ == "__main__":
    main()