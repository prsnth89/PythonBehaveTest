import json
import os
import requests

from main.commonutils.config_manager import ConfigManager
from main.commonutils.utils import Utils


class RestActions:
    global response, statusCode

    def getResponseCode(self, url, headers=None):
        print("url--", url)
        return requests.get(url, headers=headers)

    def getJSONResponse(self, url):
        response = self.getResponseCode(url)
        json_response_result = (json.dumps(response.json(), indent=2))
        return json_response_result

    def post(self, url, data, headers=None):
        return requests.post(url, json=data, headers=headers)

    def put(self, url, data, headers=None):
        return requests.put(url, json=data, headers=headers)

    def patch(self, url, data, headers=None):
        return requests.patch(url, json=data, headers=headers)

    def delete(self, url, headers=None):
        return requests.delete(url, headers=headers)