#!/usr/bin/python3

# https://www.toptal.com/python/in-depth-python-logging

import logging
import sys
from logging.handlers import TimedRotatingFileHandler
FORMATTER = logging.Formatter("%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S")
LOG_FILE = '/var/tmp/test.log'

def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler

def get_file_handler():
    file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
    file_handler.setFormatter(FORMATTER)
    return file_handler

def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG) # better to have too much log than not enough
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    # with this pattern, it's rarely necessary to propagate the error up to parent
    logger.propagate = False
    return logger

if __name__ == "__main__":
    logger = get_logger("auditaga")
    logger.info("Just a start")