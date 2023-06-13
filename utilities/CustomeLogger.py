import inspect
import logging


def custom_logger(logLevel=logging.DEBUG):
    """
    This will create the log file with detailed log of the execution performed with log level provided
    :param logLevel:
    :return:
    """
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)

    file_handler = logging.FileHandler("automation.log", mode="a")
    file_handler.setLevel(logLevel)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
