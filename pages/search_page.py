# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from selenium.webdriver.common.by import By

from driver.driver_config import DriverConfig
from pages.base_page import BasePage


class SearchPage(BasePage):
    def search_content(self, content):
        sleep(2)
        print(
            "输入"+str(content)
        )
        try:
            if (self.driver.find_element_by_id("com.zhangyue.iReader.search:id/edit_text_view")):
                self.driver.find_element_by_id("com.zhangyue.iReader.search:id/edit_text_view").send_keys(content)
                sleep(2)
        except Exception as e:
            print("输入失败:" + str(e))
