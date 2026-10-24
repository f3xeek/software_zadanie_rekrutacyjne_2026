from pathlib import Path

from utils import yaml_import


CONFIGFILE = Path('./simulator_config.yaml')

def main():
    config = yaml_import(CONFIGFILE)


    
