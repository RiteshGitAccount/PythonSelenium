import inspect
import logging


def custom_logger(log_level=logging.DEBUG):
    """
    This will create the log file with detailed log of the execution performed with log level provided
    :param log_level:
    :return:
    """
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)

    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")

    file_handler = logging.FileHandler('automation.log', mode='a')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(log_level)

    logger.addHandler(file_handler)
    return logger
