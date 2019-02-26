from selenium import webdriver
import time

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..","..", ".." ))
from webstation.pages.refactor_login_page import LoginPage
from webstation.pages.ws_navigation_page import NavigationPage
import unittest

class TestNavigation(unittest.TestCase):

    base_url = 'http://webstationtest3.ttweb.net/WebStation.aspx'
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(base_url)

    lp = LoginPage(driver)
    np = NavigationPage(driver)

    lp.validLogin('milo.jovanovi72', 'Proba020')
    np.clickMarkets()




    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.implicitly_wait(5)
    #     cls.driver.maximize_window()
    #     cls.driver.get('http://webstationtest3.ttweb.net/WebStation.aspx')
    #
    # def test1_valid_login(self):
    #
    #     driver = self.driver
    #     login = LoginPage(driver)
    #     login_test = TestLogin()
    #     login_test.test3_valid_login()

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



# if __name__ == "__main__":
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\MJ\MJ\PROJECTS\AutomationFramework_1\webstation\reports\test-runners'), verbosity=2)

