"""Functions related to puting things in the work queue

Functions implemented in this file are:

- cmd_add
- cmd_exit
- cmd_delta
- cmd_cache
- cmd_list
- cmd_related

"""

import ecommerce.config
import ecommerce.db
from   ecommerce.queue import *

from globals import *
import jobs

#########################################################

#
# get a queue producer
#
def getProducer():
    """Get a Producer queue instance"""

    # get the config and a producer
    config = ecommerce.config.getConfig()
    return ecommerce.queue.queue(config, queuePrefix)

#########################################################

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

def generateJobs(producer, EntityType, eList, tag = None):

    # build jobs of up to 256 entries
    jobCount = 0
    jList = [ ]
    for i in range(len(eList)):
        # append the entity
        jList.append( [ EntityType, eList[i] ] )

        # if max number of entities reached, send job
        if len(jList) == maxEntities:

            # create the job
            job = jobs.encode(jobs.generate(jList, tag))

            # get an item, set content and make it ready
            item = producer.item()
            item.content = job
            producer.ready(item)
            jobCount += 1

            # new list
            jList = [ ]

    # if list not empty, send job
    if len(jList) > 0:

        # create the job
        job = jobs.encode(jobs.generate(jList, tag))

        # get an item, set content and make it ready
        item = producer.item()
        item.content = job
        producer.ready(item)
        jobCount += 1

    return jobCount

#########################################################
#########################################################
#
# COMMAND - ADD
#
def cmd_add(arguments):
    """Puts generate commands into the queue"""

    # build the list of entities
    entities = { type : [ ] for type in entityTypes }
    type     = ""
    param    = 1            # skip "add" command
    while param < len(arguments):

        # get an entity type and check it's valid
        fullType = arguments[param]
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
        if arguments[param] == "*":

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
            while param < len(arguments):

                try:
                    eList.append(int(arguments[param]))
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
        partialJobCount = generateJobs(producer, type, elist)

        # report
        if partialJobCount > 0:
            print "added %5d jobs for entity %s" % (partialJobCount, fullType)
            jobCount += partialJobCount

    # report the number of jobs created
    print ""
    print "Added a total of %5d jobs in queue" % jobCount
    print ""

    return 0


#########################################################
#########################################################
#
# COMMAND - DELTA
#
def max_entity_date(entity_type):
    """Get the LastUpdateDate for this type of entity"""

    # assume empty date
    max_date = None
    try:

        # get a cursor
        conn = ecommerce.db.getConnection()
        cursor = conn.cursor()

        # execute the query
        cursor.execute("""
                SELECT          TO_CHAR(LastUpdateDate, 'YYYY-MM-DD HH24:MI:SS')
                    FROM        Stage0_DeltaControl
                    WHERE       EntityType = ?
            """, (entity_type, ) )

        # fetch the max date
        row = cursor.fetchone()
        if row is not None:
            max_date = row[0]
        cursor.close()
    except:
        pass

    return max_date


def list_modified_entities(entity_type, max_date):
    """Get the list of modified entities before a specified date"""

    # get a cursor
    conn = ecommerce.db.getConnection()
    cursor = conn.cursor()

    # execute the query
    cursor.execute("""
                SELECT          EntityId
                    FROM        Stage0_Delta
                    WHERE       EntityType = ? AND
                                FlagUpdated = 1 AND
                                LastUpdate <= TO_DATE(?, 'YYYY-MM-DD HH24:MI:SS')
        """, (entity_type, max_date) )

    # fetch the ids
    elist = [ ]
    row = cursor.fetchone()
    while row is not None:
        elist.append(int(row[0]))
        row = cursor.fetchone()
    cursor.close()

    return elist


def mark_processed_entities(entity_type, max_date):
    """Mark the entities modified before a specific date as processed"""

    try:
    
        # get a connection and cursor
        conn = ecommerce.db.getConnection()
        cursor = conn.cursor()
    
        # execute the query
        cursor.execute("""
                UPDATE Stage0_Delta
                    SET         FlagUpdated = 0
                    WHERE       EntityType = ? AND
                                FlagUpdated = 1 AND
                                LastUpdate <= TO_DATE(?, 'YYYY-MM-DD HH24:MI:SS')
            """, (entity_type, max_date) )
    
        # commit changes
        conn.commit()
    except:
        conn.rollback()
        pass


def cmd_delta(arguments):
    """Process the Stage0_Delta table and create queue commands
    to process each record that has FlagUpdated = 1
    """
    cmd_delta.entities = [
        # each entry is a 2-uple, stating the EntityType and
        # wheter if queue jobs must be generated or not
        ( "CONT", False ),
        ( "IMPR", False ),
        ( "_DSP", False ),
        ( "SUBJ", True  ),
        ( "PROD", True  ),
        ( "PAGE", True  )
    ]

    # iterate each entity type
    for e in range(len(cmd_delta.entities)):

        # get handy values
        entity_type = cmd_delta.entities[e][0]
        generate    = cmd_delta.entities[e][1]

        print "Processing Entity %s" % (entity_type),
        logger.info("Processing Entity %s" % (entity_type))

        # get the max date
        max_date = max_entity_date(entity_type)
        if max_date is not None:

            # get the list of modified entities (if we need to generate)
            entities = [ ]
            if generate:
            
                # get the list of entities
                entities = list_modified_entities(entity_type, max_date)

                # generate queue jobs
                producer = getProducer()
                partialJobCount = generateJobs(producer, entity_type, entities)

            # mark entities as processed
            if max_date is not None:
                mark_processed_entities(entity_type, max_date)

            print "- DONE (%d entities)" % len(entities)
            logger.info("Processed Entity %s OK (%d entities)" % (entity_type, len(entities)))
        else:
            print "- ERROR"
            logger.info("Processed Entity %s with ERROR" % (entity_type))

    return 0


#########################################################
#########################################################
#
# COMMAND - EXIT
#
def cmd_exit(arguments):

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
def cmd_cache(arguments):

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
# COMMAND - LIST
#
def cmd_list(arguments):
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
# COMMAND - REGEN
#
cmd_regen_subcommands       = {
    #
    # PROD
    #
    "PROD/main"             : {
        "name"              : "PROD/main",
        "desc"              : "Regenerate the documents that match PROD and tag 'main'",
        "type"              : "PROD",
        "tag"               : "main",
        "query"             : """
            SELECT          D.EntityId
                FROM        Stage0_Delta D
                INNER JOIN  Articulos A
                    ON      D.EntityId = A.Id_Articulo AND
                            A.Categoria_Seccion IN (1, 3, 4, 5) AND
                            A.Activo = 'SI' AND
                            A.Habilitado_Tematika = 'S'
                WHERE       D.EntityType = 'PROD'
                ORDER BY    D.EntityId DESC
        """
    },
    "PROD/related"          : {
        "name"              : "PROD/related",
        "desc"              : "Regenerate the documents that match PROD and tag 'related'",
        "type"              : "PROD",
        "tag"               : "related",
        "query"             : """
            SELECT          A.Id_Articulo
                FROM        Articulos A
                WHERE       A.Categoria_Seccion IN (1, 3, 4, 5) AND
                            A.Activo = 'SI' AND
                            A.Habilitado_Tematika = 'S' AND
                            A.Id_Articulo IN (
                                    SELECT      AR.Id_Articulo
                                        FROM    RCO_Articulos_Relacionados AR
                            )
                ORDER BY    A.Id_Articulo DESC
        """
    },
    "PROD/price"            : {
        "name"              : "PROD/price",
        "desc"              : "Regenerate the documents that match PROD and tag 'price'",
        "type"              : "PROD",
        "tag"               : "price",
        "query"             : """
            SELECT          D.EntityId
                FROM        Stage0_Delta D
                INNER JOIN  Articulos A
                    ON      D.EntityId = A.Id_Articulo AND
                            A.Categoria_Seccion IN (1, 3, 4, 5) AND
                            A.Activo = 'SI' AND
                            A.Habilitado_Tematika = 'S'
                WHERE       D.EntityType = 'PROD'
                ORDER BY    D.EntityId DESC
        """
    },
    "PROD/comment"          : {
        "name"              : "PROD/comment",
        "desc"              : "Regenerate the documents that match PROD and tag 'comment'",
        "type"              : "PROD",
        "tag"               : "comment",
        "query"             : """
            SELECT          D.EntityId
                FROM        Stage0_Delta D
                INNER JOIN  Articulos A
                    ON      D.EntityId = A.Id_Articulo AND
                            A.Categoria_Seccion IN (1, 3, 4, 5) AND
                            A.Activo = 'SI' AND
                            A.Habilitado_Tematika = 'S'
                WHERE       D.EntityType = 'PROD' AND
                            D.EntityId IN (
                                SELECT          CA.Id_Articulo
                                    FROM        Comentario_Articulos CA
                                    WHERE       CA.Estado = 'A'
                            )
                ORDER BY    D.EntityId DESC
        """
    },
    #
    # PAGE
    #
    "PAGE/1/main"           : {
        "name"              : "PAGE/1/main",
        "desc"              : "Regenerate the HOME documents that match the tag 'main'",
        "type"              : "PAGE",
        "tag"               : "main",
        "query"             : """
                SELECT          EntityId
                    FROM        Stage0_Delta
                    WHERE       EntityType = 'PAGE' AND
                                EntityId = 1
        """
    },
    "PAGE/1/price"          : {
        "name"              : "PAGE/1/price",
        "desc"              : "Regenerate the HOME documents that match the tag 'price'",
        "type"              : "PAGE",
        "tag"               : "price",
        "query"             : """
                SELECT          EntityId
                    FROM        Stage0_Delta
                    WHERE       EntityType = 'PAGE' AND
                                EntityId = 1
        """
    },
    "PAGE/1/comment"        : {
        "name"              : "PAGE/1/comment",
        "desc"              : "Regenerate the HOME documents that match the tag 'comment'",
        "type"              : "PAGE",
        "tag"               : "comment",
        "query"             : """
                SELECT          EntityId
                    FROM        Stage0_Delta
                    WHERE       EntityType = 'PAGE' AND
                                EntityId = 1
        """
    },
    #
    # SUBJ
    #
    "SUBJ/main"             : {
        "name"              : "SUBJ/main",
        "desc"              : "Regenerate the documents that match SUBJ and tag 'main'",
        "type"              : "SUBJ",
        "tag"               : "main",
        "query"             : """
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
                                D.EntityType = 'SUBJ'
                    ORDER BY    2, D.EntityId
        """
    },
    "SUBJ/comment"        : {
        "name"              : "SUBJ/comment",
        "desc"              : "Regenerate the documents that match SUBJ and tag 'comment'",
        "type"              : "SUBJ",
        "tag"               : "comment",
        "query"             : """
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
                                D.EntityType = 'SUBJ'
                    ORDER BY    2, D.EntityId
        """
    }
}

def cmd_regen(arguments):
    """Regenerate several components"""

    # if no extra arguments => dump the list of subcommands
    if len(arguments) < 2:
        # explain the command and print the list of subcommands
        print ""
        print "The regen command provides for a handy method to regenerate"
        print "some subset of files. The available options are:"
        print ""
        for k in sorted(cmd_regen_subcommands.keys()):
            print "%-16s - %s" % (k, cmd_regen_subcommands[k]["desc"])

        return 0

    # get a queue producer
    producer = getProducer()
    jobCount = 0

    # start processing subcommands
    param = 1           # skip command name
    while param < len(arguments):

        # get the subcommand and check it's valid
        subcmd = arguments[param]
        if subcmd not in cmd_regen_subcommands:
            print "ERROR: invalid subcommand [%s], ignoring" % subcmd
            param += 1
            continue

        # get some data
        tag   = cmd_regen_subcommands[subcmd]["tag"]
        query = cmd_regen_subcommands[subcmd]["query"]
        type  = cmd_regen_subcommands[subcmd]["type"]

        # get the list (execute the query)
        eList = [ ]
        try:
            print "Retrieving entities for %s" % subcmd

            # get a connection and cursor
            conn = ecommerce.db.getConnection()
            cursor = conn.cursor()

            # execute the query
            cursor.execute(query)

            # fetch the ids
            row = cursor.fetchone()
            while row is not None:
                eList.append(int(row[0]))
                row = cursor.fetchone()
            cursor.close()
        except:
            pass

        # generate as many jobs as needed
        partialJobCount = 0     # assume nothing to do
        if len(eList) > 0:
            partialJobCount = generateJobs(producer, type, eList, tag)

        # report
        if partialJobCount > 0:
            print "added %5d jobs for entity %s" % (partialJobCount, subcmd)
            jobCount += partialJobCount

        # next subcommand
        param += 1

    # report the number of jobs created
    print ""
    print "Added a total of %5d jobs in queue" % jobCount
    print ""

    return 0


#########################################################
#########################################################
#
# COMMAND - SITEMAP
#
def cmd_sitemap(arguments):
    """List the job queue"""

    # create a sitemap job
    job = jobs.encode(jobs.sitemap())

    # get a producer
    producer = getProducer()

    # get an item, set content and make it ready
    item = producer.item()
    item.content = job
    producer.ready(item)

    print "Sitemap command put in queue"

    return 0
