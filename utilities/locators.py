from selenium.webdriver.common.by import By


class LoginPageLocatorFields:
    username_field = (By.NAME, "username")
    password_field = (By.NAME, "password")
    login_button = (By.XPATH, "//*[@id='Signon']/form/div/div/button")


class DashboardLocatorFields:
    @staticmethod
    def get_navbar_link_locator(link_text):
        return By.XPATH, f"//*[@id='QuickLinks']/a[text()='{link_text}']"

    dashboard_title = (By.XPATH, "//*[@id='Catalog']/h3")

    search_field = (By.XPATH, "//*[@id='SearchContent']/form/div/input")
    search_field_title = (By.XPATH, "//*[@id='Catalog']/h3")
    search_button = (By.XPATH, "//button[text()='Search']")

    @staticmethod
    def get_product_link_locator(product_id):
        return By.XPATH, f"//*[@id='Catalog']/table/tbody//a[text()='{product_id}']"

    product_price_locator = (By.XPATH, "//*[@id='CenterForm']/table/tbody/tr[5]/td")

    product_add_to_cart_button = (By.XPATH, "//*[@id='CenterForm']//a[text()='Add to Cart']")
    product_name_text = (By.XPATH, "//*[@id='CenterForm']/h3")
