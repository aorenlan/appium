# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
import logging
import allure
from driver.driver_config import DriverConfig
from pages.check_pop import CheckPop


class TestDemo:

    def setup(self):
        self.driver = DriverConfig().get_vivo_driver()
        self.check_shucheng_pop = CheckPop().check_shucheng_pop()

    @allure.feature('viptab')
    def test_vip_tab(self):
    #     # 跳过
        print("zxczxc")
        self.check_begin_pop(self.driver)
        self.check_shucheng_pop(self.driver)
        TouchAction(self.driver).tap(x=547, y=1827).perform()
        TouchAction(self.driver).tap(x=125, y=142).perform()

        TouchAction(self.driver).press(x=727, y=328).move_to(x=826, y=459).release().perform()

        TouchAction(self.driver).press(x=775, y=1525).move_to(x=758, y=439).release().perform()

        TouchAction(self.driver).press(x=707, y=1539).move_to(x=698, y=345).release().perform()

        TouchAction(self.driver).tap(x=288, y=134).perform()
        TouchAction(self.driver).press(x=801, y=1587).move_to(x=806, y=425).release().perform()

        TouchAction(self.driver).tap(x=493, y=142).perform()
        TouchAction(self.driver).tap(x=353, y=427).perform()
        TouchAction(self.driver).tap(x=715, y=425).perform()
        TouchAction(self.driver).press(x=786, y=1590).move_to(x=764, y=564).release().perform()

        TouchAction(self.driver).tap(x=641, y=140).perform()



    def check_begin_pop(self,driver):

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

    def click_shucheng(self):
        print(
            "进入书城"
        )
        try:
            if(self.driver.find_element_by_accessibility_id("bookstore_button")):
                self.driver.find_element_by_accessibility_id("bookstore_button").click()
        except Exception:
            logging.info("进入书城失败")

    def teardown(self):
        print("teardown successful")
        self.driver.quit()
