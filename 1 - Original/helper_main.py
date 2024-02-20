# Logging

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%y %H:%M:%S",
)

# Different Levels of Logging
print("*** Different Levels of Logging ***")
logging.debug("this is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
print()


logger = logging.getLogger(__name__)

# Create Handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler("helper.log")

# Level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("This is a Warning")
logger.error("This is an Error")
