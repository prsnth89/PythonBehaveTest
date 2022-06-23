from playwright.sync_api import sync_playwright, Playwright, Page
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.ie.service import Service
from selenium.webdriver.ie.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager


class WebDriverFactory:
    _driver: WebDriver = None
    _driver: Page = None
    _playwright_browser: Playwright = None

    def open_browser(self, browserName):
        if browserName == "chrome":
            _driver = webdriver.Chrome(ChromeDriverManager().install())
        elif browserName == "firefox":
            _driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browserName == "ie":
            _driver = webdriver.Ie(service=Service(IEDriverManager().install()))
        else:
            print('Browser type not found - ' + browserName)
            raise Exception('Browser type not found - ' + browserName)
        self._driver = _driver
        self._driver.maximize_window()
        self._driver.delete_all_cookies()
        return self._driver

    def close_browser(self):
        self._driver.close()

    def open_play_wright_browser(self, browserName):
        print("Entering open_playwright_browser")
        if browserName == "chrome":
            playwright_browser = sync_playwright().start()
            browser = playwright_browser.chromium.launch(headless=False, slow_mo=50)
            driver = browser.new_page()

        elif browserName == "firefox":
            playwright_browser = sync_playwright().start()
            playwright_browser.firefox.launch(headless=False, slow_mo=50)
            driver = playwright_browser.new_page()
        elif browserName == "ie":
            playwright_browser = sync_playwright().start()
            playwright_browser.chromium.launch(headless=False, slow_mo=50)
            driver = playwright_browser.new_page()
        else:
            print('Browser type not found - ' + browserName)
            raise Exception('Browser type not found - ' + browserName)
        self._driver = driver

    def close_play_wight_browser(self):
        self._driver.close()
        self._playwright_browser.stop()
