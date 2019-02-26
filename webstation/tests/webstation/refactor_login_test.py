from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..","..", ".." ))
from webstation.pages.refactor_login_page import LoginPage
from webstation.pages.header_page import HeaderPage
import unittest

class LoginTest(unittest.TestCase):
    base_url = 'http://webstationtest3.ttweb.net/WebStation.aspx'
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(base_url)


    lp = LoginPage(driver)
    lo = HeaderPage(driver)
    lp.noEulaLogin('milo.jovanovi72', 'Proba020')
    time.sleep(2)

    lp.invalidUserName('milos.jovanovi72', 'Proba020')
    time.sleep(2)

    lp.invalidPassword('milo.jovanovi72', 'proba020')
    time.sleep(2)

    lp.validLogin('milo.jovanovi72', 'Proba020')
    time.sleep(10)

    lo.logout()
    time.sleep(2)

    driver.close()
    driver.quit()

