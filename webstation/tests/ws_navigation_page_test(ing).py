from selenium import webdriver
import unittest
import time
import pytest
from webstation.pages.ws_login_page import LoginPage
from webstation.tests.ws_login_complete_test import TestLogin
from webstation.pages.ws_navigation_page import NavigationPage
import HtmlTestRunner

class TestNavigation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.driver.get('http://webstationtest3.ttweb.net/WebStation.aspx')

    def test1_valid_login(self):

        driver = self.driver
        login = LoginPage(driver)
        login_test = TestLogin()
        login_test.test3_valid_login()

    # def test2_markets(self):
    #     driver = self.driver
    #     navigation = NavigationPage(driver)
    #     navigation.markets()
    #     time.sleep(5)





    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test Completed')



if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\MJ\MJ\PROJECTS\AutomationFramework_1\webstation\reports\test-runners'), verbosity=2)

