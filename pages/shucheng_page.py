# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from _pytest import logging
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from data.read_ini import ReadConfig

from driver.driver_config import DriverConfig
from pages.base_page import BasePage

_agree = ("BY.ID", "android:id/button1")
_jump = ("BY.ID", "com.chaozh.iReaderFree:id/menu_preference_jump_id")
_jump = ("BY.ID", "com.chaozh.iReaderFree:id/menu_preference_jump_id")


class ShuchengPage(BasePage):


    def __int__(self, driver: WebDriver):
        self.driver = driver


    def check_begin_pop(self):

        try:
            # 我已阅读并同意
            if self.find_element(_agree):
                self.click_button(_agree)
            # 判断是否有跳过按钮
            if self.find_element(_jump):
                self.click_button(_jump)
            # WebDriverWait(self.driver,5).until(lambda driver: self.find_element(_shucheng_tab))
        except Exception as e:
            logging.info("打开APP失败")

    def click_shucheng(self):
        print(
            "进入书城"
        )
        try:
            if self.driver.find_element_by_accessibility_id("bookstore_button"):
                self.driver.find_element_by_accessibility_id("bookstore_button").click()
        except Exception as e:
            logging.info("进入书城失败" + e)

    def tab_bottom(self):
        print("点击底部tab")
        self.driver.find_element_by_xpath("//android.view.View[@content-desc='bookstore_button']").click()
        sleep(2)
        self.driver.find_element_by_xpath("//android.view.View[@content-desc='vip_button']").click()
        sleep(2)
        self.driver.find_element_by_xpath("//android.view.View[@content-desc='listenbook_button']").click()



if __name__ == '__main__':
    # CheckPop().check_shucheng_pop()
    pass
