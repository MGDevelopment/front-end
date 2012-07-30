"""The documents definition

This file defines all the documents that can be generated and
how to generate them.

The information is structured as a dictionary of EntityType
(PROD, SUBJ, PAGE, CONT, IMPR, PUBL, etc). Each has type has
a list of documents.

A function is provided so that, given a tag (passed in in the
job) the list of relevant documents (for each type of entity)
is returned.

by Jose Luis Campanello
"""

############################################
#
# document definition
#

documents = {
    ##############################################
    ##############################################
    #
    # PAGE - page - home page
    #
    "PAGE"  : [
        ####################### main
        {
            "name"          : "homepage-main",
            "dataset"       : "homeMain",
            "template"      : "home/index.html",
            "headers"       : {
                "Content-Type"      : "text/html",
                "Content-Encoding"  : "gzip",
                "Cache-Control"     : "max-age=3600, must-revalidate"
            },
            "tags"          : [ "main" ],
            "target.path"   : [ "/index.htm", "/index.html" ],
            "target.repo"   : "jrunhome"
        },
        ####################### showcase
        {
            "name"          : "homepage-showcase",
            "dataset"       : "homeShowcase",
            "template"      : "home/showcase.js",
            "headers"       : {
                "Content-Type"      : "text/javascript",
                "Content-Encoding"  : "gzip",
                "Cache-Control"     : "max-age=3600, must-revalidate"
            },
            "tags"          : [ "main" ],
            "target.path"   : "/home-showcase.js",
            "target.repo"   : "jrunhome"
        },
        ####################### comments
        {
            "name"          : "homepage-comments",
            "dataset"       : "homeComments",
            "template"      : "home/comments.js",
            "headers"       : {
                "Content-Type"      : "text/javascript",
                "Content-Encoding"  : "gzip",
                "Cache-Control"     : "max-age=3600, must-revalidate"
            },
            "tags"          : [ "comment" ],
            "target.path"   : "/home-comments.js",
            "target.repo"   : "jrunhome"
        },
        ################### price.js
        {
            "name"          : "homepage-price",
            "dataset"       : "homePrice",
            "template"      : "home/exchange.js",
            "headers"       : {
                "Content-Type"      : "text/javascript",
                "Content-Encoding"  : "gzip",
                "Cache-Control"     : "max-age=3600, must-revalidate"
            },
            "tags"          : [ "price" ],
            "target.path"   : "/home-exchange.js",
            "target.repo"   : "jrunhome"
        }
    ],
    ##############################################
    ##############################################
    #
    # PROD - product - articulo
    #
    "PROD"  : [
        ####################### main
        {
            "name"          : "product-main",
            "dataset"       : "productMain",
            "template"      : "product/index.html",
            "headers"       : {
                "Content-Type"      : "text/html",
                "Content-Encoding"  : "gzip",
                "Cache-Control"     : "max-age=3600, must-revalidate"
            },
            "tags"          : [ "main" ],
            "target.path"   : [ "{{cannonical}}.htm" ],
            "target.repo"   : "dynamic"
        },
        ####################### related
        {
            "name"          : "product-related",
            "dataset"       : "productRelated",
            "template"      : "product/related.js",
            "headers"       : {
                "Content-Type"      : "text/javascript",
                "Content-Encoding"  : "gzip",
                "Cache-Control"     : "max-age=3600, must-revalidate"
            },
            "tags"          : [ "related" ],
            "target.path"   : "/related/{{cannonical}}.js",
            "target.repo"   : "static"
        },
        ####################### comments
        {
            "name"          : "product-comments",
            "dataset"       : "productComments",
            "template"      : "product/comments.js",
            "headers"       : {
                "Content-Type"      : "text/javascript",        # requerido por IE
                "Content-Encoding"  : "gzip",
                "Cache-Control"     : "max-age=3600, must-revalidate"
            },
            "tags"          : [ "comment" ],
            "target.path"   : "/comments/{{cannonical}}.js",
            "target.repo"   : "static"
        },
        ####################### price
        {
            "name"          : "product-price",
            "dataset"       : "productPrice",
            "template"      : "product/price.js",
            "headers"       : {
                "Content-Type"      : "text/javascript",        # requerido por IE
                "Content-Encoding"  : "gzip",
                "Cache-Control"     : "max-age=3600, must-revalidate"
            },
            "tags"          : [ "price" ],
            "target.path"   : "/price/{{cannonical}}.js",
            "target.repo"   : "static"
        }
    ],
    ##############################################
    ##############################################
    #
    # SUBJ - subject - categorias
    #
    "SUBJ"  : [
        ####################### main
        {
            "name"          : "subject-main",
            "dataset"       : "subjectMain",
            "template"      : "subject/index.html",
            "headers"       : {
                "Content-Type"      : "text/html",
                "Content-Encoding"  : "gzip",
                "Cache-Control"     : "max-age=3600, must-revalidate"
            },
            "tags"          : [ "main" ],
            "target.path"   : [ "{{cannonical}}/index.htm", "{{cannonical}}.htm" ],
            "target.repo"   : "dynamic"
        },

        ####################### catalog
        {
            "name"          : "subject-catalog",
            "dataset"       : "subjectData",
            "template"      : "subject/catalog.js",
            "headers"       : {
                "Content-Type"      : "text/javascript",
                "Content-Encoding"  : "gzip",
                "Cache-Control"     : "max-age=3600, must-revalidate"
            },
            "tags"          : [ "main" ],
            "target.path"   : "/catalog/{{cannonical}}.js",
            "target.repo"   : "static"
        },
        ####################### showcase
        {
            "name"          : "subject-showcase",
            "dataset"       : "subjectData",
            "template"      : "subject/showcase.js",
            "headers"       : {
                "Content-Type"      : "text/javascript",
                "Content-Encoding"  : "gzip",
                "Cache-Control"     : "max-age=3600, must-revalidate"
            },
            "tags"          : [ "main" ],
            "target.path"   : "/showcase/{{cannonical}}.js",
            "target.repo"   : "static"
        },
        ####################### comments
        {
            "name"          : "subject-comments",
            "dataset"       : "subjectComments",
            "template"      : "subject/comments.js",
            "headers"       : {
                "Content-Type"      : "text/javascript",        # requerido por IE
                "Content-Encoding"  : "gzip",
                "Cache-Control"     : "max-age=3600, must-revalidate"
            },
            "tags"          : [ "comment" ],
            "target.path"   : "/comments/{{cannonical}}.js",
            "target.repo"   : "static"
        }
    ]
}

############################################
#
# find relevant documents
#

def relevant(tag = None):
    """Find the defined documents that apply to the tag"""

    # some tag fixing
    if tag == "*" or tag == "all" or tag == "__all__":
        tag = None

    # prepare the result
    result = { }
    for type in documents:

        # build the list for the type
        doclist = [ d.copy() for d in documents[type]
                    if tag is None or tag in d["tags"] ]

        # append the list
        result[type] = doclist

    return result

