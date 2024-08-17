import time
from pages.dashboard_page import DashboardPage
from tests.base_test import BaseTest
from utilities.test_data import TestData
import pytest

pytestmark = [pytest.mark.sanity]


class TestDashboard(BaseTest):
    @pytest.mark.smoke
    @pytest.mark.parametrize("animal", ["Dogs", "Reptiles", "Cats", "Birds", "Fish"])
    def test_navbar_product_buttons(self, animal):
        dashboard = DashboardPage(self.driver)
        dashboard.click_nav_button(animal)
        title = dashboard.get_dashboard_title()
        assert title == animal

    @pytest.mark.smoke
    def test_search_field(self):
        dashboard = DashboardPage(self.driver)
        search_input = TestData.search_input
        dashboard.search_something(search_input)
        search_value = dashboard.search_title()
        assert search_input in search_value
