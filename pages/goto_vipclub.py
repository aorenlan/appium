# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from driver.driver_config import DriverConfig

class TabChange:
    def __init__(self):
        self.driver = DriverConfig.get_vivo_driver()
    # def go_vipclub(self):
    #     # if(new UiSelector()):
    #     #     self.driver.find_element_by_id("com.chaozh.iReader:id/sign_tip").click()
