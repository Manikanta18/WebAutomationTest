import pytest
from selenium import webdriver
from datetime import datetime
from utilities.test_data import TestData
import os

@pytest.fixture(params=["chrome", "edge"])
def initialize_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver = webdriver.Edge()
    request.cls.driver = driver
    print("Browser: ", request.param)
    driver.get(TestData.url)
    driver.maximize_window()
    yield
    print("Close Driver")
    driver.close()


def pytest_configure(config):
    # Ensure the reports directory exists
    reports_dir = "reports"
    os.makedirs(reports_dir, exist_ok=True)

    # Generate the timestamped report filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_filename = os.path.join(reports_dir, f"report_{timestamp}.html")

    # Set the HTML report path in the pytest config
    config.option.htmlpath = report_filename
