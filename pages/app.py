# from selenium.webdriver.remote.webdriver import WebDriver
from appium import webdriver

class App:
    driver: webdriver = None
    @classmethod
    def start(cls):
        try:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "SJE7N17522001140"
            caps["appPackage"] = "com.chaozh.iReaderFree"
            caps["appActivity"] = "com.chaozh.iReader.ui.activity.WelcomeActivity"
            caps["automationName"] = "uiautomator2"
            caps["platformVersion"] = "9.0"
            caps["noReset"] = "true"
            caps["autoGrantPermissions"] = "true"
            cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            print("setup successful")
            return cls.driver
        except Exception as e:
            raise e

    @classmethod
    def quit(cls):
        try:
            cls.driver.quit()
        except Exception as e:
            print(e)