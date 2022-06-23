from behave import *

from main.actions.rest_actions import RestActions
from main.commonutils.config_manager import ConfigManager

use_step_matcher("re")


@given("hit the given url")
def step_impl(context):
    hostURL = ConfigManager().initialize_env_config("appConfig", "apiURL")
    print("current url--", hostURL)
    test = "api/users"
    global url
    url= hostURL + test
    print(url)
    response = RestActions().getJSONResponse(url)
    print(response)


@then("verify the success response from url")
def step_impl(context):
    response_code = RestActions().getResponseCode(url)
    print("ResponseCode---",response_code.status_code)
    assert response_code.status_code==200
