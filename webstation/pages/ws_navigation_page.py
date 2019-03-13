# Webstation - Crossbrowser Smoke Test => 2. Navigation Icons

import time
from selenium import webdriver
from webstation.base.selenium_webdriver import SeleniumDriver


class NavigationPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # buttons in the navigation bar :

    _markets_button_xpath        =       '//*[@id="lowerDiv"]/div[1]/table/tbody/tr[1]/td/div/table/tbody/tr/td[1]/a'
    _currencies_button_xpath    =       '//*[@id="lowerDiv"]/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr/td[1]/a'
    _commodities_button_spath   =       '//*[@id="lowerDiv"]/div[1]/table/tbody/tr[3]/td/div/table/tbody/tr/td[1]/a'
    _fixedIncome_button_xpath         =       '//*[@id="fixedIncomeButton"]/table/tbody/tr/td[1]/a'
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

    # elements on pages:
    _markets_header_css         = ".main-pages-header.markets"
    _currencies_header_css      = ".main-pages-header.currencies"
    _commodities_header         = ".main-pages-header.commodities"
    _fixedIncome_header         = ".main-pages-header.fixedIncome"
    _futures_header             = ".main-pages-header.futures"
    _funds_header               = ".main-pages-header.funds"
    _news_header                = ".main-pages-header.news-header"
    _calendar_header            = ".main-pages-header.companyCalendar"
    _analyzer_header            = ".main-pages-header.analyzerHeader"
    _portfolio_header           = ".main-pages-header.portfolio"
    _watchlist_header           = ".main-pages-header.watchlist"
    _alert_header               = ".main-pages-header.alerts"
    _personal_page_header       = ".main-pages-header.personal-pages"
    _trump_effect_header        = ".main-pages-header.trumpEfect"
    _economic_data_header       = ".main-pages-header.economicCalendar"
    _back_tester_header         = ".backtester-header.back-tester"
    _screener_header            = ".main-pages-header.screenerHeader"
    _etf_header                 = ".main-pages-header.etf"
    _real_time_header           = ".main-pages-header.realtimeIn"

    def clickMarkets(self):
        self.elementClick(self._markets_button_xpath, locatorType='xpath')
        self.isElementPresent(self._markets_header_css)
        print(self.driver.current_url)

    def clickCurrencies(self):
        self.elementClick(self._currencies_button_xpath, locatorType='xpath')
        self.isElementPresent(self._currencies_header_css)
        print(self.driver.current_url)
        # time.sleep(5)

    def clickCommodities(self):
        self.elementClick(self._commodities_button_spath, locatorType='xpath')
        self.isElementPresent(self._commodities_header)
        print(self.driver.current_url)

    def clickFixedIncome(self):
        self.elementClick(self._fixedIncome_button_xpath, locatorType='xpath')
        self.isElementPresent(self._fixedIncome_header)
        print(self.driver.current_url)

    def clickFutures(self):
        self.elementClick(self._futures_button_xpath, locatorType='xpath')
        self.isElementPresent(self._futures_header)
        print(self.driver.current_url)

    def clickTrumpEffect(self):
        self.elementClick(self._trump_button_xpath, locatorType='xpath')
        self.isElementPresent(self._trump_effect_header)
        print(self.driver.current_url)

    def clickScreener(self):
        self.elementClick(self._screener_button_xpath, locatorType='xpath')
        self.isElementPresent(self._screener_header)
        print(self.driver.current_url)

    def clickNews(self):
        self.elementClick(self._news_button_xpath, locatorType='xpath')
        self.isElementPresent(self._news_header)
        print(self.driver.current_url)

    def clickCalendar(self):
        self.elementClick(self._calendar_button_xpath, locatorType='xpath')
        self.isElementPresent(self._calendar_header)
        print(self.driver.current_url)

    def clickPortfolio(self):
        self.elementClick(self._portfolio_button_xpath, locatorType='xpath')
        self.isElementPresent(self._portfolio_header)
        print(self.driver.current_url)

    def clickWatchlist(self):
        self.elementClick(self._watchlist_button_xpath, locatorType='xpath')
        self.isElementPresent(self._watchlist_header)
        print(self.driver.current_url)

    def clickAnalyzer(self):
        self.elementClick(self._analyzer_button_xpath, locatorType='xpath')
        self.isElementPresent(self._alert_header)
        print(self.driver.current_url)

    def clickEconomicData(self):
        self.elementClick(self._economicdata_button_xpath, locatorType='xpath')
        self.isElementPresent(self._economic_data_header)
        print(self.driver.current_url)

    def clickEtfs(self):
        self.elementClick(self._etfs_button_xpath, locatorType='xpath')
        self.isElementPresent(self._etf_header)
        print(self.driver.current_url)

    def clickRealTime(self):
        self.elementClick(self._realtime_button_xpath, locatorType='xpath')
        self.isElementPresent(self._real_time_header)
        print(self.driver.current_url)

    def clickAlerts(self):
        self.elementClick(self._alerts_button_xpath, locatorType='xpath')
        self.isElementPresent(self._alert_header)
        print(self.driver.current_url)

    def clickFunds(self):
        self.elementClick(self._funds_button_xpath, locatorType='xpath')
        self.isElementPresent(self._funds_header)
        print(self.driver.current_url)

    def clickBacktester(self):
        self.elementClick(self._backtester_button_xpath, locatorType='xpath')
        self.isElementPresent(self._back_tester_header)
        print(self.driver.current_url)
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









