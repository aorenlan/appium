# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep
from selenium.webdriver.android.webdriver import WebDriver
from data.read_ini import ReadConfig

from driver.driver_config import DriverConfig


class ShuengPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def tab_search(self):
        print(
            "点击搜索"
        )
        try:
            if(self.driver.find_element_by_id("com.zhangyue.iReader.bookStore:id/id_search_bar_input")):
                self.driver.find_element_by_id("com.zhangyue.iReader.bookStore:id/id_search_bar_input").click()
        except Exception as e:
            print("点击搜索失败:"+e)

        print(
            "输入斗罗大陆"
        )
        try:
            if (self.driver.find_element_by_id("com.zhangyue.iReader.search:id/edit_text_view")):
                self.driver.find_element_by_id("com.zhangyue.iReader.search:id/edit_text_view").send_keys("斗罗大陆")
        except Exception as e:
            print("输入失败:" + e)



        pass

    def click_shucheng(self):
        print(
            "进入书城"
        )
        try:
            if(self.driver.find_element_by_accessibility_id("bookstore_button")):
                self.driver.find_element_by_accessibility_id("bookstore_button").click()
        except Exception as e:
            print("进入书城失败:"+e)


if __name__ == '__main__':
    pass
