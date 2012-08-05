"""Globaly defined variables
"""

import __builtin__          # we put a logger variable in here
import logging
import logging.config

import ecommerce.config

#########################################################
#########################################################
#
# some constants and handy functions
#
configPrefix    = "content"
generatorPrefix = "generator"
daemonPrefix    = "content"
tasksPrefix     = "tasks"
application     = configPrefix
queuePrefix     = configPrefix + ".queue"

entityTypes  = [ "PAGE", "PROD", "SUBJ" ]
subtypes     = {
    "PAGE"   : [ ],
    "PROD"   : [ ],
    "SUBJ"   : [ "Seccion", "Grupo", "Familia", "Subfamilia" ]
}
maxEntities  = 64       # do not generate more than this because of
                        # the oracle 9i buffer size bug (long sql
                        # sentences generate bogus results)

# the global logger
_logconf = None
_loggers = None    # will be a dictionary

def get_logger(app_prefix, log_prefix, config = None):

    global _loggers
    global _logconf

    # be sure to have a config
    if config is None:
        config = ecommerce.config.getConfig()

    # configure logging
    if _loggers is None:

        # set basic parameters
        logging.basicConfig(level = logging.DEBUG, datefmt = '%Y-%m-%d %H:%M:%S')

        # get logging config
        _logconf = config.getMulti(app_prefix, "logging")
        if _logconf is not None:

            # config the logging
            logging.config.dictConfig(_logconf) 

        _loggers = { }

    # create the logger if not already created
    logger = _loggers[log_prefix] if log_prefix in _loggers else None
    if logger is None:

        # get a logger
        if _logconf is not None:
            # get a logger
            logger = logging.getLogger(log_prefix)
        else:
            logger = logging.getLogger('')

        # save the logger
        _loggers[log_prefix] = logger

    return logger


def set_logger(app_prefix, log_prefix, config = None):

    # make globally accesible
    __builtin__.logger = get_logger(app_prefix, log_prefix, config)
