from selenium.webdriver.common.by import By


class LoginPageLocatorFields:
    username_field = (By.NAME, "username")
    password_field = (By.NAME, "password")
    login_button = (By.XPATH, "//*[@id='Signon']/form/div/div/button")


class DashboardLocatorFields:
    navbar_links = {
        "fish": (By.XPATH, "//*[@id='QuickLinks']/a[text()='Fish']"),
        "dogs": (By.XPATH, "//*[@id='QuickLinks']/a[text()='Dogs']"),
        "reptiles": (By.XPATH, "//*[@id='QuickLinks']/a[text()='Reptiles']"),
        "cats": (By.XPATH, "//*[@id='QuickLinks']/a[text()='Cats']"),
        "birds": (By.XPATH, "//*[@id='QuickLinks']/a[text()='Birds']")
    }
    dashboard_title = (By.XPATH, "//*[@id='Catalog']/h3")
    search_field = (By.XPATH, "//*[@id='SearchContent']/form/div/input")
    search_field_title = (By.XPATH, "//*[@id='Catalog']/h3")
    search_button = (By.XPATH, "//button[text()='Search']")

