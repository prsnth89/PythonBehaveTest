from behave.model_core import Status

from main.actions.playwright_actions import PlayWrightActions
from main.actions.selenium_actions import SeleniumActions
from main.commonutils.config_manager import ConfigManager

global iWeb,evidence_path


def before_all(context):
    print("-----before all-----")
    browser = ConfigManager().initialize_env_config("appConfig", "browserName")
    print(browser)
    context.browserName = browser
    print(context.browserName)


def before_scenario(context, scenario):
    context.iWeb = SeleniumActions()
    # context.iWeb = PlayWrightActions()
    context.iWeb.open_browser(context.browserName)
    # context.iWeb.open_play_wright_browser(context.browserName)
    context.iWeb.navigateToURL(ConfigManager().initialize_env_config("appConfig", "webBaseURL"))


def after_step(context, step):
    print(step)
    print(f"----after step---", step.status)
    if step.status == Status.failed:
        context.iWeb.takeScreenshot(context.evidence_path)
        print(f"stored screenshot successfully---path--{context.evidence_path}")


def after_scenario(context, scenario):
    # context.iWeb.close_play_wight_browser()
    context.iWeb.close_browser()
    print("Browser closed successfully")
