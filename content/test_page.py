
import datetime
import pprint

import ecommerce.db.dataset

import preprocess

print "Started at %s" % str(datetime.datetime.now())

ecommerce.db.dataset.configApplication("content")
ecommerce.db.dataset.setPreProcess(preprocess.preProcess)
entities = [
    # home page
    ( 'PAGE', 1,   'homeMain' ),
    ( 'PAGE', 1,   'homeShowcase' ),
    ( 'PAGE', 1,   'homeComments' ),
    ( 'PAGE', 1,   'homePrice' )
]

dump = {
    "sample/sample_data.py"         : [
        ( "homeMainData",           0 ),
        ( "homeShowcaseData",       1 ),
        ( "homeCommentsData",       2 ),
        ( "homePriceData",          3 )
    ]
}

result = ecommerce.db.dataset.fetch(entities, "content")

for fname in dump:
    
    # open the output file
    f = open(fname, "w")

    f.writelines( [ "from decimal import Decimal\n", "import datetime\n", "\n", "\n" ] )

    # get the list of entries
    entries = dump[fname]

    for e in range(len(entries)):

        # get the entry and the data
        entry = entries[e]
        data  = result[entry[1]][3]

        f.writelines( [ "##############################\n", "#\n", "#\n" ] )
        f.write(entry[0] + " = " + pprint.pformat(data, 4))
        f.write("\n")
        f.write("\n")

    f.close

print "Ended at %s" % str(datetime.datetime.now())
