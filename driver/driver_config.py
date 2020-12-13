# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep
from appium import webdriver

class DriverConfig:
    def __int__(self):
        pass

    def get_ks_driver(self):
        try:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "SJE7N17522001140"
            caps["appPackage"] = "com.kuaishou.nebula"
            caps["appActivity"] = "com.yxcorp.gifshow.HomeActivity"
            caps["automationName"] = "uiautomator2"
            caps["platformVersion"] = "9.0"
            caps["noReset"] = "true"
            caps["autoGrantPermissions"] = "true"
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            print("setup successful")
            return self.driver
        except Exception as e:
            raise e
