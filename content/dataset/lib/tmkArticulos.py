"""This file has functions for post processing on Articulos


by Jose Luis Campanello
"""

import os.path

import ecommerce.config

import tmkSupport
import tmkTree

########################################################

def fixTitle(row):
    """Capitalize the title"""

    # capitalize the title
    if "Title" in row:
        row["Title"] = tmkSupport.capitalize(row["Title"])

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
    row["SmallCover"] = None
    row["SmallCoverGeneric"] = True
    for i in range(len(small)):
        path = checkImageFile(basePath, small[i], variables)
        if path is not None:
            row["SmallCover"] = path
            row["SmallCoverGeneric"] = False
            break
    # still no image? => check for a default
    if row["SmallCover"] is None and smallDef is not None:
        path = checkImageFile(basePath, smallDef, variables)
        if path is not None:
            row["SmallCover"] = path
            row["SmallCoverGeneric"] = True

    # try to find the large image
    row["LargeCover"] = None
    for i in range(len(large)):
        path = checkImageFile(basePath, large[i], variables)
        if path is not None:
            row["LargeCover"] = path
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
           "--" + str(row["EntityId"]) + ".htm"

    # set the url
    row["LinkBase"] = url

    return row

#####URL ========================
#####5) titulo segun:
#####
#####    soloLetrasYNumeros(sinTildesNiEnie(corregir({{description}}, true)).lowecase())
#####
#####6) "-- {{id_articulo}}.htm"
