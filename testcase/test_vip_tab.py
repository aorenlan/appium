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
from pages.shucheng_page import ShuengPage


class TestDemo:

    def setup(self):
        self.driver = App.start()
        self.base = BasePage(self.driver)
        # self.shucheng = ShuengPage(self.driver)

    @allure.feature('viptab')
    def test_vip_tab(self):
    #     # 跳过
        print("zxczxc")
        self.base.check_begin_pop()
        self.base.handld_exception()
        TouchAction(self.driver).tap(x=547, y=1827).perform()
        TouchAction(self.driver).tap(x=125, y=142).perform()

        TouchAction(self.driver).press(x=727, y=328).move_to(x=826, y=459).release().perform()

        TouchAction(self.driver).press(x=775, y=1525).move_to(x=758, y=439).release().perform()

        TouchAction(self.driver).press(x=707, y=1539).move_to(x=698, y=345).release().perform()

        TouchAction(self.driver).tap(x=288, y=134).perform()
        TouchAction(self.driver).press(x=801, y=1587).move_to(x=806, y=425).release().perform()

        TouchAction(self.driver).tap(x=493, y=142).perform()
        TouchAction(self.driver).tap(x=353, y=427).perform()
        TouchAction(self.driver).tap(x=715, y=425).perform()
        TouchAction(self.driver).press(x=786, y=1590).move_to(x=764, y=564).release().perform()

        TouchAction(self.driver).tap(x=641, y=140).perform()







    def teardown(self):

        App.quit()
