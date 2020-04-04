# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from driver.driver_config import DriverConfig
from pages.base_page import BasePage


class VipPage(BasePage):
    def __init__(self):

        pass

    def jump(self):
        super().jump()
        print("son jump")

if __name__ == "__main__":
    VipPage().jump()