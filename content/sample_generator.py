import sys, getopt
from   ecommerce.storage  import FilesystemStorage, S3Storage
import jinja2
from   json               import dumps as js_dump

import sample.sample_data
import sample.sample_data_books_1
import sample.sample_data_books_1_1
import sample.sample_data_books_1_1_1
import sample.sample_data_books_1_1_1_1
import sample.sample_data_games_3
import sample.sample_data_music_4
import sample.sample_data_music_4_1
import sample.sample_data_movies_5
import sample.sample_product_book_413418
import sample.sample_product_book_465771
import sample.sample_product_music_530185
import sample.sample_product_movie_529368


# String to wrap HTML content with JS loader
JS_WRAP = '''with(window.open("","_blank","width="+screen.width*.6+",left="+screen.width*.2+",height="+screen.height*.9+",resizable,scrollbars=yes")){document.write( %s );document.close();}void 0'''

#
# Config
#
# What S3 bucket is target for what host.domain
storage = {
    's3': {
        "dynamic": "beta1.testmatika.com",
        "static":  "beta1.testmatika.com",
    },
    'folder': {
        "dynamic": "./out",
        "static":  "./out"
    }
}


############################################################
############################################################
############################################################
#
# URLs
#

homeURL = {
    "cannonical"    : "/",
    "urls"          : [ "/index.html", "/index.jsp" ],
    "static"        : "http://estatico.tematika.com",
    "dynamic"       : "http://www.tematika.com",
    "search"        : "http://buscador.tematika.com",
    "checkout"      : "http://seguro.tematika.com",
    "service"       : "http://servicios.tematika.com",
    "images"        : "http://img-tmk.tematika.com",
    "data"          : "http://beta1.testmatika.com.s3-website-us-east-1.amazonaws.com"
}

librosURL = {
    "cannonical"    : "/libros/",
    "urls"          : [ "/libros", "/libros/index.html", "/libros/index.jsp" ],
    "static"        : "http://estatico.tematika.com",
    "dynamic"       : "http://www.tematika.com",
    "search"        : "http://buscador.tematika.com",
    "checkout"      : "http://seguro.tematika.com",
    "service"       : "http://servicios.tematika.com",
    "images"        : "http://img-tmk.tematika.com",
    "data"          : "http://beta1.testmatika.com.s3-website-us-east-1.amazonaws.com"
}

musicaURL = {
    "cannonical"    : "/musica/",
    "urls"          : [ "/musica", "/musica/index.html", "/musica/index.jsp" ],
    "static"        : "http://estatico.tematika.com",
    "dynamic"       : "http://www.tematika.com",
    "search"        : "http://buscador.tematika.com",
    "checkout"      : "http://seguro.tematika.com",
    "service"       : "http://servicios.tematika.com",
    "images"        : "http://img-tmk.tematika.com",
    "data"          : "http://beta1.testmatika.com.s3-website-us-east-1.amazonaws.com"
}

peliculasURL = {
    "cannonical"    : "/peliculas/",
    "urls"          : [ "/peliculas", "/peliculas/index.html", "/peliculas/index.jsp" ],
    "static"        : "http://estatico.tematika.com",
    "dynamic"       : "http://www.tematika.com",
    "search"        : "http://buscador.tematika.com",
    "checkout"      : "http://seguro.tematika.com",
    "service"       : "http://servicios.tematika.com",
    "images"        : "http://img-tmk.tematika.com",
    "data"          : "http://beta1.testmatika.com.s3-website-us-east-1.amazonaws.com"
}

pasatiemposURL = {
    "cannonical"    : "/pasatiempos/",
    "urls"          : [ "/pasatiempos", "/pasatiempos/index.html", "/pasatiempos/index.jsp" ],
    "static"        : "http://estatico.tematika.com",
    "dynamic"       : "http://www.tematika.com",
    "search"        : "http://buscador.tematika.com",
    "checkout"      : "http://seguro.tematika.com",
    "service"       : "http://servicios.tematika.com",
    "images"        : "http://img-tmk.tematika.com",
    "data"          : "http://beta1.testmatika.com.s3-website-us-east-1.amazonaws.com"
}

############################################################
############################################################
############################################################
#
# DOCUMENTOS A GENERAR
#

documentos = [
    #######################################################
    #
    # home - html
    #
    ########## /index.html
    {
        "EntityType"    : "PAGE",
        "EntityId"      : 1,
        "dataset"       : "homeMain",          "_data" : sample.sample_data.homeMainData,
                                               "_url"  : homeURL,
        "template"      : "home/index.html",
        "headers"       : {
            "Content-Type"      : "text/html",
            "Content-Encoding"  : "gzip",
            "Cache-Control"     : "max-age=3600"
        },
        "target.path"   : "/index.html",
        "target.repo"   : "dynamic"
    },
    ########## /index.html
    {
        "EntityType"    : "PAGE",
        "EntityId"      : 1,
        "dataset"       : "homeMain",          "_data" : sample.sample_data.homeMainData,
                                               "_url"  : homeURL,
        "template"      : "home/index.html",
        "headers"       : {
            "Content-Type"      : "text/html",
            "Content-Encoding"  : "gzip",
            "Cache-Control"     : "max-age=3600"
        },
        "target.path"   : "/index.jsp",
        "target.repo"   : "dynamic"
    },
    #
    # home - vidrieras
    #
    {
        "EntityType"    : "PAGE",
        "EntityId"      : 1,
        "dataset"       : "homeShowcase",       "_data" : sample.sample_data.homeShowcaseData,
                                                "_url"  : homeURL,
        "template"      : "home/showcase.js",
        "headers"       : {
            "Content-Type"      : "text/javascript",        # requerido por IE
            "Content-Encoding"  : "gzip",
            "Cache-Control"     : "max-age=3600"
        },
        "target.path"   : "/home-showcase.js",
        "target.repo"   : "static"
    },
    #
    # home - comentarios
    #
    {
        "EntityType"    : "PAGE",
        "EntityId"      : 1,
        "dataset"       : "homeComments",       "_data" : sample.sample_data.homeCommentsData,
                                                "_url"  : homeURL,
        "template"      : "home/comments.js",
        "headers"       : {
            "Content-Type"      : "text/javascript",        # requerido por IE
            "Content-Encoding"  : "gzip",
            "Cache-Control"     : "max-age=3600"
        },
        "target.path"   : "/home-comments.js",
        "target.repo"   : "static"
    },
    #######################################################
    #
    # libros - html
    #
    ########## /libros
#    {
#        "EntityType"    : "SUBJ",
#        "EntityId"      : 1,
#        "dataset"       : "subjectMain",        "_data" : sample.sample_data_books_1.books_1_main,
#                                                "_url"  : librosURL,
#        "template"      : "subject/index.html",
#        "headers"       : {
#            "Content-Type"      : "text/html",
#            "Content-Encoding"  : "gzip",
#            "Cache-Control"     : "max-age=3600"
#        },
#        "target.path"   : "/libros",
#        "target.repo"   : "dynamic"
#    },
    ########## /libros/index.html
    {
        "EntityType"    : "SUBJ",
        "EntityId"      : 1,
        "dataset"       : "subjectMain",        "_data" : sample.sample_data_books_1.books_1_main,
                                                "_url"  : librosURL,
        "template"      : "subject/index.html",
        "headers"       : {
            "Content-Type"      : "text/html",
            "Content-Encoding"  : "gzip",
            "Cache-Control"     : "max-age=3600"
        },
        "target.path"   : "/libros/index.html",
        "target.repo"   : "dynamic"
    },
    ########## /catalogo/libros.js More
    {
        "EntityType"    : "SUBJ",
        "EntityId"      : 1,
        "dataset"       : "subjectComments",    "_data" : sample.sample_data_books_1.books_1_data,
                                                "_url"  : librosURL,
        "template"      : "subject/catalog.js",
        "headers"       : {
            "Content-Type"      : "text/javascript",
            "Content-Encoding"  : "gzip",
            "Cache-Control"     : "max-age=3600"
        },
        "target.path"   : "/catalog/libros.js",
        "target.repo"   : "static"
    },

    #
    # libros - vidrieras
    #
    {
        "EntityType"    : "SUBJ",
        "EntityId"      : 1,
        "dataset"       : "subjectShowcase",    "_data" : sample.sample_data_books_1.books_1_data,
                                                "_url"  : librosURL,
        "template"      : "subject/showcase.js",
        "headers"       : {
            "Content-Type"      : "text/javascript",        # requerido por IE
            "Content-Encoding"  : "gzip",
            "Cache-Control"     : "max-age=3600"
        },
        "target.path"   : "/showcase/libros.js",
        "target.repo"   : "static"
    },
    #
    # libros - comentarios
    #
    {
        "EntityType"    : "SUBJ",
        "EntityId"      : 1,
        "dataset"       : "subjectComments",    "_data" : sample.sample_data_books_1.books_1_comments,
                                                "_url"  : librosURL,
        "template"      : "subject/comments.js",
        "headers"       : {
            "Content-Type"      : "text/javascript",        # requerido por IE
            "Content-Encoding"  : "gzip",
            "Cache-Control"     : "max-age=3600"
        },
        "target.path"   : "/comments/libros.js",
        "target.repo"   : "static"
    },

    ########## /catalogo/libros/ficcion_y_literatura--1.htm
    {
        "EntityType"    : "SUBJ",
        "EntityId"      : 1,
        "dataset"       : "subjectMain",
        "_data"         : sample.sample_data_books_1_1.books_1_1_main,
        "_url"          : dict(librosURL, **{'cannonical': "/catalogo/libros/ficcion_y_literatura--1"}),
        "template"      : "subject/index.html",
        "headers"       : {
            "Content-Type"      : "text/html",
            "Content-Encoding"  : "gzip",
            "Cache-Control"     : "max-age=3600"
        },
        "target.path"   : "/catalogo/libros/ficcion_y_literatura--1.htm",
        "target.repo"   : "dynamic"
    },
    ########## /catalogo/libros/ficcion_y_literatura--1 showcase
    {
        "EntityType"    : "SUBJ",
        "EntityId"      : 1,
        "dataset"       : "subjectShowcase",    "_data" : sample.sample_data_books_1_1.books_1_1_data,
                                                "_url"  : librosURL,
        "template"      : "subject/showcase.js",
        "headers"       : {
            "Content-Type"      : "text/javascript",        # requerido por IE
            "Content-Encoding"  : "gzip",
            "Cache-Control"     : "max-age=3600"
        },
        "target.path"   : "/showcase/catalogo/libros/ficcion_y_literatura--1.js",
        "target.repo"   : "static"
    },
    ########## /catalogo/libros/ficcion_y_literatura--1 comments
    {
        "EntityType"    : "SUBJ",
        "EntityId"      : 1,
        "dataset"       : "subjectComments",    "_data" : sample.sample_data_books_1_1.books_1_1_comments,
                                                "_url"  : librosURL,
        "template"      : "subject/comments.js",
        "headers"       : {
            "Content-Type"      : "text/javascript",        # requerido por IE
            "Content-Encoding"  : "gzip",
            "Cache-Control"     : "max-age=3600"
        },
        "target.path"   : "/comments/catalogo/libros/ficcion_y_literatura--1.js",
        "target.repo"   : "static"
    },

    ########## /catalogo/libros/ficcion_y_literatura--1 More
    {
        "EntityType"    : "SUBJ",
        "EntityId"      : 1,
        "dataset"       : "subjectComments",    "_data" : sample.sample_data_books_1_1.books_1_1_data,
                                                "_url"  : librosURL,
        "template"      : "subject/catalog.js",
        "headers"       : {
            "Content-Type"      : "text/javascript",
            "Content-Encoding"  : "gzip",
            "Cache-Control"     : "max-age=3600"
        },
        "target.path"   : "/catalog/catalogo/libros/ficcion_y_literatura--1.js",
        "target.repo"   : "static"
    },

    #
    # MUSICA
    #

    ########## /musica/index.html
    {
        "EntityType"    : "SUBJ",
        "EntityId"      : 1,
        "dataset"       : "subjectMain",        "_data" : sample.sample_data_music_4.music_4_main,
                                                "_url"  : musicaURL,
        "template"      : "subject/index.html",
        "headers"       : {
            "Content-Type"      : "text/html",
            "Content-Encoding"  : "gzip",
            "Cache-Control"     : "max-age=3600"
        },
        "target.path"   : "/musica/index.html",
        "target.repo"   : "dynamic"
    },

    ########## /catalogo/musica.js More
    {
        "EntityType"    : "SUBJ",
        "EntityId"      : 1,
        "dataset"       : "subjectComments",    "_data" : sample.sample_data_music_4.music_4_data,
                                                "_url"  : musicaURL,
        "template"      : "subject/catalog.js",
        "headers"       : {
            "Content-Type"      : "text/javascript",
            "Content-Encoding"  : "gzip",
            "Cache-Control"     : "max-age=3600"
        },
        "target.path"   : "/catalog/musica.js",
        "target.repo"   : "static"
    },

    #
    # musica - vidrieras
    #
    {
        "EntityType"    : "SUBJ",
        "EntityId"      : 1,
        "dataset"       : "subjectShowcase",    "_data" : sample.sample_data_music_4.music_4_data,
                                                "_url"  : musicaURL,
        "template"      : "subject/showcase.js",
        "headers"       : {
            "Content-Type"      : "text/javascript",        # requerido por IE
            "Content-Encoding"  : "gzip",
            "Cache-Control"     : "max-age=3600"
        },
        "target.path"   : "/showcase/musica.js",
        "target.repo"   : "static"
    },
    #
    # musica - comentarios
    #
    {
        "EntityType"    : "SUBJ",
        "EntityId"      : 1,
        "dataset"       : "subjectComments",    "_data" : sample.sample_data_music_4.music_4_comments,
                                                "_url"  : musicaURL,
        "template"      : "subject/comments.js",
        "headers"       : {
            "Content-Type"      : "text/javascript",        # requerido por IE
            "Content-Encoding"  : "gzip",
            "Cache-Control"     : "max-age=3600"
        },
        "target.path"   : "/comments/musica.js",
        "target.repo"   : "static"
    },
    ########## /catalogo/cds/rp_internacional--1.htm
    {
        "EntityType"    : "SUBJ",
        "EntityId"      : 1,
        "dataset"       : "subjectMain",
        "_data"         : sample.sample_data_music_4_1.music_4_1_main,
        "_url"          : dict(librosURL, **{'cannonical': "/catalogo/cds/rp_internacional--1"}),
        "template"      : "subject/index.html",
        "headers"       : {
            "Content-Type"      : "text/html",
            "Content-Encoding"  : "gzip",
            "Cache-Control"     : "max-age=3600"
        },
        "target.path"   : "/catalogo/cds/rp_internacional--1.htm",
        "target.repo"   : "dynamic"
    },
    ########## /catalogo/cds/rp_internacional--1 showcase
    {
        "EntityType"    : "SUBJ",
        "EntityId"      : 1,
        "dataset"       : "subjectShowcase",    "_data" : sample.sample_data_music_4_1.music_4_1_data,
                                                "_url"  : librosURL,
        "template"      : "subject/showcase.js",
        "headers"       : {
            "Content-Type"      : "text/javascript",        # requerido por IE
            "Content-Encoding"  : "gzip",
            "Cache-Control"     : "max-age=3600"
        },
        "target.path"   : "/showcase/catalogo/cds/rp_internacional--1.js",
        "target.repo"   : "static"
    },
    ########## /catalogo/cds/rp_internacional--1 comments
    {
        "EntityType"    : "SUBJ",
        "EntityId"      : 1,
        "dataset"       : "subjectComments",    "_data" : sample.sample_data_music_4_1.music_4_1_comments,
                                                "_url"  : librosURL,
        "template"      : "subject/comments.js",
        "headers"       : {
            "Content-Type"      : "text/javascript",        # requerido por IE
            "Content-Encoding"  : "gzip",
            "Cache-Control"     : "max-age=3600"
        },
        "target.path"   : "/comments/catalogo/cds/rp_internacional--1.js",
        "target.repo"   : "static"
    },

    ########## /catalogo/cds/rp_internacional--1 More
    {
        "EntityType"    : "SUBJ",
        "EntityId"      : 1,
        "dataset"       : "subjectComments",    "_data" : sample.sample_data_music_4_1.music_4_1_data,
                                                "_url"  : librosURL,
        "template"      : "subject/catalog.js",
        "headers"       : {
            "Content-Type"      : "text/javascript",
            "Content-Encoding"  : "gzip",
            "Cache-Control"     : "max-age=3600"
        },
        "target.path"   : "/catalog/catalogo/cds/rp_internacional--1.js",
        "target.repo"   : "static"
    },

    ########## /peliculas/index.html
    {
        "EntityType"    : "SUBJ",
        "EntityId"      : 1,
        "dataset"       : "subjectMain",        "_data" : sample.sample_data_movies_5.movies_5_main,
                                                "_url"  : peliculasURL,
        "template"      : "subject/index.html",
        "headers"       : {
            "Content-Type"      : "text/html",
            "Content-Encoding"  : "gzip",
            "Cache-Control"     : "max-age=3600"
        },
        "target.path"   : "/peliculas/index.html",
        "target.repo"   : "dynamic"
    },

    {
        "EntityType"    : "SUBJ",
        "EntityId"      : 1,
        "dataset"       : "subjectMain",        "_data" : sample.sample_data_games_3.games_3_main,
                                                "_url"  : pasatiemposURL,
        "template"      : "subject/index.html",
        "headers"       : {
            "Content-Type"      : "text/html",
            "Content-Encoding"  : "gzip",
            "Cache-Control"     : "max-age=3600"
        },
        "target.path"   : "/juguetes/index.html",
        "target.repo"   : "dynamic"
    },

 # home - exchange
   #
   {
       "EntityType"    : "PAGE",
       "EntityId"      : 1,
       "dataset"       : "homeExchange",       "_data" : sample.sample_data.homePriceData,
                                               "_url"  : homeURL,
       "template"      : "home/exchange.js",
       "headers"       : {
           "Content-Type"      : "text/javascript",        # requerido por IE
           "Content-Encoding"  : "gzip",
           "Cache-Control"     : "max-age=3600"
       },
       "target.path"   : "/home-exchange.js",
       "target.repo"   : "static"
   },
    #
   # product - comentarios
   #
   {
       "EntityType"    : "PAGE",
       "EntityId"      : 1,
       "dataset"       : "productComments",       "_data" : sample.sample_product_book_413418.products_413418_comments,
                                               "_url"  : homeURL,
       "template"      : "product/comments.js",
       "headers"       : {
           "Content-Type"      : "text/javascript",        # requerido por IE
           "Content-Encoding"  : "gzip",
           "Cache-Control"     : "max-age=3600"
       },
       "target.path"   : "/comments/libros/ciencias_de_la_salud__naturales_y_divulgacion_cientifica--7/divulgacion_cientifica--1/en_general--1/matematica___estas_ahi_sobre_numeros__personajes__problemas_y_curiosidades--413418.js",
       "target.repo"   : "static"
   },
   #
   # product - related
   #
   {
       "EntityType"    : "PAGE",
       "EntityId"      : 1,
       "dataset"       : "productRelated",       "_data" : sample.sample_product_book_413418.products_413418_related,
                                               "_url"  : homeURL,
       "template"      : "product/related.js",
       "headers"       : {
           "Content-Type"      : "text/javascript",        # requerido por IE
           "Content-Encoding"  : "gzip",
           "Cache-Control"     : "max-age=3600"
       },
       "target.path"   : "/related/libros/ciencias_de_la_salud__naturales_y_divulgacion_cientifica--7/divulgacion_cientifica--1/en_general--1/matematica___estas_ahi_sobre_numeros__personajes__problemas_y_curiosidades--413418.js",
       "target.repo"   : "static"
   },
   #
   # product - price
   #
   {
       "EntityType"    : "PAGE",
       "EntityId"      : 1,
       "dataset"       : "productPrice",       "_data" : sample.sample_product_book_413418.products_413418_price,
                                               "_url"  : homeURL,
       "template"      : "product/price.js",
       "headers"       : {
           "Content-Type"      : "text/javascript",        # requerido por IE
           "Content-Encoding"  : "gzip",
           "Cache-Control"     : "max-age=3600"
       },
       "target.path"   : "/price/libros/ciencias_de_la_salud__naturales_y_divulgacion_cientifica--7/divulgacion_cientifica--1/en_general--1/matematica___estas_ahi_sobre_numeros__personajes__problemas_y_curiosidades--413418.js",
       "target.repo"   : "static"
   },
########## /index.html
   {
       "EntityType"    : "PAGE",
       "EntityId"      : 1,
       "dataset"       : "main",          "_data" : sample.sample_product_book_413418.products_413418_main,
                                              "_url"  : homeURL,
        "_url"          : dict(librosURL, **{'cannonical': "/libros/ciencias_de_la_salud__naturales_y_divulgacion_cientifica--7/divulgacion_cientifica--1/en_general--1/matematica___estas_ahi_sobre_numeros__personajes__problemas_y_curiosidades--413418" }),
       "template"      : "product/index.html",
       "headers"       : {
           "Content-Type"      : "text/html",
           "Content-Encoding"  : "gzip",
           "Cache-Control"     : "max-age=3600"
       },
       "target.path"   : "/libros/ciencias_de_la_salud__naturales_y_divulgacion_cientifica--7/divulgacion_cientifica--1/en_general--1/matematica___estas_ahi_sobre_numeros__personajes__problemas_y_curiosidades--413418.htm",
       "target.repo"   : "dynamic"
   },
########## prouct page
   {
       "EntityType"    : "PAGE",
       "EntityId"      : 1,
       "dataset"       : "main",          "_data" : sample.sample_product_book_465771.products_465771_main,
                                              "_url"  : homeURL,
        "_url"          : dict(librosURL, **{'cannonical': "/libros/ficcion_y_literatura--1/novelas--1/general--1/comer__rezar__amar--465771"}),
       "template"      : "product/index.html",
       "headers"       : {
           "Content-Type"      : "text/html",
           "Content-Encoding"  : "gzip",
           "Cache-Control"     : "max-age=3600"
       },
       "target.path"   : "/libros/ficcion_y_literatura--1/novelas--1/general--1/comer__rezar__amar--465771.htm",
       "target.repo"   : "dynamic"
   },
              #
   # product music - comentarios
   #
   {
       "EntityType"    : "PAGE",
       "EntityId"      : 1,
       "dataset"       : "productComments",       "_data" : sample.sample_product_music_530185.products_530185_comments,
                                               "_url"  : homeURL,
       "template"      : "product/comments.js",
       "headers"       : {
           "Content-Type"      : "text/javascript",        # requerido por IE
           "Content-Encoding"  : "gzip",
           "Cache-Control"     : "max-age=3600"
       },
       "target.path"   : "/comments/cds/rp_internacional--1/rp_internacional--1/true_sacd--530185.js",
       "target.repo"   : "static"
   },
   #
   # product - related
   #
   {
       "EntityType"    : "PAGE",
       "EntityId"      : 1,
       "dataset"       : "productRelated",       "_data" : sample.sample_product_music_530185.products_530185_related,
                                               "_url"  : homeURL,
       "template"      : "product/related.js",
       "headers"       : {
           "Content-Type"      : "text/javascript",        # requerido por IE
           "Content-Encoding"  : "gzip",
           "Cache-Control"     : "max-age=3600"
       },
       "target.path"   : "/related/cds/rp_internacional--1/rp_internacional--1/true_sacd--530185.js",
       "target.repo"   : "static"
   },
   #
   # product - price
   #
   {
       "EntityType"    : "PAGE",
       "EntityId"      : 1,
       "dataset"       : "productPrice",       "_data" : sample.sample_product_music_530185.products_530185_price,
                                               "_url"  : homeURL,
       "template"      : "product/price.js",
       "headers"       : {
           "Content-Type"      : "text/javascript",        # requerido por IE
           "Content-Encoding"  : "gzip",
           "Cache-Control"     : "max-age=3600"
       },
       "target.path"   : "/price/cds/rp_internacional--1/rp_internacional--1/true_sacd--530185.js",
       "target.repo"   : "static"
   },
########## /index.html
   {
       "EntityType"    : "PAGE",
       "EntityId"      : 1,
       "dataset"       : "main",          "_data" : sample.sample_product_music_530185.products_530185_main,
                                              "_url"  : homeURL,
        "_url"          : dict(musicaURL, **{'cannonical': "/libros/ficcion_y_literatura--1/novelas--1/general--1/comer__rezar__amar--465771"}),
       "template"      : "product/index.html",
       "headers"       : {
           "Content-Type"      : "text/html",
           "Content-Encoding"  : "gzip",
           "Cache-Control"     : "max-age=3600"
       },
       "target.path"   : "/cds/rp_internacional--1/rp_internacional--1/true_sacd--530185.htm",
       "target.repo"   : "dynamic"
   },
    #
    # product movies - comentarios
    #
   {
       "EntityType"    : "PAGE",
       "EntityId"      : 1,
       "dataset"       : "productComments",       "_data" : sample.sample_product_movie_529368.products_529368_comments,
                                               "_url"  : homeURL,
       "template"      : "product/comments.js",
       "headers"       : {
           "Content-Type"      : "text/javascript",        # requerido por IE
           "Content-Encoding"  : "gzip",
           "Cache-Control"     : "max-age=3600"
       },
       "target.path"   : "/comments/dvds/serie_tv--15/millennium_3_la_reina_en_el_palacio_de_las_corrientes_de_aire--529368.js",
       "target.repo"   : "static"
   },
   #
   # product - related
   #
   {
       "EntityType"    : "PAGE",
       "EntityId"      : 1,
       "dataset"       : "productRelated",       "_data" : sample.sample_product_movie_529368.products_529368_related,
                                               "_url"  : homeURL,
       "template"      : "product/related.js",
       "headers"       : {
           "Content-Type"      : "text/javascript",        # requerido por IE
           "Content-Encoding"  : "gzip",
           "Cache-Control"     : "max-age=3600"
       },
       "target.path"   : "/related/dvds/serie_tv--15/millennium_3_la_reina_en_el_palacio_de_las_corrientes_de_aire--529368.js",
       "target.repo"   : "static"
   },
   #
   # product - price
   #
   {
       "EntityType"    : "PAGE",
       "EntityId"      : 1,
       "dataset"       : "productPrice",       "_data" : sample.sample_product_movie_529368.products_529368_price,
                                               "_url"  : homeURL,
       "template"      : "product/price.js",
       "headers"       : {
           "Content-Type"      : "text/javascript",        # requerido por IE
           "Content-Encoding"  : "gzip",
           "Cache-Control"     : "max-age=3600"
       },
       "target.path"   : "/price/dvds/serie_tv--15/millennium_3_la_reina_en_el_palacio_de_las_corrientes_de_aire--529368.js",
       "target.repo"   : "static"
   },
########## /index.html
   {
       "EntityType"    : "PAGE",
       "EntityId"      : 1,
       "dataset"       : "main",          "_data" : sample.sample_product_movie_529368.products_529368_main,
                                              "_url"  : homeURL,
        "_url"          : dict(musicaURL, **{'cannonical': "/libros/ficcion_y_literatura--1/novelas--1/general--1/comer__rezar__amar--465771"}),
       "template"      : "product/index.html",
       "headers"       : {
           "Content-Type"      : "text/html",
           "Content-Encoding"  : "gzip",
           "Cache-Control"     : "max-age=3600"
       },
       "target.path"   : "/dvds/serie_tv--15/millennium_3_la_reina_en_el_palacio_de_las_corrientes_de_aire--529368.htm",
       "target.repo"   : "dynamic"
   }
   
]


def templating(template, data, urls, targetPath):
    """Generates the a document

    Parameters:
    template --- the template to use (it must be loaded)
    data --- the data that the template requires
    urls --- the urls that apply to the document
    targetPath --- the target path of the document, it can
                   be one of the urls in urls["urls"]
    """

    result = "TARGET [%s]\nTEMPLATE [%s]\n" \
             "DATA--------\n%s\nURLS--------\n%s\n" % \
             (targetPath, template, data, urls)

    return result


def save(document, headers, targetRepo, targetPath):
    """Saves a document

    Parameters:
    document --- the document contents
    headers --- the document headers
    targetRepo --- the repository name
    targetPath --- the target path of the document
    """

    ########### DO SOMETHING USEFUL HERE!!!

    return True

#print "------------------------"
#print "Por generar %d documentos" % len(documentos)
#for i in range(len(documentos)):
#
#    # obtenemos los datos
#    entityType  = documentos[i]["EntityType"]
#    entityId    = documentos[i]["EntityId"]
#    data        = documentos[i]["_data"]
#    url         = documentos[i]["_url"]
#    template    = documentos[i]["template"]
#    headers     = documentos[i]["headers"]
#    targetPath  = documentos[i]["target.path"]
#    targetRepo  = documentos[i]["target.repo"]
#
#    print "- generando para %s/%d target %s@%s" % \
#          (entityType, entityId, targetRepo, targetPath),   # no new line
#
#    # generate document from template
#    document = templating(template, data, url, targetPath)
#
#    # save document to file
#    saved = save(document, headers, targetRepo, targetPath)
#    print "%s" % ("OK" if saved else "ERR")

class Storage_Cache(object):
    '''Cache of bucket objects'''
    def __init__(self, type='folder'):
        self._save = {}
        if type == 'folder':
            self._st = FilesystemStorage
        elif type == 's3':
            self._st = S3Storage
        else:
            sys.exit(2)

    def __call__(self, name):
        '''Get a bucket object from cache or create a new one'''
        if not self._save.has_key(name):
            self._save[name] = self._st(name)
        return self._save[name]


if __name__ == '__main__':

    env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

    script_tag   = False     # No script tag by default
    storage_type = 'folder'  # Default to folder output
    target = None

    try:
        opts, args = getopt.getopt(sys.argv[1:], 's:jt:',
                ['storage=', 'jshack', 'target='])
    except getopt.GetoptError, e:
        print e
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-j', '--jshack'):
            script_tag = True
        elif opt in ('-s', '--storage'):
            if arg not in ('s3', 'folder'):
                print 'invalid storage ', arg
                sys.exit(2)
            storage_type = arg
        elif opt in ('-t', '--target'):
            target = arg
        else:
            print 'usage:\n', sys.argv[0], ' -s <s3, folder>'
            sys.exit(2)

    storage_cache = Storage_Cache(storage_type)

    for d in documentos:

        if target and d['target.path'] != target:
            continue  # skip targets not solicited

        print "Generating: ", storage_type, d['target.path'], " for ", \
            d['target.repo'], storage[storage_type][d['target.repo']]

        # Get corresponding bucket from storage connection cache
        s = storage_cache(storage[storage_type][d['target.repo']])

        t = env.get_template(d['template'])
        t_params = { 'd': d['_data'], 'url': d['_url'].copy() }

        if script_tag:
            # trick HTML to load from same source as remote script
            t_params['url']['gen_script'] = t_params['url']['data']

        page_html = t.render(t_params).encode('utf-8')
        target_path = d['target.path']
        headers = d['headers'].copy()
        content_type = headers['Content-Type']

        if script_tag:

            # No cache this trick (helps with development, no refresh)
            headers['Cache-Control'] = "no-cache"

            if content_type == 'text/html':
                # Convert to script tag replacing document.body
                target_path = target_path.replace('.html', '_html.js')
                target_path = target_path.replace('.htm', '_htm.js')
                headers['Content-Type'] = 'text/javascript'
                page_html = JS_WRAP % js_dump(page_html)

        s.send(target_path, page_html, headers)

        #break # XXX

