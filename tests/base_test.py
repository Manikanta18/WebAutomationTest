import time

import pytest

from pages.login_page import LoginPage
from pages.base_page import BasePage
from utilities.test_data import TestData


@pytest.mark.usefixtures("initialize_driver")
class BaseTest:
    pass
