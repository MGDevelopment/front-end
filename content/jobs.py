"""This file implements the job format

Jobs are basic data structures (hashmaps, lists, strings,
numbers, and booleans) and are encoded using json.

by Jose Luis Campanello
"""

import json

#########################################################
#########################################################
#
# Encoding/Decoding
#

def encode(job):
    """Return a string representation of the job"""

    return json.dumps(job)


def decode(s):
    """Return the job of a string representation"""

    return json.loads(s)


#########################################################
#########################################################
#
# JOB - EXIT
#
def exit(tag = "*", design = "*", store = "*"):
    """Create a job of type exit"""

    job = {
        "type"      : "exit",
        "tag"       : tag,
        "design"    : design,
        "store"     : store
    }
    return job


#########################################################
#########################################################
#
# JOB - GENERATE
#
def generate(entities, tag = "*", design = "*", store = "*"):
    """Create a job of type generate
    
    The entities parameter is an array of 2-uples (EntityType, EntityId)
    """

    # convert entities from list of 2-uples to list of lists
    _entities = [ [ e[0], e[1] ] for e in entities ]

    job = {
        "type"      : "generate",
        "tag"       : tag,
        "design"    : design,
        "store"     : store,
        "entities"  : _entities
    }
    return job

