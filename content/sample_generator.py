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
import sample.sample_data_movies_5


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
    "cannonical"    : "/index.html",
    "urls"          : [ "/index.html", "/index.jsp" ],
    "static"        : "estatico.tematika.com",
    "dynamic"       : "www.tematika.com",
    "search"        : "buscador.tematika.com",
    "checkout"      : "seguro.tematika.com",
    "service"       : "servicios.tematika.com",
    "images"        : "http://img-tmk.tematika.com",
    "data"          : "http://beta1.testmatika.com.s3.amazonaws.com/"
}

librosURL = {
    "cannonical"    : "/libros",
    "urls"          : [ "/libros", "/libros/index.html", "/libros/index.jsp" ],
    "static"        : "estatico.tematika.com",
    "dynamic"       : "www.tematika.com",
    "search"        : "buscador.tematika.com",
    "checkout"      : "seguro.tematika.com",
    "service"       : "servicios.tematika.com",
    "images"        : "http://img-tmk.tematika.com",
    "data"          : "http://beta1.testmatika.com.s3.amazonaws.com/"
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
            "Cache-Control"     : "max-age=3600, must-revalidate"
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
            "Cache-Control"     : "max-age=3600, must-revalidate"
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
            "Cache-Control"     : "max-age=3600, must-revalidate"
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
            "Cache-Control"     : "max-age=3600, must-revalidate"
        },
        "target.path"   : "/home-comments.js",
        "target.repo"   : "static"
    },
    #
    # JS app
    #
    {
        "EntityType"    : "PAGE",
        "EntityId"      : 1,
        "dataset"       : "homeComments",       "_data" : {},
                                                "_url"  : homeURL,
        "template"      : "js/app.js",
        "headers"       : {
            "Content-Type"      : "text/javascript",
            "Content-Encoding"  : "gzip",
            "Cache-Control"     : "max-age=3600, must-revalidate"
        },
        "target.path"   : "/js/app.js",
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
#            "Cache-Control"     : "max-age=3600, must-revalidate"
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
            "Cache-Control"     : "max-age=3600, must-revalidate"
        },
        "target.path"   : "/libros/index.html",
        "target.repo"   : "dynamic"
    },
    ########## /libros/index.jsp
    {
        "EntityType"    : "SUBJ",
        "EntityId"      : 1,
        "dataset"       : "subjectMain",        "_data" : sample.sample_data_books_1.books_1_main,
                                                "_url"  : librosURL,
        "template"      : "subject/index.html",
        "headers"       : {
            "Content-Type"      : "text/html",
            "Content-Encoding"  : "gzip",
            "Cache-Control"     : "max-age=3600, must-revalidate"
        },
        "target.path"   : "/libros/index.jsp",
        "target.repo"   : "dynamic"
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
            "Cache-Control"     : "max-age=3600, must-revalidate"
        },
        "target.path"   : "/libros/showcase.js",
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
            "Cache-Control"     : "max-age=3600, must-revalidate"
        },
        "target.path"   : "/libros/comments.js",
        "target.repo"   : "static"
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

    try:
        opts, args = getopt.getopt(sys.argv[1:], 's:j', ['storage=', 'jshack'])
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
        else:
            print 'usage:\n', sys.argv[0], ' -s <s3, folder>'
            sys.exit(2)

    storage_cache = Storage_Cache(storage_type)

    for d in documentos:

        print "Generating: ", storage_type, d['target.path'], " for ", \
            d['target.repo'], storage[storage_type][d['target.repo']]

        # Get corresponding bucket from storage connection cache
        s = storage_cache(storage[storage_type][d['target.repo']])

        t = env.get_template(d['template'])
        t_params = { 'd': d['_data'], 'url': d['_url'] }

        page_html = t.render(t_params).encode('utf-8')
        target_path = d['target.path']
        headers = d['headers'].copy()
        content_type = headers['Content-Type']

        if script_tag:
            headers['Cache-Control'] = "no-cache, must-revalidate"
            if content_type == 'text/html':
                # Convert to script tag replacing document.body
                target_path = target_path.replace('.html', '_html.js')
                headers['Content-Type'] = 'text/javascript'
                page_html = JS_WRAP % js_dump(page_html)

        s.send(target_path, page_html, headers)

        #break # XXX

