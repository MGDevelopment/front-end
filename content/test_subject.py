
import datetime
import pprint

import ecommerce.db.dataset

import preprocess

print "Started at %s" % str(datetime.datetime.now())

ecommerce.db.dataset.configApplication("content")
ecommerce.db.dataset.setPreProcess(preprocess.preProcess)
entities = [
    # books
    ( 'SUBJ', 1,   'subjectMain' ),     # (1, -1, -1, -1)
    ( 'SUBJ', 1,   'subjectData' ),
    ( 'SUBJ', 1,   'subjectComments' ),
    ( 'SUBJ', 2,   'subjectMain' ),     # (1, 1, -1, -1) / ficcion y literatura
    ( 'SUBJ', 2,   'subjectData' ),
    ( 'SUBJ', 2,   'subjectComments' ),
    ( 'SUBJ', 3,   'subjectMain' ),     # (1, 1, 1, -1) / ficcion y literatura / novelas
    ( 'SUBJ', 3,   'subjectData' ),
    ( 'SUBJ', 3,   'subjectComments' ),
    ( 'SUBJ', 4,   'subjectMain' ),     # (1, 1, 1, 1) / ficcion y literatura / novelas / general
    ( 'SUBJ', 4,   'subjectData' ),
    ( 'SUBJ', 4,   'subjectComments' ),
    # games
    ( 'SUBJ', 619, 'subjectMain' ),     # (3, -1, -1, -1)
    ( 'SUBJ', 619, 'subjectData' ),
    ( 'SUBJ', 619, 'subjectComments' ),
    ( 'SUBJ', 620, 'subjectMain' ),     # (3, 1, -1, -1)
    ( 'SUBJ', 620, 'subjectData' ),
    ( 'SUBJ', 620, 'subjectComments' ),
    # music
    ( 'SUBJ', 730, 'subjectMain' ),     # (4, -1, -1, -1)
    ( 'SUBJ', 730, 'subjectData' ),
    ( 'SUBJ', 730, 'subjectComments' ),
    ( 'SUBJ', 731, 'subjectMain' ),     # (4, 1, -1, -1)
    ( 'SUBJ', 731, 'subjectData' ),
    ( 'SUBJ', 731, 'subjectComments' ),
    # movies
    ( 'SUBJ', 791, 'subjectMain' ),     # (5, -1, -1, -1)
    ( 'SUBJ', 791, 'subjectData' ),
    ( 'SUBJ', 791, 'subjectComments' ),
    ( 'SUBJ', 796, 'subjectMain' ),     # (5, 1, -1, -1)
    ( 'SUBJ', 795, 'subjectData' ),
    ( 'SUBJ', 795, 'subjectComments' )
]

dump = {
    "sample/sample_data_books_1.py"        : [
        ( "books_1_main",            0 ),
        ( "books_1_data",            1 ),
        ( "books_1_comments",        2 )
    ],
    "sample/sample_data_books_1_1.py"      : [
        ( "books_1_1_main",          3 ),
        ( "books_1_1_data",          4 ),
        ( "books_1_1_comments",      5 )
    ],
    "sample/sample_data_books_1_1_1.py"    : [
        ( "books_1_1_1_main",        6 ),
        ( "books_1_1_1_data",        7 ),
        ( "books_1_1_1_comments",    8 )
    ],
    "sample/sample_data_books_1_1_1_1.py"  : [
        ( "books_1_1_1_1_main",      9 ),
        ( "books_1_1_1_1_data",     10 ),
        ( "books_1_1_1_1_comments", 11 )
    ],
    "sample/sample_data_games_3.py"        : [
        ( "games_3_main",           12 ),
        ( "games_3_data",           13 ),
        ( "games_3_comments",       14 )
    ],
    "sample/sample_data_games_3_1.py"        : [
        ( "games_3_1_main",         15 ),
        ( "games_3_1_data",         16 ),
        ( "games_3_1_comments",     17 )
    ],
    "sample/sample_data_music_4.py"        : [
        ( "music_4_main",           18 ),
        ( "music_4_data",           19 ),
        ( "music_4_comments",       20 )
    ],
    "sample/sample_data_music_4_1.py"        : [
        ( "music_4_1_main",         21 ),
        ( "music_4_1_data",         22 ),
        ( "music_4_1_comments",     23 )
    ],
    "sample/sample_data_movies_5.py"       : [
        ( "movies_5_main",          24 ),
        ( "movies_5_data",          25 ),
        ( "movies_5_comments",      26 )
    ],
    "sample/sample_data_movies_5_1.py"       : [
        ( "movies_5_1_main",        27 ),
        ( "movies_5_1_data",        28 ),
        ( "movies_5_1_comments",    29 )
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
