"""Functions related to the program commands

Many commands are imported from external files (cmd_queue.py,
cmd_updates.py) but other commands are defined in this file.

Also, the whole cmd_task (and depending functions) is defined
in here.

A YAML file (in /etc/ecommerce) defines the valid tasks. Each
task is a group of valid commands (ex: add, delta, updates, etc).

Tasks can have exclusion times. This means that when the specified
task is invoked during those times, the task will not be executed,
but no error report will be issued.

"""

import  sys
import  logging
import  platform
import  datetime
import  os
import  os.path
from    yaml    import safe_load

import ecommerce.config
import ecommerce.db
from   ecommerce.queue import *

from   globals      import *
from   cmd_queue    import cmd_add, cmd_delta, cmd_exit, cmd_cache, cmd_list, \
                           cmd_regen, cmd_sitemap
from   cmd_updates  import cmd_updates
import daemon


#########################################################
#########################################################
#
# COMMAND - DAEMON
#
def cmd_daemon(arguments):
    """Go into daemon mode"""

    # get the config and a consumer
    config = ecommerce.config.getConfig()
    consumer = None
    try:
        consumer = ecommerce.queue.queue(config, queuePrefix, False)
    except QueueConfigurationException as ex:
        print "CONFIG: %s" % ex
        return -1
    except QueueRuntimeException as ex:
        print "RUNTIME: %s" % ex
        return -1
    except QueueFolderLockException:
        # not an error, there is another daemon running
        print "WARNING: cannot start daemon, already running"
        return 0
    except Exception as ex:
        print "ERROR: %s" % ex
        return -1

    # go daemon
    return daemon.daemon(config, configPrefix, daemonPrefix, consumer)


#########################################################
#########################################################
#
# COMMAND - HELP
#
def cmd_help(arguments):

    print """usage: python generator.py [parameters]
    
Where parameters can be one of:
- add job to the regeneration queue
    "add" ( <entity type>[/<subtype>] [ * | <entity id list> ] )+

  Where the "/<subtype>" addition is only valid for SUBJ. This provides
  a greater degree of control of what and in what sequence to generate.

- regenerate internal cache (images, interviews, biographies, etc)
    "cache"

- go into daemon mode
    "daemon"

- process the database delta (things that changed, see command updates)
    "delta"

- cause the daemon to exit (using a job, which can take some time)
    "exit"

- print help (default option if cannot figure out what to do)
    "help"

- list the queue
    "list"

- regenerate several components (execute the command without params for help)
    "regen"

- generate the sitemaps for Google (uses the job queue)
    "sitemap"

- list all the available subtypes
    "subtypes"

- figure out the list of updated database's records (things that changed)
    "updates"
"""

    return 0


#########################################################
#########################################################
#
# COMMAND - SUBTYPES
#
def cmd_subtypes(arguments):
    """List al entity types with the available subtypes"""

    print "The known entity types (and subtypes) are:"
    print ""

    # list types
    for type in entityTypes:
        sub = ("subtypes: " + ", ".join(subtypes[type])) if subtypes[type] else "no subtypes"
        print "%s - %s" % (type, sub)

    print ""

    return 0


#########################################################
#########################################################
#
# COMMAND - TASK
#
def task_load():
    """Loads the task configuration file"""

    # get a config file
    config = ecommerce.config.getConfig()

    # get the task file
    fname = config.getMulti(configPrefix, application + ".tasks.file")
    if fname is None:
        fname = "/etc/ecommerce/tasks.yaml"
        if platform.system() == "Windows":
            fname = 'c:\\etc\\ecommerce\\tasks.yaml'

    # if it is still none => return a default tasks file
    if fname is None:
        return {
            "exclude" : { },
            "tasks"   : { }
        }

    # if the file does not exists => error => return None
    if not os.path.exists(fname):
        return None
    try:
        f = open(fname, 'r')
        tasksText = f.read()
        f.close()
    except:
        return None

    # try to parse the file, if error, return None
    tasks = None
    try:
        # read and parse the configuration
        tasks = safe_load(tasksText)
    except:
        return None

    # be sure that we have an "exclude" and a "tasks" section
    if "tasks" not in tasks or not isinstance(tasks["tasks"], dict):
        return None
    if "exclude" not in tasks or not isinstance(tasks["exclude"], dict):
        return None

    return tasks


def time_excluded(tasks, task_name, task_def):
    """Check if the task is in exclusion time"""

    time_excluded.week_days = {
        "monday"        : 0,
        "tuesday"       : 1,
        "wednesday"     : 2,
        "thursday"      : 3,
        "friday"        : 4,
        "saturday"      : 5,
        "sunday"        : 6,
        "mon"           : 0,
        "tue"           : 1,
        "wed"           : 2,
        "thu"           : 3,
        "fri"           : 4,
        "sat"           : 5,
        "sun"           : 6,
        "lunes"         : 0,
        "martes"        : 1,
        "miercoles"     : 2,
        "jueves"        : 3,
        "viernes"       : 4,
        "sabado"        : 5,
        "domingo"       : 6,
        "lun"           : 0,
        "mar"           : 1,
        "mie"           : 2,
        "jue"           : 3,
        "vie"           : 4,
        "sab"           : 5,
        "dom"           : 6
    }

    # get current time data
    now  = datetime.datetime.now().timetuple()
    time_vars = {
        "week_day"  : now.tm_wday,
        "minute"    : now.tm_hour * 60 + now.tm_min
    }

    # get the exclusion entry from the task def (no entry is valid)
    exclusion = task_def["exclude"] if "exclude" in task_def else None
    if exclusion is None:
        # not in time exclusion
        return False

    # get the list of exclusion times (if not present, assume empty)
    excluded = tasks["exclude"][exclusion] if exclusion in tasks["exclude"] else [ ]

    # process each possible entry
    for e in excluded:

        # convert the tuple to a valid format
        w_day     = e[0]
        min_start = e[1]
        min_end   = e[2]
        if w_day in time_excluded.week_days:
            w_day = time_excluded.week_days[w_day]
        else:
            w_day = -1      # fail any match

        # now make the checks
        if w_day == time_vars["week_day"]:
            # check the minute range
            if  min_start <= time_vars["minute"] and \
                time_vars["minute"] < min_end:

                # we are in exclusion time
                return True

    return False


def execute_task(task_name, task_def):
    """Execute the defined tasks"""

    # sanity check
    commands = [ ]
    if "commands" not in task_def or \
        not isinstance(task_def["commands"], list):

        # log and fail
        logger.error("ERROR task %s has no commands definition" % (task_name, ))
        return False

    # dispatch each command
    for c in range(len(task_def["commands"])):

        command = task_def["commands"][c]

        logger.info("task %s: dispatching command %s" % (task_name, command))
        command_dispatch(command)

    return True


def cmd_task(arguments):
    """Execute the named task"""

    set_logger(configPrefix, tasksPrefix)

    # load the task definition file
    tasks = task_load()
    if tasks is None:
        print "FATAL ERROR - Cannot read the tasks file"
        logger.info("FATAL ERROR - Cannot read the tasks file")
        return -1

    # if no extra arguments => dump the list of defined tasks
    if len(arguments) < 2:
        # explain the command and print the list of subcommands
        print ""
        print "The task command provides for way to execute sets"
        print "of tasks where each task is a valid generator.py"
        print "command. The available tasks are:"
        print ""
        print "There are %d defined tasks" % len(tasks["tasks"])
        print ""
        for t in tasks["tasks"]:
            print "Task %s" % t

        return 0

    # get the tasks to execute and execute them
    to_do = arguments[1:]
    while len(to_do) > 0:

        # get the first task and it's definition
        task_name = to_do[0]
        task_def  = tasks["tasks"][task_name] \
                    if task_name in tasks["tasks"] \
                    else None

        print "executing task %s" % task_name,
        logger.info("will execute task %s" % task_name)

        # execute the task
        if task_def is not None:

            # set a termination message
            term = "- OK"

            # check the exclusion time
            if not time_excluded(tasks, task_name, task_def):
                # do execute
                if execute_task(task_name, task_def):
                    pass
                else:
                    term = "- ERROR executing tasks"
            else:
                term = "- IGNORE in exclusion time"

            print "%s" % term
            logger.info("did execute task %s %s" % (task_name, term) )
        else:
            print " - ERROR task does not exist"
            logger.info("did execute task %s - ERROR task does not exist" % task_name)

        # remove from the list
        to_do.pop(0)

    return 0


#########################################################
#########################################################
#
# COMMAND DISPATCHING
#
commands = {
    "add"           : cmd_add,
    "cache"         : cmd_cache,
    "daemon"        : cmd_daemon,
    "delta"         : cmd_delta,
    "exit"          : cmd_exit,
    "help"          : cmd_help,
    "list"          : cmd_list,
    "regen"         : cmd_regen,
    "sitemap"       : cmd_sitemap,
    "subtypes"      : cmd_subtypes,
    "task"          : cmd_task,
    "updates"       : cmd_updates,
    "__default__"   : cmd_help
}


def command_execute(cmd, arguments):
    """Execute a command (must be valid)"""

    # execute the command
    logger.info("Executing command %s with arguments %s" % (cmd, str(arguments)))
    result = commands[cmd](arguments)
    logger.info("Executed command %s with result %d" % (cmd, result))
    
    return result


def command_dispatch(arguments):
    """Distpatch a command (check it is valid)"""

    # get the command
    cmd = arguments[0] if len(arguments) >= 1 else "__default__"
    if cmd not in commands:
        cmd = "__default__"

    return command_execute(cmd, arguments)
