import datetime
import json
import os
from pathlib import Path


class Utils:

    def getCurrentDateAndTime(self):
        now = datetime.datetime.now()
        format = "%Y%m%d%H%M%S%f"
        return now.strftime(format)

    def _get_project_root(self) -> Path:
        return Path(__file__).parent.parent

    def read_config_file(self):
        root = self._get_project_root().parent
        config_path = os.path.join(root, 'resources\config.json')
        return config_path

    def readJSONFile(self,fileName):
        root=self._get_project_root().parent
        jsonPath = os.path.join(root, fileName)
        data=open(jsonPath)
        jsonData=json.load(data)
        print(jsonData)
        return jsonData

