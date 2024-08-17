import time
import pytest

from pages.login_page import LoginPage
from tests.base_test import BaseTest
from utilities.test_data import TestData
from utilities.urls import Urls



pytestmark = [pytest.mark.regression, pytest.mark.sanity]


class TestLogin(BaseTest):

    def test_customer_login(self):
        self.driver.get(Urls.login)
        login_page = LoginPage(self.driver)
        login_page.log_into_application(TestData.valid_user_login_data["username"], TestData.valid_user_login_data["password"])
        is_logged_in = login_page.check_if_page_contains_text("My Account")
        assert is_logged_in
