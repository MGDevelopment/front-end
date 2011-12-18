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
subtypes     = {
    "PAGE"   : [ ],
    "PROD"   : [ ],
    "SUBJ"   : [ "Seccion", "Grupo", "Familia", "Subfamilia" ]
}
maxEntities  = 256


def getProducer():
    """Get a Producer queue instance"""

    # get the config and a producer
    config = ecommerce.config.getConfig()
    return ecommerce.queue.queue(config, queuePrefix)


#
# important: write the queries so that the parameters are
# (IN ORDER):
#
#      EntityType
#      Subtype     (for any other value)
#
entityQueries   = {
    ######################################
    #
    # PAGE
    #
    "PAGE"      : """
SELECT          D.EntityId
    FROM        Stage0_Delta D
    WHERE       D.EntityType = ?
    ORDER BY    D.EntityId DESC
    """,
    ######################################
    #
    # SUBJ
    #
    # NOTE: order by a function on subtype, so that
    #       primary pages are built before secondary
    #       pages
    #
    "SUBJ"      : """
SELECT          D.EntityId,
                CASE S.Subtype
                    WHEN 'Seccion' THEN             0
                    WHEN 'Grupo' THEN               1
                    WHEN 'Familia' THEN             2
                    WHEN 'Subfamilia' THEN          3
                END                     AS Orden
    FROM        Stage0_Subjects S
    INNER JOIN  Stage0_Delta D
        ON      S.SubjectId = D.EntityId AND
                D.EntityType = ?
    WHERE       S.Subtype = ?
    ORDER BY    2, D.EntityId
    """,
    ######################################
    #
    # PROD
    #
    "PROD"      : """
SELECT          D.EntityId
    FROM        Stage0_Delta D
    INNER JOIN  Articulos A
        ON      D.EntityId = A.Id_Articulo AND
                A.Categoria_Seccion IN (1, 3, 4, 5) AND
                A.Activo = 'SI' AND
                A.Habilitado_Tematika = 'S'
    WHERE       D.EntityType = ?
    ORDER BY    D.EntityId DESC
    """
}

def getEntityIds(type, subtype = None):
    """Get the list of all entities of a given type from DB"""

    # get a cursor
    conn = ecommerce.db.getConnection()
    cursor = conn.cursor()

    # decide the query to execute
    if type not in entityQueries:
        return [ ]

    # execute the query
    qparams = (type, )
    if subtype is not None:
        qparams = (type, subtype)
    cursor.execute(entityQueries[type], qparams)

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
        fullType = sys.argv[param]
        type = fullType
        subtype = None
        if "/" in type:
            (type, waste, subtype) = fullType.partition("/")
        param += 1
        if type not in entityTypes:
            print "ERROR: entity type [%s] is not valid" % type
            return -1
        if subtype is not None and subtype not in subtypes[type]:
            print "ERROR: entity subtype [%s] for type [%s] is not valid" % (subtype, type)
            return -1

        # build the list of values
        eList = [ ]
        if sys.argv[param] == "*":

            # if the entity has subtypes and we have no subtype, iterate
            if subtype is None and subtypes[type]:
                # iterate subtypes
                for subtype in subtypes[type]:

                    # set the fullType
                    fullType = type + "/" + subtype

                    # get the list of (ALL) ids from the database
                    eList = getEntityIds(type, subtype)
                    param += 1

                    # attach the list to the type
                    entities[fullType] = eList

            else:
                # no subtypes or subtype specified

                # get the list of (ALL) ids from the database
                eList = getEntityIds(type, subtype)
                param += 1

                # attach the list to the type
                entities[fullType] = eList
        else:
            # process the params
            while param < len(sys.argv):

                try:
                    eList.append(int(sys.argv[param]))
                    param += 1
                except ValueError:
                    break
            # attach the list to the type
            entities[fullType] = eList

    # get a producer
    producer = getProducer()

    # start creating jobs
    jobCount = 0
    for fullType in entities:

        # separate type/subtype
        type = fullType
        if "/" in type:
            (type, waste, subtype) = fullType.partition("/")

        # get the list
        elist = entities[fullType]

        # build jobs of up to 256 entries
        localJobCount = 0
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
                localJobCount += 1

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
            localJobCount += 1

        # report
        if localJobCount > 0:
            print "added %5d jobs for entity %s" % (localJobCount, fullType)
        jobCount += localJobCount

    # report the number of jobs created
    print ""
    print "Added a total of %5d jobs in queue" % jobCount
    print ""

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
# COMMAND - CACHE
#
def cmd_cache():

    # create an exit job
    job = jobs.encode(jobs.cache())

    # get a producer
    producer = getProducer()

    # get an item, set content and make it ready
    item = producer.item()
    item.content = job
    producer.ready(item)

    print "Cache command put in queue"

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
    "add" ( <entity type>[/<subtype>] [ * | <entity id list> ] )+

  Where the "/<subtype>" addition is only valid for SUBJ. This provides
  a greater degree of control of what and in what sequence to generate.

- regenerate internal cache (images, interviews, biographies, etc)
    "cache"

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

- regenerate the related files for all products
    "related"

- list all the available subtypes
    "subtypes"
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
# COMMAND - RELATED
#
def cmd_related():
    """Regenerate the related documents for Products"""

    print "Retrieving the Products with Relations"

    # get a cursor
    conn = ecommerce.db.getConnection()
    cursor = conn.cursor()

    # execute the query
    cursor.execute("""
SELECT          DISTINCT AR.Id_Articulo
    FROM        RCO_Articulos_Relacionados AR
    WHERE       AR.Id_Articulo IN (
                    SELECT      A.Id_Articulo
                        FROM    Articulos A
                        WHERE   A.Categoria_Seccion IN (1, 3, 4, 5) AND
                                A.Activo = 'SI' AND
                                A.Habilitado_Tematika = 'S')
    ORDER BY    AR.Id_Articulo DESC
""")

    # fetch the ids
    elist = [ ]
    row = cursor.fetchone()
    while row is not None:
        elist.append(int(row[0]))
        row = cursor.fetchone()
    cursor.close()
    conn.close()

    # get a producer
    producer = getProducer()

    # start creating jobs (of up to 256 entries each)
    jobCount = 0
    jlist = [ ]
    for e in elist:
        # append the entity
        jlist.append( [ "PROD", e ] )

        # if max number of entities reached, send job
        if len(jlist) == maxEntities:

            # create the job
            job = jobs.encode(jobs.generate(jlist, "related"))

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
        job = jobs.encode(jobs.generate(jlist, "related"))

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
# COMMAND - SUBTYPES
#
def cmd_subtypes():
    """List al entity types with the available subtypes"""

    print "The known entity types (and subtypes) are:"
    print ""

    # list types
    for type in entityTypes:
        sub = ("subtypes: " + ", ".join(subtypes[type])) if subtypes[type] else "no subtypes"
        print "%s - %s" % (type, sub)

    print ""

    return 0


#########################################################
#########################################################
#
# MAIN FUNCTION
#
commands = {
    "add"           : cmd_add,
    "cache"         : cmd_cache,
    "daemon"        : cmd_daemon,
    "delta"         : cmd_delta,
    "exit"          : cmd_exit,
    "help"          : cmd_help,
    "list"          : cmd_list,
    "related"       : cmd_related,
    "subtypes"      : cmd_subtypes,
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
