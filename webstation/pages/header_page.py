from selenium.webdriver.common.by import By
from webstation.base.selenium_webdriver import SeleniumDriver
import time

class HeaderPage(SeleniumDriver):
    '''
    Used after login.
    Should contain buttons: top 4 favorites, help, open in new browser, select layout, add/remove favorite, customize/control
    '''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators (start with customize/control):

    _user_button_id             =       "user-button"
    _logout_button_xpath        =       "//a[contains(text(),'Logout')]"



    def logout (self):
        self.elementClick(self._user_button_id)
        time.sleep(1)
        self.elementClick(self._logout_button_xpath, locatorType='xpath')








