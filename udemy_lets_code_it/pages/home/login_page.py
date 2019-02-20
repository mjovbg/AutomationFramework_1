from selenium.webdriver.common.by import By
from udemy_lets_code_it.base.selenium_driver import SeleniumDriver

class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators for elements
    _login_link = 'login'
    _email_field = 'user_email'
    _password_field = 'password_field'
    _login_button = 'commit'

    # now return the elements

    # def getLoginLink(self):
    #     return self.driver.find_element(By.NAME, self._login_link)
    #
    # def getEmailField(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.NAME, self._login_button)

    # now create actions

    def clickLoginLink(self):
        # self.getLoginLink().click()
        self.elementClick(self._login_link, locatorType='link')

    def enterEmail(self, email):
        # self.getEmailField().send_keys()
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        # self.getPasswordField().send_keys()
        self.sendKeys(password, self._password_field)

    def clickLogin(self):
        # self.getLoginButton().click()
        self.elementClick(self._login_button, locatorType='name')


    def login(self, email, password):

        # loginLink = self.driver.find_element(By.LINK_TEXT, "Login")
        # loginLink.click()
        # elementField = self.driver.find_element(By.ID, "user_email")
        # elementField.send_keys(username)
        # passwordFiled = self.driver.find_element(By.ID, "user_password")
        # passwordFiled.send_keys(password)
        #
        # loginButton = self.driver.find_element(By.NAME, "commit")
        # loginButton.click()

# after adding locators and action methods
        # functionalities that wrap all the actions:
        self.clickLogin()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLogin()
