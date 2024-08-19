import pytest
from selenium import webdriver
from datetime import datetime
from utilities.urls import Urls
import os
import logging


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
    logging.info(f"Browser: {request.param}")
    logging.info(f"Test URL: {Urls.home}")
    driver.maximize_window()
    yield
    logging.info("Close Driver")
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

    # Configure logging
    # Set up logging
    logging.basicConfig(
        filename='test_log.log',  # Log file name
        level=logging.INFO,  # Logging level
        format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
        filemode='w'  # Overwrite the log file each time
    )
    logging.info("Logging started")


def pytest_runtest_setup(item):
    # Log the name of the current test case
    logging.info(f"Starting test case: {item.name}")


def pytest_runtest_makereport(item, call):
    # Log the test case failure if it failed during the call phase
    if call.when == 'call' and call.excinfo is not None:
        # Extract file name, line number, and error message
        tb = call.excinfo.traceback[-1]  # Get the last traceback entry
        file_name = os.path.basename(tb.path)
        line_number = tb.lineno + 1
        error_message = call.excinfo.value

        # Log the failure details
        logging.error(f"Test case {item.name} failed")
        logging.error(f"File: {file_name}, Line: {line_number}")
        logging.error(f"Error: {error_message}")
