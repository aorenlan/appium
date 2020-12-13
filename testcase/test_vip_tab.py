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

from pages.slide_page import SlidePage


class TestDemo:

    def setup(self):
        self.driver = App.start()
        self.base = BasePage(self.driver)
        self.slide = SlidePage(self.driver)

    @allure.feature('viptab')
    def test_vip_tab(self):
    #     # 跳过
        print("zxczxc")
        self.slide.check_rules()

        self.slide.check_endtime()

    def teardown(self):

        App.quit()
