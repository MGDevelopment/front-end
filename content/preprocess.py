
import ecommerce.db

# empty cache
_cache = None

def preProcess(entities, application = None):
    """Change the dataset for SUBJ entries
    
    The change requires accessing the database to check
    if the SUBJ is a section, group, family or subfamily
    and changing the dataset name to include "Section",
    "Group", "Family" or "Subfamily" at the end. The
    table checked is stage0_subjects.
    """

    # sanity checks
    if entities is None:
        return None

    # make sure the cache is loaded
    _loadCache()

    # iterate the entities and change dataset as needed
    for i in range(len(entities)):

        # if not a SUBJ => continue
        if entities[i][0] != 'SUBJ':
            continue

        # find subtype in cache and entity id
        entityId = entities[i][1]
        dataset  = entities[i][2]
        subtype  = _cache.get(entities[i][1], "")

        # replace the tuple
        entities[i] = ('SUBJ', entityId, dataset + subtype)

    return entities

def _loadCache():
    """Load the cache if not already loaded"""

    global _cache

    # sanity check
    if _cache is not None:
        return

    # get a connection to default db
    conn = ecommerce.db.getConnection()
    cursor = conn.cursor()

    # execute the query
    cursor.execute("SELECT SubjectId, Subtype FROM Stage0_Subjects")

    # fetch the records and create the cache
    cache = { }
    row = cursor.fetchone()
    while row is not None:
        cache[row[0]] = row[1]
        row = cursor.fetchone()

    # save the cache
    _cache = cache


