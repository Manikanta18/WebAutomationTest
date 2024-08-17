from pages.base_page import BasePage
from utilities.locators import DashboardLocatorFields


class DashboardPage(BasePage):
    def __init__(self, driver):
        self.locate = DashboardLocatorFields
        super().__init__(driver)

    def click_nav_button(self, name):
        self.click(DashboardLocatorFields.navbar_links[name])

    def input_text_search(self, value):
        self.set(DashboardLocatorFields.search_field, value)

    def search_title(self):
        return self.get_text(DashboardLocatorFields.search_field_title)

    def search_something(self, value):
        self.input_text_search(value)
        self.click(DashboardLocatorFields.search_button)
