
import datetime
import pprint

import ecommerce.db.dataset

import preprocess

print "Started at %s" % str(datetime.datetime.now())

ecommerce.db.dataset.configApplication("content")
ecommerce.db.dataset.setPreProcess(preprocess.preProcess)
entities = [
    # BOOK - multiple isbn, google books
    ( 'PROD', 530061,   'productMain' ),
    ( 'PROD', 530061,   'productComments' ),
    ( 'PROD', 530061,   'productRelated' ),
    ( 'PROD', 530061,   'productPrice' ),
    # MOVIE - audiences
    ( 'PROD', 530251,   'productMain' ),
    ( 'PROD', 530251,   'productComments' ),
    ( 'PROD', 530251,   'productRelated' ),
    ( 'PROD', 530251,   'productPrice' ),
    # MUSIC - temas musicales
    ( 'PROD', 530185,   'productMain' ),
    ( 'PROD', 530185,   'productComments' ),
    ( 'PROD', 530185,   'productRelated' ),
    ( 'PROD', 530185,   'productPrice' ),
    # BOOK - tabla de contenidos, doble biografia, entrevista
    ( 'PROD', 413418,   'productMain' ),
    ( 'PROD', 413418,   'productComments' ),
    ( 'PROD', 413418,   'productRelated' ),
    ( 'PROD', 413418,   'productPrice' ),
    # BOOK - primer capitulo
    ( 'PROD', 526900,   'productMain' ),
    ( 'PROD', 526900,   'productComments' ),
    ( 'PROD', 526900,   'productRelated' ),
    ( 'PROD', 526900,   'productPrice' ),
    # BOOK - biografia (para el libro)
    ( 'PROD', 493520,   'productMain' ),
    ( 'PROD', 493520,   'productComments' ),
    ( 'PROD', 493520,   'productRelated' ),
    ( 'PROD', 493520,   'productPrice' ),
    # BOOK - contratapa y solapa
    ( 'PROD', 530141,   'productMain' ),
    ( 'PROD', 530141,   'productComments' ),
    ( 'PROD', 530141,   'productRelated' ),
    ( 'PROD', 530141,   'productPrice' ),
    # BOOK - contratapa y solapa
    ( 'PROD', 465771,   'productMain' ),
    ( 'PROD', 465771,   'productComments' ),
    ( 'PROD', 465771,   'productRelated' ),
    ( 'PROD', 465771,   'productPrice' ),
    # MOVIE - audiences y descripcion
    ( 'PROD', 529368,   'productMain' ),
    ( 'PROD', 529368,   'productComments' ),
    ( 'PROD', 529368,   'productRelated' ),
    ( 'PROD', 529368,   'productPrice' ),
    # MUSIC - descripcion
    ( 'PROD', 527054,   'productMain' ),
    ( 'PROD', 527054,   'productComments' ),
    ( 'PROD', 527054,   'productRelated' ),
    ( 'PROD', 527054,   'productPrice' ),
    # GAME - descripcion
    ( 'PROD', 529503,   'productMain' ),
    ( 'PROD', 529503,   'productComments' ),
    ( 'PROD', 529503,   'productRelated' ),
    ( 'PROD', 529503,   'productPrice' ),
    # BOOK - ingles
    ( 'PROD', 516261,   'productMain' ),
    ( 'PROD', 516261,   'productComments' ),
    ( 'PROD', 516261,   'productRelated' ),
    ( 'PROD', 516261,   'productPrice' ),
    # BOOK - castellano
    ( 'PROD', 516262,   'productMain' ),
    ( 'PROD', 516262,   'productComments' ),
    ( 'PROD', 516262,   'productRelated' ),
    ( 'PROD', 516262,   'productPrice' ),
    # MOVIE - DVD
    ( 'PROD', 527159,   'productMain' ),
    ( 'PROD', 527159,   'productComments' ),
    ( 'PROD', 527159,   'productRelated' ),
    ( 'PROD', 527159,   'productPrice' ),
    # MOVIE - BLU-RAY
    ( 'PROD', 529815,   'productMain' ),
    ( 'PROD', 529815,   'productComments' ),
    ( 'PROD', 529815,   'productRelated' ),
    ( 'PROD', 529815,   'productPrice' ),
    # BOOK - 501952
    ( 'PROD', 501952,   'productMain' ),
    ( 'PROD', 501952,   'productComments' ),
    ( 'PROD', 501952,   'productRelated' ),
    ( 'PROD', 501952,   'productPrice' )
]

dump = {
    "sample/sample_product_book_530061.py"  : [
        ( "products_530061_main",        0 ),
        ( "products_530061_comments",    1 ),
        ( "products_530061_related",     2 ),
        ( "products_530061_price",       3 )
    ],
    "sample/sample_product_movie_530251.py"  : [
        ( "products_530251_main",        4 ),
        ( "products_530251_comments",    5 ),
        ( "products_530251_related",     6 ),
        ( "products_530251_price",       7 )
    ],
    "sample/sample_product_music_530185.py"  : [
        ( "products_530185_main",        8 ),
        ( "products_530185_comments",    9 ),
        ( "products_530185_related",    10 ),
        ( "products_530185_price",      11 )
    ],
    "sample/sample_product_book_413418.py"  : [
        ( "products_413418_main",       12 ),
        ( "products_413418_comments",   13 ),
        ( "products_413418_related",    14 ),
        ( "products_413418_price",      15 )
    ],
    "sample/sample_product_book_526900.py"  : [
        ( "products_526900_main",       16 ),
        ( "products_526900_comments",   17 ),
        ( "products_526900_related",    18 ),
        ( "products_526900_price",      19 )
    ],
    "sample/sample_product_book_493520.py"  : [
        ( "products_493520_main",       20 ),
        ( "products_493520_comments",   21 ),
        ( "products_493520_related",    22 ),
        ( "products_493520_price",      23 )
    ],
    "sample/sample_product_book_530141.py"  : [
        ( "products_530141_main",       24 ),
        ( "products_530141_comments",   25 ),
        ( "products_530141_related",    26 ),
        ( "products_530141_price",      27 )
    ],
    "sample/sample_product_book_465771.py"  : [
        ( "products_465771_main",       28 ),
        ( "products_465771_comments",   29 ),
        ( "products_465771_related",    30 ),
        ( "products_465771_price",      31 )
    ],
    "sample/sample_product_movie_529368.py"  : [
        ( "products_529368_main",       32 ),
        ( "products_529368_comments",   33 ),
        ( "products_529368_related",    34 ),
        ( "products_529368_price",      35 )
    ],
    "sample/sample_product_music_527054.py"  : [
        ( "products_527054_main",       36 ),
        ( "products_527054_comments",   37 ),
        ( "products_527054_related",    38 ),
        ( "products_527054_price",      39 )
    ],
    "sample/sample_product_game_529503.py"  : [
        ( "products_529503_main",       40 ),
        ( "products_529503_comments",   41 ),
        ( "products_529503_related",    42 ),
        ( "products_529503_price",      43 )
    ],
    "sample/sample_product_book_516261.py"  : [
        ( "products_516261_main",       44 ),
        ( "products_516261_comments",   45 ),
        ( "products_516261_related",    46 ),
        ( "products_516261_price",      47 )
    ],
    "sample/sample_product_book_516262.py"  : [
        ( "products_516262_main",       48 ),
        ( "products_516262_comments",   49 ),
        ( "products_516262_related",    50 ),
        ( "products_516262_price",      51 )
    ],
    "sample/sample_product_movie_527159.py"  : [
        ( "products_527159_main",       52 ),
        ( "products_527159_comments",   53 ),
        ( "products_527159_related",    54 ),
        ( "products_527159_price",      55 )
    ],
    "sample/sample_product_movie_529815.py"  : [
        ( "products_529815_main",       56 ),
        ( "products_529815_comments",   57 ),
        ( "products_529815_related",    58 ),
        ( "products_529815_price",      59 )
    ],
    "sample/sample_product_book_501952.py"  : [
        ( "products_501952_main",       60 ),
        ( "products_501952_comments",   61 ),
        ( "products_501952_related",    62 ),
        ( "products_501952_price",      63 )
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
