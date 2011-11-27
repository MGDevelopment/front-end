"""This file has functions for post processing on Subjects (categories)

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
#
# THE URL SCHEME IS NON-OBVIOUS
#
# Libros:
#
#    home:       /libros/
#    tree:       /catalogo/libros/...
#    product:    /libros/...
#
# Games:
#
#    home:       /juguetes/
#    tree:       /catalogo/pasatiempos/...
#    product:    /pasatiempos/...
#
# Music:
#
#    home:       /musica/
#    tree:       /catalogo/cds/...
#    product:    /cds/...
#
# Movies:
#
#    home:       /peliculas/
#    tree:       /catalogo/dvds/...
#    product:    /dvds/...

_urlBases = {
    "Seccion"    : { 1: "libros/",          3: "juguetes/",
                     4: "musica/",          5: "peliculas/" },
    "Grupo"      : { 1: "catalogo/libros/", 3: "catalogo/pasatiempos/",
                     4: "catalogo/cds/",    5: "catalogo/dvds/" },
    "Familia"    : { 1: "catalogo/libros/", 3: "catalogo/pasatiempos/",
                     4: "catalogo/cds/",    5: "catalogo/dvds/" },
    "Subfamilia" : { 1: "catalogo/libros/", 3: "catalogo/pasatiempos/",
                     4: "catalogo/cds/",    5: "catalogo/dvds/" }
}

def calcURL(row):

    # find the nodes
    subtype    = row["Subtype"]
    seccion    = tmkTree.findNode(row["Categoria_Seccion"], -1,
                                  -1, -1)
    grupo      = tmkTree.findNode(row["Categoria_Seccion"], row["Categoria_Grupo"],
                                  -1, -1)
    familia    = tmkTree.findNode(row["Categoria_Seccion"], row["Categoria_Grupo"],
                                  row["Categoria_Familia"], -1)
    subfamilia = tmkTree.findNode(row["Categoria_Seccion"], row["Categoria_Grupo"],
                                  row["Categoria_Familia"], row["Categoria_Subfamilia"])

    # prepare an empty URL
    url = "/"

    # FIRST PART - seccion or /catalogo/seccion - all cases
    if subtype in [ "Seccion", "Grupo", "Familia", "Subfamilia" ]:
        if subtype in _urlBases and seccion["id"] in _urlBases[subtype]:
            url += _urlBases[subtype][seccion["id"]]
        else:
            if subtype == "Seccion":
                url += tmkSupport.noDiacritics(seccion["Nombre"]) + "/"
            else:
                url += "catalogo/" + tmkSupport.noDiacritics(seccion["Nombre"]) + "/"

    # SECOND PART - seccion (group and bellow)
    if subtype in [ "Grupo", "Familia", "Subfamilia" ]:
        url += tmkSupport.alphaOnly(
                    tmkSupport.noDiacritics(
                        tmkSupport.capitalize(
                            grupo["Nombre"]))).lower() + \
               "--" + str(grupo["id"]) + "/"

    # THIRD PART - seccion (family and bellow)
    if subtype in [ "Familia", "Subfamilia" ]:
        url += tmkSupport.alphaOnly(
                    tmkSupport.noDiacritics(
                        tmkSupport.capitalize(
                            familia["Nombre"]))).lower() + \
               "--" + str(familia["id"]) + "/"

    # FOURT PART - seccion (subfamily and bellow)
    if subtype in [ "Subfamilia" ]:
        url += tmkSupport.alphaOnly(
                    tmkSupport.noDiacritics(
                        tmkSupport.capitalize(
                            subfamilia["Nombre"]))).lower() + \
               "--" + str(subfamilia["id"]) + "/"

    # FILE EXTENSION (ONLY IF NOT "Seccion")
    if subtype in [ "Grupo", "Familia", "Subfamilia" ]:
        # remove the trailing "/" (if present)
        if url[-1] == "/":
            url = url[:-1]
        
        # append the file extension
        #####url += ".htm"

    # set the url
    row["LinkBase"] = url

    return row
