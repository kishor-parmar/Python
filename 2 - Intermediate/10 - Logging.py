# Logging

# Different Levels of Logging
print("*** Different Levels of Logging ***")

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%y %H:%M:%S",
)

logging.debug("this is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
print()
