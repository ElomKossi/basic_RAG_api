import logging

# we are setting the logging level to log everything at level info and above
logging.basicConfig(level=logging.INFO)

# we are creating one common logger for our application that we will later use
# everywhere we want to log stuff
# this provides common configuration and, if we want it, standard/format
logger = logging.getLogger(__name__)
# we will push the logs to the console/stdout
ConsoleOutputHandler = logging.StreamHandler()
logger.addHandler(ConsoleOutputHandler)