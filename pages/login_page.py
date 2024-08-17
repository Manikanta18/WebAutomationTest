from pages.base_page import BasePage
from utilities.locators import LoginPageLocatorFields


class LoginPage(BasePage):

    def __init__(self, driver):
        self.locate = LoginPageLocatorFields
        super().__init__(driver)

    def set_email_address(self, username):
        self.set(self.locate.username_field, username)

    def set_password(self, password):
        self.set(self.locate.password_field, password)

    def click_login_button(self):
        self.click(self.locate.login_button)

    def log_into_application(self, email, password):
        self.set_email_address(email)
        self.set_password(password)
        self.click_login_button()
