from selenium import webdriver
import unittest
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://webstationtest3.ttweb.net/WebStation.aspx')


driver.find_element_by_id('userName').send_keys('milo.jovanovi72')
driver.find_element_by_id('password').send_keys('Proba020')
driver.find_element_by_xpath('//*[@id="login"]/table/tbody/tr[4]/td/label[1]').click()
driver.find_element_by_id('loginUser').click()
print(driver.current_url)
driver.implicitly_wait(5)

# header part:
# markets
driver.find_element_by_xpath('//*[@id="lowerDiv"]/div[1]/table/tbody/tr[1]/td/div/table/tbody/tr/td[1]/a').click()
time.sleep(5)
print(driver.current_url)

# currencies
driver.find_element_by_xpath('//*[@id="lowerDiv"]/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr/td[1]/a').click()
time.sleep(5)
print(driver.current_url)

# fixed income
driver.find_element_by_xpath('//*[@id="fixedIncomeButton"]/table/tbody/tr/td[1]/a').click()
time.sleep(5)
print(driver.current_url)

# futures
driver.find_element_by_xpath('//*[@id="lowerDiv"]/div[1]/table/tbody/tr[5]/td/div/table/tbody/tr/td[1]/a').click()
time.sleep(5)
print(driver.current_url)

# trump effect
driver.find_element_by_xpath('//*[@id="lowerDiv"]/div[1]/table/tbody/tr[6]/td/div/table/tbody/tr/td/a').click()
time.sleep(5)
print(driver.current_url)

# screener
driver.find_element_by_xpath('//*[@id="lowerDiv"]/div[1]/table/tbody/tr[8]/td/div/table/tbody/tr/td/a').click()
time.sleep(5)
print(driver.current_url)

# news
driver.find_element_by_xpath('//*[@id="lowerDiv"]/div[1]/table/tbody/tr[9]/td/div/table/tbody/tr/td/a').click()
time.sleep(5)
print(driver.current_url)

# calendar
driver.find_element_by_xpath('//*[@id="lowerDiv"]/div[1]/table/tbody/tr[10]/td/div/table/tbody/tr/td/a').click()
time.sleep(5)
print(driver.current_url)

# portfolio
driver.find_element_by_xpath('//*[@id="portfolioButton"]/table/tbody/tr/td/a/span').click()
time.sleep(5)
print(driver.current_url)

# watchlist
driver.find_element_by_xpath('//*[@id="watchlistButton"]/table/tbody/tr/td/a').click()
time.sleep(5)
print(driver.current_url)

# analyzer
driver.find_element_by_xpath('//*[@id="lowerDiv"]/div[1]/table/tbody/tr[13]/td/div/table/tbody/tr/td/a').click()
time.sleep(5)
print(driver.current_url)

# economic data
driver.find_element_by_xpath('//*[@id="economicDataButton"]/table/tbody/tr/td/a').click()
time.sleep(5)
print(driver.current_url)

# etfs
driver.find_element_by_xpath('//*[@id="lowerDiv"]/div[1]/table/tbody/tr[15]/td/div/table/tbody/tr/td/a').click()
time.sleep(5)
print(driver.current_url)

# real time
driver.find_element_by_xpath('//*[@id="lowerDiv"]/div[1]/table/tbody/tr[16]/td/div/table/tbody/tr/td/a').click()
time.sleep(5)
print(driver.current_url)

# alerts
driver.find_element_by_xpath('//*[@id="alertsButton"]/table/tbody/tr/td/a').click()
time.sleep(5)
print(driver.current_url)

# funds
driver.find_element_by_xpath('//*[@id="lowerDiv"]/div[1]/table/tbody/tr[18]/td/div/table/tbody/tr/td/a').click()
time.sleep(5)
print(driver.current_url)

# backtester
driver.find_element_by_xpath('//*[@id="lowerDiv"]/div[1]/table/tbody/tr[7]/td/div/table/tbody/tr/td/a').click()
print(driver.current_url)
time.sleep(10)

driver.close()
driver.quit()