"""This file has functions for post processing on Articulos

by Jose Luis Campanello
"""

import os.path
import urllib

import ecommerce.config

import tmkSupport
import tmkTree

########################################################

def fixTitle(row):
    """Capitalize the title"""

    # capitalize the title
    if "Title" in row:
        row["Title"] = tmkSupport.capitalize(row["Title"])
    else:
        row["Title"] = None

    return row

########################################################

def checkImageFile(base, template, variables):
    """Try to find an image file that responds to macro expansion"""

    # try expanding each variable
    for v in variables:
        template = template.replace("{{" + v + "}}", str(variables[v]))

    # join the file names
    fname = os.path.join(base, template)

    # return the file only if check if the file exists and is not empty
    return ("/" + template) if os.path.isfile(fname) and os.path.getsize(fname) > 0 else None


def calcImages(row):
    """Figure out if an Article has images and what the paths are

    Requires attributes:
    EntityId - the Product Id (same as Id_Articulo, PK on Articulos)
    Categoria_Seccion - from Articulos

    Up to four attributes are appended:
    SmallCover - the path to the small cover
    SmallCoverGeneric - a boolean indicating that the SmallCover is a generic
    LargeCover - if exists, the path to the large cover
    """

    # get some config values (be sure to make copies)
    config   = ecommerce.config.getConfig()
    basePath = config.get("paths.resources")
    small    = config.get("paths.cover.small", [ ])[:] # shallow copy
    smallDef = config.get("paths.cover.small-def")
    large    = config.get("paths.cover.large", [ ])[:] # shallow copy

    # figure out the variables we want to pass
    variables = {
        "EntityId"              : row.get("EntityId"),
        "Categoria_Seccion"     : row.get("Categoria_Seccion")
    }

    # try to find the small image
    row["CoverSmall"] = None
    row["CoverSmallGeneric"] = True
    for i in range(len(small)):
        path = checkImageFile(basePath, small[i], variables)
        if path is not None:
            row["CoverSmall"] = path
            row["CoverSmallGeneric"] = False
            break
    # still no image? => check for a default
    if row["CoverSmall"] is None and smallDef is not None:
        path = checkImageFile(basePath, smallDef, variables)
        if path is not None:
            row["CoverSmall"] = path
            row["CoverSmallGeneric"] = True

    # try to find the large image
    row["CoverLarge"] = None
    for i in range(len(large)):
        path = checkImageFile(basePath, large[i], variables)
        if path is not None:
            row["CoverLarge"] = path
            break

    return row

########################################################

def calcURL(row):

    # find the nodes
    seccion    = tmkTree.findNode(row["Categoria_Seccion"], -1,
                                  -1, -1)
    grupo      = tmkTree.findNode(row["Categoria_Seccion"], row["Categoria_Grupo"],
                                  -1, -1)
    familia    = tmkTree.findNode(row["Categoria_Seccion"], row["Categoria_Grupo"],
                                  row["Categoria_Familia"], -1)
    subfamilia = tmkTree.findNode(row["Categoria_Seccion"], row["Categoria_Grupo"],
                                  row["Categoria_Familia"], row["Categoria_Subfamilia"])

    # FIRST PART - seccion
    url = "/"
    if seccion["id"] == 1:
        url += "libros/"
    elif seccion["id"] == 3:
        url += "pasatiempos/"
    elif seccion["id"] == 4:
        url += "cds/"
    elif seccion["id"] == 5:
        url += "dvds/"
    else:
        url += tmkSupport.noDiacritics(seccion["Nombre"]) + "/"

    # SECOND PART - grupo (if any)
    if grupo is not None and grupo["id"] != 0:
        url += tmkSupport.alphaOnly(
                    tmkSupport.noDiacritics(
                        tmkSupport.capitalize(
                            grupo["Nombre"]))).lower() + \
               "--" + str(grupo["id"]) + "/"

    # THIRD PART - familia (if any)
    if familia is not None and familia["id"] != 0:
        url += tmkSupport.alphaOnly(
                    tmkSupport.noDiacritics(
                        tmkSupport.capitalize(
                            familia["Nombre"]))).lower() + \
               "--" + str(familia["id"]) + "/"

    # FOURTH PART - subfamilia (if any)
    if subfamilia is not None and subfamilia["id"] != 0:
        url += tmkSupport.alphaOnly(
                    tmkSupport.noDiacritics(
                        tmkSupport.capitalize(
                            subfamilia["Nombre"]))).lower() + \
               "--" + str(subfamilia["id"]) + "/"

    # FIFTH PART - title
    url += tmkSupport.alphaOnly(
                tmkSupport.noDiacritics(
                    tmkSupport.capitalize(
                        row.get("Title")))).lower() + \
           "--" + str(row["EntityId"]) ##### + ".htm"

    # set the url
    row["LinkBase"] = url

    return row

########################################################

def embedRatings(row):
    """Makes Rating group as direct attributes"""

    # sanity check
    if "Ratings" not in row or row["Ratings"] is None:
        row["Ratings"] = { }

    # get the data item
    ratings = row["Ratings"]

    row["Rating"] = ratings.get("Rating")
    row["CommentCount"] = ratings.get("CommentCount")

    # pass the attributes up (do None for missing attrs)
    for attr in [ "CommentCount", "Rating" ]:
        row[attr] = ratings.get(attr)

    # remove the ratings from the row
    del row["Ratings"]

    return row

########################################################

def imprintTitle(row):
    """Reformats the Imprint title"""

    # sanity check
    if "ImprintName" not in row:
        return row

    # get the title
    title = row["ImprintName"]

    # if title is prefixed with "[MUS] ", remove
    if title.startswith("[MUS] "):
        title = title[6:]

    # capitalize
    title = tmkSupport.capitalize(title)

    # reset the title
    row["ImprintName"] = title

    return row

########################################################

def imprintCalcURL(row):
    """Creates the URL for the Imprint page"""

    # get some data
    seccionId   = str(row.get("Categoria_Seccion", 1))
    imprintId   = str(row.get("ImprintId", 0))
    imprintName = row.get("ImprintName", "")

    # encode the url params
    params = urllib.urlencode( {
        "seccion"           : seccionId,
        "idSeccion"         : seccionId,
        "criterioDeOrden"   : 2,
        "claveDeBusqueda"   : "porIDdeEditorial",
        "texto"             : imprintName,
        "idEditor"          : imprintId
    } )

    # build the url
    linkBase = "/buscador/productos.jsp?" + params

    # set the URL
    row["ImprintURL"] = linkBase

    return row

########################################################

def contributorTitle(row):
    """Reformats the Contributor title"""

    # sanity check
    if "ContributorName" not in row:
        return row

    # get the title
    title = row["ContributorName"]

    # if title is prefixed with "[MUS] ", remove
    if title.startswith("[MUS] "):
        title = title[6:]

    # capitalize
    title = tmkSupport.capitalize(title)

    # reset the title
    row["ContributorName"] = title

    return row

########################################################

def contributorCalcURL(row):
    """Creates the URL for the Contributor page"""

    # get some data
    seccionId       = str(row.get("Categoria_Seccion", 1))
    contributorId   = str(row.get("ContributorId", 0))
    contributorName = row.get("ContributorName", "")

    # encode the url params
    params = urllib.urlencode( {
        "seccion"           : seccionId,
        "idSeccion"         : seccionId,
        "criterioDeOrden"   : 2,
        "claveDeBusqueda"   : "porIDdeAutor",
        "texto"             : contributorName,
        "idEditor"          : contributorId
    } )

    # build the url
    linkBase = "/buscador/productos.jsp?" + params

    # set the URL
    row["ContributorURL"] = linkBase

    return row
