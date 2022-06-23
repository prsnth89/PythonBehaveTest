import json
import os
from pathlib import Path

from main.commonutils.utils import Utils


class ConfigManager:

    def initialize_env_config(self, configHeader, configName):
        configFile = Utils().read_config_file()
        config = open(configFile)
        data = json.load(config)
        application_header_value = data[configHeader]
        application_value = application_header_value[configName]
        return application_value

