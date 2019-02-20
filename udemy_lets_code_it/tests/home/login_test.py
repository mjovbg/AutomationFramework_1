from selenium import webdriver
from selenium.webdriver.common.by import By
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..","..", ".." ))
from udemy_lets_code_it.pages.home.login_page import LoginPage
import unittest


class LoginTest(unittest.TestCase):



    def test_validLogin(self):
        baseURL = "https://learn.letskodeit.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        lp = LoginPage(driver)
        lp.login("test@email.com", "abcabc")


        userIcon = driver.find_element(By.CSS_SELECTOR, ".gravatar")
        if userIcon is not None:
            print("Login valid")
        else:
            print("Login failed")