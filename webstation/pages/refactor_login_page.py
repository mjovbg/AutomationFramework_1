from selenium.webdriver.common.by import By
from webstation.base.selenium_webdriver import SeleniumDriver


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators:

    _username_textbox       =       'userName'
    _password_textbox       =       'password'
    _eula_checkbox          =       "//label[contains(text(),'I accept the')]"
    _login_button           =       'loginUser'

    # warning_messages:
    _eula_alert_xpath             =       "//td[contains(text(),'You have to accept the End User License Agreement ')]"
    _credentials_alert_xpath      =       "//div[@class='error_container_inner']"


    def enterUsername(self, username):
        self.sendKeys(username, self._username_textbox)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_textbox)

    def clickEula(self):
        self.elementClick(self._eula_checkbox, locatorType="xpath")
        # self.driver.find_element_by_xpath(self._eula_checkbox).click()

    def clickLoginButton(self):
        self.elementClick(self._login_button)

    def noEulaLogin(self, username, password):
        self.clearField(self._username_textbox)
        self.enterUsername(username)
        self.clearField(self._password_textbox)
        self.enterPassword(password)

        self.clickLoginButton()
        self.isElementPresent(self._eula_alert_xpath, locatorType='xpath')
        self.getText(self._eula_alert_xpath, locatorType='xpath')

    def invalidUserName(self, username, password):
        self.clearField(self._username_textbox)
        self.enterUsername(username)
        self.clearField(self._password_textbox)
        self.enterPassword(password)

        self.clickEula()
        self.clickLoginButton()
        self.isElementPresent(self._credentials_alert_xpath, locatorType='xpath')
        self.getText(self._credentials_alert_xpath, locatorType='xpath')

    def invalidPassword(self, username, password):
        self.clearField(self._username_textbox)
        self.enterUsername(username)
        self.clearField(self._password_textbox)
        self.enterPassword(password)

        # self.clickEula()
        self.clickLoginButton()
        self.isElementPresent(self._credentials_alert_xpath, locatorType='xpath')
        self.getText(self._credentials_alert_xpath, locatorType='xpath')


    def validLogin(self, username, password):
        self.clearField(self._username_textbox)
        self.enterUsername(username)
        self.clearField(self._password_textbox)
        self.enterPassword(password)

        self.clickEula()
        self.clickLoginButton()


