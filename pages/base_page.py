import logging
import os
import time
from telnetlib import EC
from time import sleep
# from report.get_log import Logger
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data.read_ini import ReadConfig


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, *loc):  # 查找单个元素
        try:
            WebDriverWait(self.driver, 5, 1).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            print("%s 页面中未找到%s 元素" % (self, loc))

    def find_elements(self, *loc):  # 查找元素组
        try:
            WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except:
            print('页面未找到%s元素' % (loc))

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




    def clear_keys(self, loc):  # 清空输入框
        self.find_element(*loc).clear()

    def send_keys(self, loc, value):  # 清空输入框，查找元素，输入值
        self.clear_keys(loc)
        self.find_element(*loc).send_keys(value)

    def click_button(self, loc):  # 查找元素，点击
        self.find_element(*loc).click()

    def click_buttons(self, loc, n):  # 点击元素组中的一个
        self.find_elements(*loc)[n].click()

    def get_window_size(self):  # 获取屏幕尺寸
        return self.driver.get_window_size()

    def swipe(self, start_x, start_y, end_x, end_y, duration):  # 屏幕滑动
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def alert_accept(self):  # 接受弹窗
        sleep(2)
        return self.driver.switch_to_alert().accept()

    def alert_text(self):  # 获取弹窗文本
        sleep(2)
        return self.driver.switch_to_alert().text

    # 获取屏幕的宽高
    def get_size(self):
        size = self.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    # 向左边滑动
    def swipe_left(self):
        # [100,200]
        x1 = self.get_size()[0] / 10 * 9
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10
        self.swipe(x1, y1, x, y1, 2000)

    # 向右边滑动
    def swipe_right(self):
        # [100,200]
        x1 = self.get_size()[0] / 10
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10 * 9
        self.swipe(x1, y1, x, y1, 2000)

    # 向上滑动
    def swipe_up(self):
        # [100,200]direction
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 9
        y = self.get_size()[1] / 10
        self.swipe(x1, y1, x1, y, 2000)

    # 向下滑动
    def swipe_down(self):
        # [100,200]
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10
        y = self.get_size()[1] / 10 * 9
        self.swipe(x1, y1, x1, y, 2000)

    def get_screenshot(self, screenshot_name):
        now = time.strftime("%Y-%m-%d %H-%M-%S ")
        base_path = os.path.dirname(os.path.dirname(__file__))
        file_path = base_path + "/report/screenshots/" + now + screenshot_name + ".png"
        return self.driver.get_screenshot_as_file(file_path)

    def is_toast_exist(self, driver, text):
        '''is toast exist, return True or False
                    :Agrs:
                     - driver - 传driver
                     - text   - 页面上看到的文本内容
                     - timeout - 最大超时时间，默认30s
                     - poll_frequency  - 间隔查询时间，默认0.5s查询一次
                    :Usage:
                     is_toast_exist(driver, "看到的内容")
                    '''
        try:
            toast_loc = (By.XPATH, ".//*[contains(@text,'%s')]" % text)
            WebDriverWait(self.driver, 20, 0.01).until(EC.presence_of_element_located(toast_loc))
            return True
        except Exception as e:
            print(e)
            return False