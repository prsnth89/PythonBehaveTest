from behave import *

from features.lib.demo.pages.home_page import HomePage
from features.lib.demo.pages.login_page import LoginPage


class DemoStepDef:
    use_step_matcher("re")
    # iWeb = None
    _loginPage = None
    _home_page = None

    @then('enter username "(?P<username>.+)" and password "(?P<password>.+)"')
    def step_impl(self, username, password):
        print("Enter username and password in step def")
        print(self.iWeb)
        self._loginPage = LoginPage(self.iWeb)
        self._loginPage.enter_user_name(username)
        self._loginPage.enter_password(password)

    @then("click login")
    def step_impl(self):
        self._loginPage.click_login()
        print('click login')

    @step("verify login success")
    def step_impl(self):
        self._home_page = HomePage(self.iWeb)
        self._home_page.verify_home_page_text()
        print('Login successfull')
