
class BasePage:
    """
  The Purpose Of A BasePage Is To Contain Methods Common To All Page Objects
  """

    def __init__(self, driver):
        self.driver = driver

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(*locator).click()

    def set(self, locator, value):
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)

    def get_text(self, locator):
        return self.find(*locator).text

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def check_if_page_contains_text(self, value):
        if value in self.driver.page_source:
            return True
        return False
