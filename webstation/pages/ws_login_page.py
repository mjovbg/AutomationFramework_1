# Webstation Login
import time
from selenium import webdriver

class LoginPage():

    # create constructor:
    def __init__(self, driver):
        self.driver = driver

        # add html elements/locator types:
        self.username_textbox_id =          'userName'
        self.password_textbox_id =          'password'
        self.stay_logged_checkbox_xpath =   '//*[@id="login"]/table/tbody/tr[3]/td/label'
        self.eula_checkbox_xpath =          '//*[@id="login"]/table/tbody/tr[4]/td/label[1]'
        self.login_button_id =              'loginUser'
        self.eula_warning_xpath =           "//div[@class='error_container_inner']"
        self.wrong_password_warning_xpath = "//td[@class='red']"
        self.user_button_id =               'user-button'
        self.logout_button_xpath =           "//a[contains(text(),'Logout')]"

    # now create functions/methods:
    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()    # good practice!
        time.sleep(1)
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)
    
    def check_eula(self):
        # self.driver.find_element_by_xpath(self.eula_checkbox_xpath).clear()
        self.driver.find_element_by_xpath(self.eula_checkbox_xpath).click()

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def logout(self):
        self.driver.find_element_by_id(self.user_button_id).click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath(self.logout_button_xpath).click()









#