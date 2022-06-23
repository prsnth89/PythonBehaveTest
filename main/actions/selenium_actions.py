import time
from abc import ABC

from main.clientfactory.webdriver_factory import WebDriverFactory
from main.commonutils.utils import Utils
from main.interfaces.iweb import IWeb


class SeleniumActions(IWeb, WebDriverFactory):
    # def __init__(self, driver):
    #     self._driver= driver

    def navigateToURL(self, url):
        self._driver.get(url)
        print(self._driver.current_url)

    def getElement(self, locator):
        locatorID = locator[0]
        locatorValue = locator[1]
        print(locator)
        return self._driver.find_element(locatorID, locatorValue)

    def click(self, locator):
        element = self.getElement(locator)
        element.click()
        print("Test click")

    def type(self, locator, testData):
        element = None
        element = self.getElement(locator)
        element.clear()
        element.send_keys(testData)
        print("Test type")

    def waitTime(self, seconds):
        time.sleep(3)

    def verifyTitle(self, textToVerify):
        url=self._driver.current_url
        print(url)
        assert url.strip(" ").__contains__(textToVerify)

    def takeScreenshot(self,path):
        imageFile=Utils().getCurrentDateAndTime()+".png"
        #imageFile=screenshotName+".png"
        systempath={path}
        print(f"systempath---{systempath}")
        filePath=f'{path}\{imageFile}'
        print(f'screenshot name---{imageFile}')
        self._driver.save_screenshot(filePath)
        print(f'Filepath---{filePath}')