from selenium import webdriver
import unittest
import time
import pytest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from webstation.pages.ws_login_page import LoginPage
import HtmlTestRunner 

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.driver.get('http://webstationtest3.ttweb.net/WebStation.aspx')


    def test1_fail_eula(self):
        driver = self.driver
        login = LoginPage(driver)
        driver.implicitly_wait(3)

        login.enter_username('milo.jovanovi72')
        login.enter_password('Proba020')
        login.click_login()
        # time.sleep(1)


    def test2_wrong_pass(self):
        driver = self.driver
        login = LoginPage(driver)
        driver.refresh()
        driver.implicitly_wait(3)       
        login.enter_username('milo.jovanovi72')
        login.enter_password('Proba0201')
        login.check_eula()
        time.sleep(1)
        login.click_login()
        # time.sleep(1)

    def test3_valid_login(self):
        driver = self.driver
        login = LoginPage(driver)
        driver.refresh()
        login.enter_username('milo.jovanovi72')
        login.enter_password('Proba020')
        login.click_login()
        time.sleep(5)

    def test4_logout(self):
        driver = self.driver
        login = LoginPage(driver)
        # driver.refresh()
        # time.sleep(1)
        driver.implicitly_wait(5)
        login.logout()
        time.sleep(2)



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test Completed')
        
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\MJ\MJ\PROJECTS\AutomationFramework_1\webstation\reports\test-runner'), verbosity=2)
