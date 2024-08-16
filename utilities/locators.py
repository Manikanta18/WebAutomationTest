from selenium.webdriver.common.by import By


class LoginPageLocatorFields:
    email_address_field = (By.ID, "email")
    password_field = (By.ID, "password")
    login_button = (By.ID, "submitBTN")
    warning_message = (By.XPATH, "//*[contains(text(), 'Invalid Login')]")
