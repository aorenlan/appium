# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import os
import random
from time import sleep

from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

_right_x_bottom = 800
_right_y_bottom = 1500

_right_x2_bottom = 800
_right_y2_bottom = 1000

_left_x_bottom = 300
_left_y_bottom = 700

_left_x2_bottom = 300
_left_y2_bottom = 300

class SlidePage():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        pass

    def check_endtime(self):

        os.popen("adb shell input tap 500 900")
        if (self.driver.find_element((By.ID,"com.kuaishou.nebula:id/player_duration"))):
            end = self.driver.find_element((By.ID, "com.kuaishou.nebula:id/player_duration")).gettext()
            print(end)
        else:
            print("短视频")
            self.slide_10()

    def slide_10(self):
        r_time = random.randint(20,30)
        sleep(r_time)
        self.swipe_up()

    def check_rules(self):

        if(self.driver.find_elements_by_id("__SVG_SPRITE_NODE__")):
            sleep(1)
            print("在任务页面")
            os.popen("adb shell input keyevent 4")

def slide_test():
        r_time = random.randint(10, 30)
        r = random.randint(1,2)
        print("model "+str(r))
        print(r_time)
        sleep(r_time)
        if r == 1:
            print("adb shell input swipe " + str(_left_x_bottom) + " " + str(_left_y_bottom) + " " + str(
                _left_x2_bottom) + " " + str(_left_y2_bottom))
            os.popen(
                "adb shell input swipe " + str(_left_x_bottom) + " " + str(_left_y_bottom) + " " + str(
                    _left_x2_bottom) + " " + str(_left_y2_bottom))
        else:
            print("adb shell input swipe " + str(_right_x_bottom) + " " + str(_right_y_bottom) + " " + str(
                _right_x2_bottom) + " " + str(_right_y2_bottom))
            os.popen("adb shell input swipe " + str(_right_x_bottom) + " " + str(_right_y_bottom) + " " + str(
                _right_x2_bottom) + " " + str(_right_y2_bottom))

def wuba_rukou_6():
    os.popen("adb shell input tap 880 1323")

def wuba_6():
    sleep(40)
    os.popen("adb shell input tap 969 111")
    sleep(5)
    os.popen("adb shell input tap 746 1252")
    sleep(5)

def wuba_renwu():
    os.popen("adb shell input tap 807 448")

def wuba_renwu_xunhuan():
    sleep(40)
    os.popen("adb shell input tap 969 111")
    sleep(5)
    # os.popen("adb shell input tap 746 1252")
    sleep(5)

if __name__ == "__main__":
    # a = SlidePage()

    for i in range(500):
        slide_test()

    # wuba_rukou_6()
    # for i in range(4):
    #     print(i)
    #     wuba_6()

    # wuba_renwu()
    # for i in range(6):
    #     print(i)
    #     wuba_renwu_xunhuan()