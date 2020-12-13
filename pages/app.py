# from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep

from appium import webdriver

class App:
    driver: webdriver = None
    @classmethod
    def start(self):
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
            sleep(5)
            return self.driver
        except Exception as e:
            raise e

    @classmethod
    def quit(cls):
        try:
            cls.driver.quit()
        except Exception as e:
            print(e)