"""The content generation program

This program has two modes of operation:

1- daemon mode (single parameter with value "daemon")
2- generation mode (parameters)

DAEMON MODE
In this mode the process enters an infinite loop that tries to get
jobs from the queue and tries to execute those jobs. The loop is not
actualy infinite, as the process exits after a specified time
(content.daemon.maxrun). The goal of this is to give chance to the
system to create a new generator every now and then, but not too often.

GENERATION MODE
In this mode, the process interprets the command line arguments to do
one of the following things:
- print help (arguments: help or no arguments)
- list the queue (arguments: list)
- add jobs to the queue (arguments: add <entity type> [* | <entity ids>]...)

by Jose Luis Campanello
"""

import sys

from   globals      import *
from   cmd          import command_dispatch

#########################################################
#########################################################
#
# MAIN FUNCTION
#


def main():
    """The main function"""

    set_logger(configPrefix, generatorPrefix)

    # get the arguments
    arguments = sys.argv[1:]
    command_dispatch(arguments)


if __name__ == "__main__":
    main()
