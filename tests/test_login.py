import time

from pages.login_page import LoginPage
from tests.base_test import BaseTest
from utilities.urls import Urls
import pytest

pytestmark = [pytest.mark.regression, pytest.mark.sanity]


class TestLogin(BaseTest):

    @pytest.mark.integration
    def test_customer_login(self):
        login_page = LoginPage(self.driver)
        time.sleep(0.5)
        login_page.click_login_button("customer")
        time.sleep(0.5)
        current_page = login_page.get_current_url()
        assert current_page == Urls.customer_login

    @pytest.mark.smoke
    def test_manager_login(self):
        login_page = LoginPage(self.driver)
        time.sleep(0.5)
        login_page.click_login_button("manager")
        time.sleep(0.5)
        current_page = login_page.get_current_url()
        assert current_page == Urls.manager
