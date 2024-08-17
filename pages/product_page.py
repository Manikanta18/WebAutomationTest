from pages.base_page import BasePage
from utilities.locators import DashboardLocatorFields
from pages.dashboard_page import DashboardPage


class ProductPage(BasePage):
    def __init__(self, driver):
        self.locate = DashboardLocatorFields
        super().__init__(driver)

    def click_product(self, product_id):
        self.click(DashboardLocatorFields.get_product_link_locator(product_id))

    def get_price(self):
        return self.get_text(DashboardLocatorFields.product_price_locator)

    def click_add_to_cart(self):
        self.click(DashboardLocatorFields.product_add_to_cart_button)

    def get_product_name(self):
        return self.get_text(DashboardLocatorFields.product_name_text)

    def click_check_out(self):
        self.click(DashboardLocatorFields.check_out_button)

    def click_billing_button(self, button_name):
        self.click(DashboardLocatorFields.get_billing_button_locator(button_name))

    def get_message(self):
        return self.get_text(DashboardLocatorFields.order_message)
