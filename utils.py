import yaml 
from models import ConfigFile
from pathlib import Path

def yaml_import(config_path: Path) -> ConfigFile:

        with open(config_path, 'r') as config_file:
            config = ConfigFile.model_validate(yaml.safe_load(config_file))
        return config
