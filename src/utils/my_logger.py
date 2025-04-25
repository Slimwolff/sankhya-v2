import sys
import logging
from pythonjsonlogger import jsonlogger


def createLogger(logName: str):

    logger = logging.getLogger(logName)

    stdoutHandler = logging.StreamHandler(stream=sys.stdout)
    fileHandler = logging.FileHandler("app.log")

    jsonFmt = jsonlogger.JsonFormatter(
        "%(name)s %(asctime)s %(levelname)s %(filename)s %(lineno)s %(process)d %(message)s",
        rename_fields={"levelname": "severity", "asctime": "timestamp"},
        datefmt="%Y-%m-%dT%H:%M:%SZ",
    )

    stdoutHandler.setFormatter(jsonFmt)
    fileHandler.setFormatter(jsonFmt)

    logger.addHandler(stdoutHandler)
    logger.addHandler(fileHandler)

    logger.setLevel(logging.INFO)

    return logger