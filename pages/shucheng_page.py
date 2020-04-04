# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep
from selenium.webdriver.android.webdriver import WebDriver
from data.read_ini import ReadConfig

from driver.driver_config import DriverConfig
class CheckPop:
    def __int__(self,driver: WebDriver):
        self.driver = driver

    def close_shucheng_pop(self):
        self.pop_dict = ReadConfig().get_pop("pop_dict")
        sleep(5)
        for every_pop_key, every_pop_value in eval(self.pop_dict).items():
            try:
                print("key" + every_pop_key, "value" + every_pop_value)
                if (self.driver.find_element_by_id(every_pop_key)):
                    self.driver.find_element_by_id(every_pop_key).click()
                    print("成功关闭弹窗" + every_pop_value)
                    break
                else:
                    continue
            except Exception as e:
                print(e)


if __name__ == '__main__':
    CheckPop().check_shucheng_pop()