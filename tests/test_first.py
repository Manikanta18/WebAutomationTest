# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pytest
# import time
#
# pytestmark = [pytest.mark.regression, pytest.mark.sanity]
#
# driver = webdriver.Chrome()
#
# @pytest.fixture()
# def setup_teardown():
#     driver.get("https://phptravels.net/login")
#     driver.find_element(By.ID, "email").send_keys("user@phptravels.com")
#     driver.find_element(By.ID, "password").send_keys("demouser")
#     driver.find_element(By.ID, "submitBTN").click()
#     print("Log In")
#     time.sleep(1)
#
#     yield
#
#     driver.find_element(By.PARTIAL_LINK_TEXT,
#                         "Logout").click()
#     print("Log Out")
#
#
# @pytest.mark.integration
# def test_bookings(setup_teardown):
#
#     driver.find_element(By.LINK_TEXT,
#                         "My Bookings").click()
#     time.sleep(1)
#     heading = driver.find_element(By.XPATH, "//*[@id='flights']/div[1]/div/div/h3[1]").text
#     assert heading == "Bookings"
#
