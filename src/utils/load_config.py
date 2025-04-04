import os
import tomllib

BASE_DIR = os.getcwd()
CONFIG_DIR = os.path.join(BASE_DIR, 'src','config','config.toml')

def getConfig():
    with open(CONFIG_DIR, mode='+rb') as PF:
        config = tomllib.load(PF)
    return config

