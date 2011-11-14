from   ecommerce.storage  import S3Storage
import jinja2
import sample_data

#
# Config
#
# What S3 bucket is target for what host.domain
bucket_domain = {
    "www.tematika.com":       "tmk-a",
    "estatico.tematika.com":  "estatico.testmatika.com",
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
    "service"       : "servicios.tematika.com"
}

librosURL = {
    "cannonical"    : "/libros",
    "urls"          : [ "/libros", "/libros/index.html", "/libros/index.jsp" ],
    "static"        : "estatico.tematika.com",
    "dynamic"       : "www.tematika.com",
    "search"        : "buscador.tematika.com",
    "checkout"      : "seguro.tematika.com",
    "service"       : "servicios.tematika.com"
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
        "dataset"       : "homeMain",          "_data" : sample_data.homeMainData,
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
        "dataset"       : "homeMain",          "_data" : sample_data.homeMainData,
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
        "dataset"       : "homeShowcase",       "_data" : sample_data.homeShowcaseData,
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
        "dataset"       : "homeComments",       "_data" : sample_data.homeCommentsData,
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
    #######################################################
    #
    # libros - html
    #
    ########## /libros
    {
        "EntityType"    : "SUBJ",
        "EntityId"      : 1,
        "dataset"       : "subjectMain",        "_data" : sample_data.librosMainData,
                                                "_url"  : librosURL,
        "template"      : "subject/index.html",
        "headers"       : {
            "Content-Type"      : "text/html",
            "Content-Encoding"  : "gzip",
            "Cache-Control"     : "max-age=3600, must-revalidate"
        },
        "target.path"   : "/libros",
        "target.repo"   : "dynamic"
    },
    ########## /libros/index.html
    {
        "EntityType"    : "SUBJ",
        "EntityId"      : 1,
        "dataset"       : "subjectMain",        "_data" : sample_data.librosMainData,
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
        "dataset"       : "subjectMain",        "_data" : sample_data.librosMainData,
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
        "dataset"       : "subjectShowcase",    "_data" : sample_data.librosShowcaseData,
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
        "dataset"       : "subjectComments",    "_data" : sample_data.librosCommentsData,
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
#
#print "----> DONE!"


if __name__ == '__main__':

    env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
    bucket_cache = {}

    for d in documentos:

#        entityType  = documentos[i]["EntityType"]
#        entityId    = documentos[i]["EntityId"]
#        data        = documentos[i]["_data"]
#        url         = documentos[i]["_url"]
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

        # d['headers']['Content-Encoding']
        # d['headers']['Cache-Control']
        bucket_name = bucket_domain[d['_url'][d['target.repo']]]
        s = S3Storage(bucket_name)  # Get corresponding bucket (XXX cache)

        t = env.get_template(d['template'])
        s.send(d['target.path'], t.render(d['_data']), d['headers'])
        #open('./' + d['target.path'], 'w').write(t.render(d['_data']))

        break # XXX

