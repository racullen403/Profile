"""
BASICS 


Basic logger for learning purposes.

Best use cases are for recording events in a running application, without having to raise an error or run separate code to deal with it.

Loggers have a Severity level heirarchy, by default at level WARNING:
    - DEBUG
    - INFO
    - WARNING
    - ERROR
    - CRITICAL

Logging is done by default on the root logger, you will see this in the log, SEVERITY:root:Message, We can configure this using basicConfig().

In general, it is better to control the logger explicity by creating it yourself and calling its methods.

We can log variable data using formatting, logging predates newer formatting techniques, hence the %-style can be used also.

We can alter the default message format in the basicConfig() with format="..."


_________________________________________________
ADVANCED:

Loggers expose the interface that code uses.
Handlers send log records to appropriate destination.
Filters provide fine grain facility for which log records to output.
Formatters specify the layout of the log recode in final output.

All this log event info is passes between loggers, handlers, filters and formatters in the LogRecord instance.

Conceptually, our loggers have a name and are arranged in a namespace hierarchy, ie scan is is the parent of scan.text, scan.html and scan.pdf.

It is good to use the module-level logger ie logger=logging.getLogger(__name__), this way the names track the package/module heirarchy and is very intuitive.

The root of this hierarchy is the root logger, using funtions like debug(), info(), warning(), error() and critical() which call the respective methods of the root logger.

We can log our messages to different destinations. This is done by handlers. If none is set, our logging functions default their destination to console (sys.stderr) 
and use default format before letting the root logger do the message output. ie severity:logger name:message

Logger has 3 main jobs
    - Expose application code for logging at runtime
    - Apply logic to determine which log messages to act upon
    - Pass releven log massages to all relevant log handlers

Loggers have 2 common method categories, configuration and message sending.

Configuration
    - setLevel(), specify lowest severity level
    - addHandler() and removeHandler()
    - addFilter() and removeFilter()

Messaging
    - debug(), info(), warning(), error(), critical()
    - exception() is similar to error() except it will also dump the stack trace, usually done from an exception Handler.
    - log() takes log level as an explicit argument, used for custom log levels.

Note that is a level is not set on the logger, then it will use the level of the parent and so on up the chain until the root logger which has WARNING. This is what 
the logger uses to decide when to send an event to a handler.

Child loggers will propagate the log message up to handlers with their ancestor loggers. (we can set this to False)


Unless creating custom handlers, we only really need to be concerned with a few methods for built-in handlers.
    - setLevel(), different from loggers setLevel() which chooses what to send to the handler, this will determine what gets sent on.
    - setFormatter() lets us select a Formatter Object for this handler to use.
    - addFilter()/removeFilter() configure filter objects on handlers.

The Formatter Object configures the final structure of the log message.
    - logging.Formatter.__init__(fmt=None, datefmt=None, style="%")
    - fmt controls the message format
    - datefmt controls the date/time format
    - style is to specify what formatting technique used, %,{, $, defaulted to %.

We can set out logger up in 3 ways:
    - Through python code, manually creating and assigning the logger its handlers and formatters (see below).
    - Through the logging.config.fileConfig("...filepath..."), this allows us to set everything up in a separate file.
    - Through the latest dictConfig(), recommended, this is a superset of the config approach and uses the Python dictionary to configure information giving 
    more options, ie JSON, YAML, or python code to recieve is "pickled" over a socket.

"""

import logging
import logging.config
import yaml
import os 
import sys

def test1():
    # Create logger instance called __name__ and to log at log level DEBUG
    logger = logging.getLogger("myLogger")
    logger.setLevel(logging.DEBUG)

    # Create Handlers to send log message to files, mode="a" is default, mode="w" will overwrite the file
    log1 = logging.FileHandler(filename="Learning/MyLogger/log1.log", mode="w")
    log2 = logging.FileHandler(filename="Learning/MyLogger/log2.log", mode="w")

    # Apply some Handler logic to deal with the log messages of certain log levels
    log1.setLevel(logging.DEBUG)
    log2.setLevel(logging.ERROR)

    # Create Formatters
    formatter = logging.Formatter(fmt="%(asctime)s:%(levelname)s:%(message)s", datefmt="%m/%d/%Y %I:%M:%S %p ")

    # Add formatter to handlers
    log1.setFormatter(formatter)
    log2.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(log1)
    logger.addHandler(log2)

    # Do some application things that run the logger
    logger.debug("log1")
    logger.info("log1")
    logger.warning("log1")
    logger.error("log1 and log2")
    logger.critical("log1 and log2")


def test2():
    # Choose the config file for logger
    logging.config.fileConfig(fname="Learning/MyLogger/MyConfig.conf")

    # Create the logger
    logger = logging.getLogger("myConfLogger")

    # Application code
    logger.debug("log3")
    logger.info("log3")
    logger.warning("log3 and log4")
    logger.error("log3 and log4")
    logger.critical("log3 and log4 and log5")

def test3():
    # Choose the config file for logger
    # Note that the input must be a dictionary so we are converting YAML to the dict using a context manager to read the file and load the data
    with open("Learning/MyLogger/MyConfig.yml", "r") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    logging.config.dictConfig(data)

    # Create the logger 
    logger = logging.getLogger("myDictLogger")

    # Application code
    logger.debug("log6")
    logger.info("log6")
    logger.warning("log6 and log7")
    logger.error("log6 and log7")
    logger.critical("log6 and log7")


def get_logger(logger_name, logger_format="%(levelname)s:%(filename)s:%(message)s"):
    # Create logger with given name parameter
    logger = logging.getLogger(logger_name)

    # Find the current environment value of LOG_LEVEL, else set to DEBUG, and set logger level
    log_level = os.environ.get("LOG_LEVEL", "DEBUG")
    logger.setLevel(log_level)

    # Create format instance
    formatter = logging.Formatter(logger_format)

    # Create Handler, attatching level and format
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)

    # Attach handler to logger and adjust settings
    logger.addHandler(console_handler)
    logger.propagate = False

    return logger

  

if __name__ == "__main__":
    test1()
    test2()
    test3()
    print(os.getcwd())