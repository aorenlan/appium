import logging
from time import sleep
from report.get_log import Logger
from selenium.webdriver.android.webdriver import WebDriver
from data.read_ini import ReadConfig


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.log = Logger('all.log', level='info')
        # log.logger.debug('debug')

    def find_element(self, locator):
        print(locator)
        try:
            return self.driver.find_element(*locator)
        except:
            self.handle_exception()
            # self.find_element(locator)
            return self.driver.find_element(*locator)

    def find_element_and_click(self, locator):
        print("click")
        try:
            # 如果click也有异常，可以这样处理
            self.find_element(locator).click()
        except:
            self.handle_exception()
            self.find_element(locator).click()

    def handld_exception(self):
        self.pop_dict = ReadConfig().get_pop("pop_dict")
        sleep(1)
        self.driver.implicitly_wait(0)
        # pageSource()
        for every_pop_key, every_pop_value in eval(self.pop_dict).items():
            sleep(1)
            try:
                print("key:" + every_pop_key, "value:" + every_pop_value)
                if self.driver.find_element_by_id(every_pop_key):
                    self.driver.find_element_by_id(every_pop_key).click()
                    print("成功关闭弹窗" + every_pop_value)
                    break
                elif self.driver.find_element_by_accessibility_id(every_pop_key):
                    print("点击关闭")
                else:
                    continue
            except Exception as e:
                print("未找到:" + every_pop_value)
                self.log.logger.debug("未找到"+every_pop_value)
        self.driver.implicitly_wait(1)

    def jump(self):
        print("jump")

    def get_devices_info(self):
        get_devices = "adb deviecs"
        get_android = "adb shell getprop ro.build.version.release"

    def check_begin_pop(self):

        try:
        # 我已阅读并同意
            if (self.driver.find_element_by_id("android:id/button1")):
                self.driver.find_element_by_id("android:id/button1").click()
            sleep(7)
            # 判断是否有跳过按钮
            if (self.driver.find_element_by_id("com.chaozh.iReaderFree:id/menu_preference_jump_id")):
                self.driver.find_element_by_id("com.chaozh.iReaderFree:id/menu_preference_jump_id").click()
                sleep(7)
        except Exception:
            logging.info("打开APP失败")

    def check_jump(self):

        try:
            for i in range(3):

                if (self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '跳过')]")):
                    self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '跳过')]").click()
                    print("成功关闭开屏幕广告")
                else:
                    print("未找到开屏广告")
                    continue
                sleep(0.5)

        except Exception:
            logging.info("跳过广告失败")

