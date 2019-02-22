from selenium import webdriver
import pytest
from webstation.pages.home_page_orange import HomePage
from webstation.pages.login_page_orange import LoginPage
from webstation.utils import utils_orange as utils

class TestLogin():

    @pytest.fixture(scope='class')
    def test_setup(self):
        global driver       # so you can use it elsewhere
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(utils.URL)
        # now create teardown using yield
        yield
        driver.close()
        driver.quit()
        print('Test completed!')

    def test_login(self, test_setup):
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.clcik_login()

    def test_logout(self, test_setup):
        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
