
from pages.base_page import BasePage
from utilities.locators import LoginPageLocatorFields


class LoginPage(BasePage):

    def __init__(self, driver):
        self.locate = LoginPageLocatorFields
        super().__init__(driver)

    def click_login_button(self, name):
        print(self.locate.loginDB_button[name])
        self.click(self.locate.loginDB_button[name])
