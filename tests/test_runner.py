import pytest
from selenium import webdriver

from utility.BaseClass import BaseClass

# def invoke_driver():
#     global driver
#     driver = webdriver.Chrome(
#         executable_path="/Users/nagarajualapati/PycharmProjects/Google_Pytest_e2e/driver/chromedriver")
#     # driver.get("https://www.google.com/intl/en_in/drive/")
#     driver.maximize_window()

class Testgoogle(BaseClass):

    def test_e2e(self):
        #self.driver.get("https://www.google.com/intl/en_in/drive/")
        self.driver.find_element_by_self.driver.find_element_by_xpath("//input[@id='identifierId']").send_keys("raju")