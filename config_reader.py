
from collections import namedtuple


def read_config():
    config_vars = {}
    with open("config.txt") as config_file:
        for line in config_file:
            name, var = line.partition("=")[::2]
            config_vars[name.strip()] = var.rstrip()
            
    return namedtuple("Config", config_vars.keys())(*config_vars.values())