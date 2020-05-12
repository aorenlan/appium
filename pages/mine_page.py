# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from selenium.webdriver.common.by import By

from driver.driver_config import DriverConfig
from pages.base_page import BasePage


class MinePage(BasePage):
    def login_vip(self):
        if(self.driver.find_element_by_accessibility_id("mine_button")):
            self.driver.find_element_by_accessibility_id("mine_button").click()
            if(self.driver.find_element_by_id("com.zhangyue.iReader.mine:id/mine_head_title").getText()=="点击登录"):
                print("用户未登录")


        #         self.driver.find_element_by_id("com.zhangyue.iReader.mine:id/mine_head_title").click()
        #
        # el4 = self.driver.find_element_by_id("com.chaozh.iReaderFree:id/account_main_switchlogintype")
        # el4.click()
        # el5 = self.driver.find_element_by_xpath(
        #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.EditText")
        # el5.send_keys("123")
        # el6 = self.driver.find_element_by_xpath(
        #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.EditText")
        # el6.click()
        # el6.send_keys("123")
        # el7 = self.driver.find_element_by_id("com.chaozh.iReaderFree:id/account_block_phonenum_login_submit")
        # el7.click()
        if(self.driver.find_element_by_android_uiautomator('new UiSelector().text("点击登录)')):
            print("用户未登录")

    def login_svip(self):
        login_menu = ""
        self.driver.find_element(By.ID,login_menu)
        print()
