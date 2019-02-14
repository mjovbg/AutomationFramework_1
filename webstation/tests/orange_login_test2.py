from selenium import webdriver
import pytest
# _test.py convention

class TestLogin():

    @pytest.fixture(scope='class')        # with session fixture will run only once! with function will run for each test
    # if you use it in the class -> make session = 'class'
    def test_setup(self):
        global driver       # so you can use it elsewhere
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/')
        # now create teardown using yield
        yield
        driver.close()
        driver.quit()
        print('Test completed!')

    def test_login(self, test_setup):
        driver.find_element_by_id('txtUsername').send_keys('Admin')
        driver.find_element_by_id('txtPassword').send_keys('admin123')
        driver.find_element_by_id('btnLogin').click()

    def test_logout(self, test_setup):
        driver.find_element_by_id('welcome').click()
        driver.find_element_by_link_text('Logout').click()

    # def test_logout():        # no need for this if you use yield
    #     driver.close()
    #     driver.quit()
    #     print('Test completed!')




