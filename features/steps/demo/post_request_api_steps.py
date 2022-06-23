import requests
from behave import *
from requests import Response

from main.actions.rest_actions import RestActions
from main.commonutils.config_manager import ConfigManager
from main.commonutils.utils import Utils

use_step_matcher("re")

response : RestActions() = None
response_code=None
@given("post the body")
def step_impl(context):
    hostURL = ConfigManager().initialize_env_config("appConfig", "apiURL")
    jsonFile = Utils().readJSONFile('resources\\api\\post_req.json')
    print("current url--", hostURL)
    print("json file--", jsonFile)
    test = "api/users"
    global url
    global response_code
    url = hostURL + test
    print(url)
    context.response = RestActions().post(url, jsonFile)
    response_code=context.response.status_code
    print(response_code)


@then("validate the response code")
def step_impl(context):
    print("response code",context.response_code)
    assert context.response_code==201

