"""The sitemap generation code

by Jose Luis Campanello
"""

#
# enumerate the sitemaps to generate
#
_def = [
    ######################################################
    #
    # catalog_book_new
    {
        "name"          : "catalog_book_new",
        "filename"      : "tematika_catalog_book_new",
        "frequency"     : "daily",
        "priority"      : "0.8",
        "query"         : """
        """
    },
    # catalog_book
    {
        "name"          : "catalog_book",
        "filename"      : "tematika_catalog_book",
        "frequency"     : "weekly",
        "priority"      : "0.5",
        "query"         : """
        """
    },
    ######################################################
    #
    # catalog_music_new
    {
        "name"          : "catalog_music_new",
        "filename"      : "tematika_catalog_music_new",
        "frequency"     : "daily",
        "priority"      : "0.8",
        "query"         : """
        """
    },
    # catalog_music
    {
        "name"          : "catalog_music",
        "filename"      : "tematika_catalog_music",
        "frequency"     : "weekly",
        "priority"      : "0.5",
        "query"         : """
        """
    },
    ######################################################
    #
    # catalog_movie_new
    {
        "name"          : "catalog_movie_new",
        "filename"      : "tematika_catalog_movie_new",
        "frequency"     : "daily",
        "priority"      : "0.8",
        "query"         : """
        """
    },
    # catalog_movie
    {
        "name"          : "catalog_movie",
        "filename"      : "tematika_catalog_movie",
        "frequency"     : "weekly",
        "priority"      : "0.5",
        "query"         : """
        """
    },
    ######################################################
    #
    # catalog_game_new
    {
        "name"          : "catalog_game_new",
        "filename"      : "tematika_catalog_game_new",
        "frequency"     : "daily",
        "priority"      : "0.8",
        "query"         : """
        """
    },
    # catalog_game
    {
        "name"          : "catalog_game",
        "filename"      : "tematika_catalog_game",
        "frequency"     : "weekly",
        "priority"      : "0.5",
        "query"         : """
        """
    },
    ######################################################
    #
    # subject_book
    {
        "name"          : "subject_book",
        "filename"      : "tematika_subject_book",
        "frequency"     : "daily",
        "priority"      : "0.8",
        "query"         : """
        """
    },
    ######################################################
    #
    # subject_music
    {
        "name"          : "subject_music",
        "filename"      : "tematika_subject_music",
        "frequency"     : "daily",
        "priority"      : "0.8",
        "query"         : """
        """
    },
    ######################################################
    #
    # subject_movie
    {
        "name"          : "subject_movie",
        "filename"      : "tematika_subject_movie",
        "frequency"     : "daily",
        "priority"      : "0.8",
        "query"         : """
        """
    },
    ######################################################
    #
    # subject_game
    {
        "name"          : "subject_game",
        "filename"      : "tematika_subject_game",
        "frequency"     : "daily",
        "priority"      : "0.8",
        "query"         : """
        """
    },
    ######################################################
    #
    # misc (home page, sucursales, etc)
    {
        "name"          : "misc",
        "filename"      : "tematika_misc",
        "frequency"     : "daily",
        "priority"      : "0.8"
        # no query => file is manualy maintained!!!!
    }
]

############################################
#
# generate
#
def generate():
    """Generate the sitemaps"""


    return 0



