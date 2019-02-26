# Webstation - Crossbrowser Smoke Test => 2. Navigation Icons

import time
from selenium import webdriver
from webstation.base.selenium_webdriver import SeleniumDriver


class NavigationPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators:

        # html elements on the navigation page:

        markets_button_xpath        =       '//*[@id="lowerDiv"]/div[1]/table/tbody/tr[1]/td/div/table/tbody/tr/td[1]/a'
        _currencies_button_xpath    =       '//*[@id="lowerDiv"]/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr/td[1]/a'
        _commodities_button_spath   =       '//*[@id="lowerDiv"]/div[1]/table/tbody/tr[3]/td/div/table/tbody/tr/td[1]/a'
        _fixed_button_xpath         =       '//*[@id="fixedIncomeButton"]/table/tbody/tr/td[1]/a'
        _futures_button_xpath       =       '//*[@id="lowerDiv"]/div[1]/table/tbody/tr[5]/td/div/table/tbody/tr/td[1]/a'
        _trump_button_xpath         =       '//*[@id="lowerDiv"]/div[1]/table/tbody/tr[6]/td/div/table/tbody/tr/td/a'
        # backtester will be added at the end!
        _screener_button_xpath      =       '//*[@id="lowerDiv"]/div[1]/table/tbody/tr[8]/td/div/table/tbody/tr/td/a'
        _news_button_xpath          =       '//*[@id="lowerDiv"]/div[1]/table/tbody/tr[9]/td/div/table/tbody/tr/td/a'
        _calendar_button_xpath      =       '//*[@id="lowerDiv"]/div[1]/table/tbody/tr[10]/td/div/table/tbody/tr/td/a'
        _portfolio_button_xpath     =       '//*[@id="portfolioButton"]/table/tbody/tr/td/a/span'
        _watchlist_button_xpath     =       '//*[@id="watchlistButton"]/table/tbody/tr/td/a'
        _analyzer_button_xpath      =       '//*[@id="lowerDiv"]/div[1]/table/tbody/tr[13]/td/div/table/tbody/tr/td/a'
        _economicdata_button_xpath  =       '//*[@id="economicDataButton"]/table/tbody/tr/td/a'
        _etfs_button_xpath          =       '//*[@id="lowerDiv"]/div[1]/table/tbody/tr[15]/td/div/table/tbody/tr/td/a'
        _realtime_button_xpath      =       '//*[@id="lowerDiv"]/div[1]/table/tbody/tr[16]/td/div/table/tbody/tr/td/a'
        _alerts_button_xpath        =       '//*[@id="alertsButton"]/table/tbody/tr/td/a'
        _funds_button_xpath         =       '//*[@id="lowerDiv"]/div[1]/table/tbody/tr[18]/td/div/table/tbody/tr/td/a'
        _backtester_button_xpath    =       '//*[@id="lowerDiv"]/div[1]/table/tbody/tr[7]/td/div/table/tbody/tr/td/a'

    def clickMarkets(self):
        self.elementClick(self.
        time.sleep(3)

    def clcikCurrencies(self):
        self.elementClick(self._currencies_button_xpath, locatorType='xpath')

    # def fixed_income(self):
    #     self.driver.find_element_by_xpath(self.fixed_button_xpath).click()
    #
    # def futures(self):
    #     self.driver.find_element_by_xpath(self.futures_button_xpath).click()
    #
    # def trump(self):
    #     self.driver.find_element_by_xpath(self.trump_button_xpath).click()
    #
    # def screener(self):
    #     self.driver.find_element_by_xpath(self.screener_button_xpath).click()
    #
    # def news(self):
    #     self.driver.find_element_by_xpath(self.news_button_xpath).click()
    #
    # def calendar(self):
    #     self.driver.find_element_by_xpath(self.calendar_button_xpath).click()
    #
    # def portfolio(self):
    #     self.driver.find_element_by_xpath(self.portfolio_button_xpath).click()
    #
    # def watchlist(self):
    #     self.driver.find_element_by_xpath(self.watchlist_button_xpath).click()
    #
    # def analyzer(self):
    #     self.driver.find_element_by_xpath(self.analyzer_button_xpath).click()
    #
    # def ec_data(self):
    #     self.driver.find_element_by_xpath(self.economicdata_button_xpath).click()
    #
    # def etfs(self):
    #     self.driver.find_element_by_xpath(self.etfs_button_xpath).click()
    #
    # def real_time(self):
    #     self.driver.find_element_by_xpath(self.realtime_button_xpath).click()
    #
    # def alerts(self):
    #     self.driver.find_element_by_xpath(self.alerts_button_xpath).click()
    #
    # def funds(self):
    #     self.driver.find_element_by_xpath(self.markets_button_xpath).click()
    #
    # def alerts(self):
    #     self.driver.find_element_by_xpath(self.alerts_button_xpath).click()
    #
    # def backtester(self):
    #     self.driver.find_element_by_xpath(self.backtester_button_xpath).click()









