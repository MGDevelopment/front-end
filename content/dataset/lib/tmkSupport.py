
"""Support methods for TMK first implementation

by Jose Luis Campanello
"""

import types
import string
import unicodedata

########################################################

def decode(value, encoding = None):
    """If a string type and there's an encoding other than UTF-8, convert"""

    # need enconding and a string type
    if encoding is None:
        return value

    # only for strings (non-unicode)
    if isinstance(value, types.StringType):
        if encoding != "UTF-8" and encoding != "utf-8":
            return value.decode(encoding).encode('utf8')

    return value

########################################################


def noDiacritics(s):
    """Removes any diacritics"""

    str = unicode(s, 'utf-8')
    ret = unicodedata.normalize('NFKD', str)
    ret = ret.encode('ascii', 'ignore')

    return ret

########################################################


def alphaOnly(s):
    """Removes any character that is not a letter or digit"""

    # strip non digits, non letters (upper or lower) and non ",", "-", "." or space AS "_"
    s = s.translate(string.maketrans(",-. ", "____"))
    s = "".join(i for i in s if i in \
                ("0123456789" + \
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + \
                "abcdefghijklmnopqrstuvwxyz" + \
                "_"))

    return s

########################################################

def capitalize(s):

    ######### FROM method corregir

    # trim, uppercase and do some replacements
    s = s.strip().upper().replace("\\.", " .",  1). \
                          replace(",",   " , ", 1). \
                          replace(";",   " ; ", 1). \
                          replace("-",   " - ", 1). \
                          replace("/",   " / ", 1). \
                          replace("  ",  " ")

    # swap articulos (ej: "inmortales, los" => "los inmortales")
    s = swapArticulos(s, capitalize.rList, True)

    ######### FROM call to method capitalizarOriginal
    s = s.title()

    ######### FROM call to method minisculizar
    s = minusculizar(s)

    ######### FROM call to method mayusculizar
    s = mayusculizar(s)

    # some replacements and trim
    s = s.replace(" \\.", ".", 1). \
          replace(" ,",   ",", 1). \
          replace(" ;",   ";", 1). \
          strip()

    return s
capitalize.rList = [   \
    (", EL ",  "EL "),  \
    (", LA ",  "LA "),  \
    (", LO ",  "LO "),  \
    (", LOS ", "LOS "), \
    (", LAS ", "LAS "), \
    (", THE ", "THE "), \
    (", LES ", "LES ")  \
]

########################################################

def swapArticulos(s, rList, fullReplacement = True):

    # append a space
    s += " "

    # iterate (if needed)
    lastSpot = 0
    while fullReplacement and (lastSpot < len(s)):

        # find the place where the swap is to happen
        spot = s.find(".", lastSpot)
        if spot < 0:
            spot = s.find("-", lastSpot)
            if spot < 0:
                if s.find(" Y ", lastSpot) >= 0:
                    spot = s.find(" Y ", lastSpot) + 1
                else:
                    spot = -1
                if spot < 0:
                    spot = len(s)

        # replace
        for r in rList:
            if s[spot - len(r[0]):spot] == r[0]:
                if lastSpot == 0:
                    # move to the begining
                    s = r[1] + s[:spot - len(r[0])] + s[spot:]
                else:
                    # move to the begining of lastSpot
                    s = s[:lastSpot - 1] + r[1] + s[lastSpot - 1:spot - len(r[0])]
                break

        # go from this spot
        lastSpot = spot + 1

    return s

########################################################

def mayusculizar(s):
    """Convert some words to upper case"""
    
    # iterate over the words to capitalize
    for word in mayusculizar.words:
        if word in s:
            s = s.replace(word, word.upper())

    return s
mayusculizar.words = [                              \
    " Cd ", " Dvd ", " Egb ", " Mtv ", " Ntsc ",    \
    " Pal ", " Palm ", " Vhs ",                     \
    #roman numbers
    " Ii ", " Iii ", " Iv ", " Vi ", " Vii ",       \
    " Viii ", " Ix ", " Xi ", " Xii ", " Xiii ",    \
    " Xiv", " Xv "                                  \
]

########################################################

def minusculizar(s):
    """Convert some words to lower case
    
    NOTE: it does not work very well. If the word is at the
          begining is not replaced (even if it appears further
          ahead)
    """

    for word in minusculizar.words:
        pos = s.find(word)
        if pos > 0:             # only if not at the begining
            if not s[pos - 1] in "./:-#!#?{}()[]":      # previous not a termination
                if s[pos + len(word)] in " ./:-#!#?{}()[]":
                    s = s.replace(word, word.lower())

    return s
minusculizar.words = [ \
    "A", "B", "C", "E", "O", "Y", "Al", "Ante",         \
    "Aquel", "Como", "Con", "Contra", "Cualquier",      \
    "De", "Del", "Desde", "Dos", "El", "En",            \
    "Entre", "Es", "Esa", "Ese", "Esta", "Fue",         \
    "Hacia", "La", "Las", "Lo", "Los", "Me",            \
    "Mejor", "Menos", "Mi", "Ni", "No", "Para",         \
    "Por", "Que", "Se", "Ser", "Sin", "Sobre",          \
    "Sola", "Solo", "Son", "Soy", "Su", "Sus",          \
    "Te", "Tema", "Tiene", "Toda", "Todas", "Tres",     \
    "Tu", "Un", "Una", "Unas", "Uno", "Unos", "Va",     \
]