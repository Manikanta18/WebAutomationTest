import time

from pages.dashboard_page import DashboardPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from tests.base_test import BaseTest
from utilities.test_data import TestData
from utilities.urls import Urls
import pytest

pytestmark = [pytest.mark.sanity]


class TestProduct(BaseTest):
    def test_single_product(self):
        product_page = ProductPage(self.driver)
        dashboard = DashboardPage(self.driver)
        test_data = TestData.single_product

        dashboard.click_nav_button(test_data.get("product_type"))
        product_page.click_product(test_data.get("product_id"))
        product_page.click_product(test_data.get("item_id"))

        assert product_page.get_product_name() == test_data.get("name")
        assert product_page.get_price() == test_data.get("price")

    @pytest.mark.cart
    def test_add_product_to_cart_with_login(self):
        self.driver.get(Urls.login)
        login_page = LoginPage(self.driver)
        test_data = TestData.valid_user_login_data

        login_page.log_into_application(test_data.get("username"), test_data.get("password"))
        is_logged_in = login_page.check_if_page_contains_text("My Account")

        assert is_logged_in

        product_page = ProductPage(self.driver)
        dashboard = DashboardPage(self.driver)
        test_data = TestData.cart_product

        dashboard.click_nav_button(test_data.get("product_type"))
        product_page.click_product(test_data.get("product_id"))
        product_page.click_product(test_data.get("item_id"))

        product_page.click_add_to_cart()
        product_page.click_check_out()
        product_page.click_billing_button("Continue")
        product_page.click_billing_button("Confirm")
        message = product_page.get_message()

        assert "submitted" in message
