import time
from abc import ABC

from main.clientfactory.webdriver_factory import WebDriverFactory
from main.interfaces.iweb import IWeb


class PlayWrightActions(IWeb, WebDriverFactory):
    def navigateToURL(self, url):
        self._driver.goto(url)

    def click(self, locator):
        self._driver.click(locator[1])

    def type(self, locator, testData):
        self._driver.fill(locator[1],testData)

    def getElement(self, locator):
        pass

    def waitTime(self, seconds):
        time.sleep(seconds)

    def verifyTitle(self, textToVerify):
        assert self._driver.url.__contains__(textToVerify)

    def takeScreenshot(self, path):
        pass
