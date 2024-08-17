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
        test_data = TestData.valid_user_login_data

        login_page.log_into_application(test_data.get("username"), test_data.get("password"))
        is_logged_in = login_page.check_if_page_contains_text("My Account")

        assert is_logged_in
