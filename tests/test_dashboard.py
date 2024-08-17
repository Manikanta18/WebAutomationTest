import time
from utilities.urls import Urls
from pages.dashboard_page import DashboardPage
from tests.base_test import BaseTest
from utilities.test_data import TestData
import pytest

pytestmark = [pytest.mark.sanity]


class TestDashboard(BaseTest):
    @pytest.mark.smoke
    def test_navbar_fish(self):
        dashboard = DashboardPage(self.driver)
        print(dashboard.get_title())
        dashboard.click_nav_button("fish")
        title = dashboard.get_text(dashboard.locate.dashboard_title)
        assert title == 'Fish'

    @pytest.mark.smoke
    def test_navbar_dogs(self):
        dashboard = DashboardPage(self.driver)
        print(dashboard.get_title())
        dashboard.click_nav_button("dogs")
        title = dashboard.get_text(dashboard.locate.dashboard_title)
        assert title == 'Dogs'

    @pytest.mark.smoke
    def test_navbar_reptiles(self):
        dashboard = DashboardPage(self.driver)
        print(dashboard.get_title())
        dashboard.click_nav_button("reptiles")
        title = dashboard.get_text(dashboard.locate.dashboard_title)
        assert title == 'Reptiles'

    @pytest.mark.smoke
    def test_navbar_cats(self):
        dashboard = DashboardPage(self.driver)
        dashboard.click_nav_button("cats")
        title = dashboard.get_text(dashboard.locate.dashboard_title)
        assert title == 'Cats'

    @pytest.mark.smoke
    def test_navbar_birds(self):
        dashboard = DashboardPage(self.driver)
        dashboard.click_nav_button("birds")
        title = dashboard.get_text(dashboard.locate.dashboard_title)
        assert title == 'Birds'

    @pytest.mark.smoke
    def test_search_field(self):
        dashboard = DashboardPage(self.driver)
        search_input = TestData.search_input
        dashboard.search_something(search_input)
        search_value = dashboard.search_title()
        assert search_input in search_value
