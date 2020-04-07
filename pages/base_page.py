from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver

from data.read_ini import ReadConfig


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self,*args):
        self.driver.find_element(args)

    def handld_exception(self):
        self.pop_dict = ReadConfig().get_pop("pop_dict")
        sleep(5)
        pageSource()
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

    def jump(self):
        print("jump")

    def get_devices_info(self):
        get_devices = "adb deviecs"
        get_android = "adb shell getprop ro.build.version.release"