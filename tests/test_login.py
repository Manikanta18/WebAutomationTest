import time

from pages.login_page import LoginPage
from tests.base_test import BaseTest
from utilities.test_data import TestData
import pytest

pytestmark = [pytest.mark.regression, pytest.mark.sanity]


class TestLogin(BaseTest):

    @pytest.mark.integration
    def test_valid_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.log_into_application(TestData.customer['email'], TestData.customer['password'])
        actual_title = login_page.get_title()
        assert actual_title == "Dashboard"

    @pytest.mark.smoke
    def test_invalid_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.log_into_application(TestData.invalid_customer['email'], TestData.invalid_customer['password'])
        time.sleep(1)
        actual_message = login_page.get_warning_message()
        assert actual_message.__contains__("Invalid Login")
