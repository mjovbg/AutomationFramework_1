from selenium import webdriver
from selenium.webdriver.common.by import By
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..","..", ".." ))
from udemy_learn_to_code.pages.home.login_page import LoginPage
import unittest

class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseURL = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.login("test@email.com", "abcabc")


        userIcon = driver.find_element(By.XPATH, '//*[@id="navbar"]/div/div/div/ul/li[4]/a')
        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login Failed")