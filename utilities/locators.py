from selenium.webdriver.common.by import By


class LoginPageLocatorFields:
    loginDB_button = {
        "customer": (By.XPATH, "//button[text()='Customer Login']"),
        "manager": (By.XPATH, "//button[text()='Bank Manager Login']")
    }


class CustomerPageLocatorFields:
    login_button = (By.XPATH, "//button[text()='Login']")


class ManagerPageLocatorFields:
    add_customer_button = (By.XPATH, "//button[text()='Add Customer']")
    open_account_button = (By.XPATH, "//button[text()='Open Account']")
    customers_list_button = (By.XPATH, "//button[text()='Customers']")
