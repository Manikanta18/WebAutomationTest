import pytest
from selenium import webdriver
from datetime import datetime
from utilities.test_data import TestData
from utilities.urls import Urls
import os


# @pytest.fixture(params=["chrome", "edge", "firefox"])
# initializing driver/s
@pytest.fixture(params=["chrome"])
def initialize_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver = webdriver.Edge()
    request.cls.driver = driver
    driver.get(Urls.home)
    print("Browser: ", request.param)
    print("Test URL: ", Urls.home)
    driver.maximize_window()
    yield
    print("Close Driver")
    driver.close()


# configuration for html and allure reports
def pytest_configure(config):
    # Ensure the reports directory exists
    reports_dir = "reports"
    os.makedirs(reports_dir, exist_ok=True)

    # Generate the timestamped report filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_filename = os.path.join(reports_dir, f"report_{timestamp}.html")

    # Set the HTML report path in the pytest config
    config.option.htmlpath = report_filename

    # Specify the directory for Allure results
    allure_report_dir = os.path.join(os.getcwd(), 'reports', 'allure-results')

    # Ensure the directory exists
    os.makedirs(allure_report_dir, exist_ok=True)

    # Set the --alluredir option programmatically
    config.option.allure_report_dir = allure_report_dir

    # command to run allure : allure serve reports/allure-results
