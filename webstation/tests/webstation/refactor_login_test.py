from selenium import webdriver
from selenium.webdriver.common.by import By
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..","..", ".." ))
from webstation.pages.refactor_login_page import LoginPage
import unittest

class LoginTest(unittest.TestCase):
    base_url = 'http://webstationtest3.ttweb.net/WebStation.aspx'
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(base_url)


    lp = LoginPage(driver)
    lp.validLogin('milo.jovanovi72', 'Proba020')


