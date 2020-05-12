# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
import logging
import allure
from driver.driver_config import DriverConfig
from pages.app import App
from pages.base_page import BasePage
from pages.search_page import SearchPage
from pages.shucheng_page import ShuengPage


class TestDemo:

    def setup(self):
        self.driver = App.start()
        self.base = BasePage(self.driver)
        self.shucheng = ShuengPage(self.driver)
        self.search = SearchPage(self.driver)

    @allure.feature('viptab')
    def test_vip_tab(self):
    #     # 跳过
        print("zxczxc")
        self.base.check_jump()
        self.base.check_begin_pop()
        self.base.handld_exception()
        self.shucheng.click_shucheng()
        self.base.handld_exception()
        self.shucheng.tab_search()
        self.search.search_content("绝世武魂")

    def teardown(self):

        App.quit()
