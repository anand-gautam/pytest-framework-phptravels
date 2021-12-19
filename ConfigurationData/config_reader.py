import configparser
from Utils.logger_utliity import GenerateLog
import os

# PWD = os.path.dirname(os.path.abspath(__file__))


def read_config(section, key):
    config = configparser.RawConfigParser()
    config.read("ConfigurationData/config.ini")
    return config.get(section, key)
