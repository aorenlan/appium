# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep
from selenium.webdriver.android.webdriver import WebDriver
from data.read_ini import ReadConfig

from driver.driver_config import DriverConfig


class ShuengPage:
    def __int__(self, driver: WebDriver):
        self.driver = driver

    def tab_search(self):
        pass


if __name__ == '__main__':
    CheckPop().check_shucheng_pop()
