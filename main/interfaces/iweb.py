from abc import abstractmethod


class IWeb:
    @abstractmethod
    def openBrowser(self, browserName):
        NotImplementedError

    @abstractmethod
    def quitBrowser(self):
        NotImplementedError

    @abstractmethod
    def navigateToURL(self, url):
        NotImplementedError

    @abstractmethod
    def click(self, locator):
        NotImplementedError

    @abstractmethod
    def type(self, locator, testData):
        NotImplementedError

    @abstractmethod
    def getElement(self, locator):
        NotImplementedError

    @abstractmethod
    def waitTime(self, seconds):
        NotImplementedError

    @abstractmethod
    def verifyTitle(self, textToVerify):
        NotImplementedError

    @abstractmethod
    def takeScreenshot(self,path):
        NotImplementedError
