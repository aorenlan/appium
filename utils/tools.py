# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import pytest
import logging

class TestTools:
    @pytest.fixture()
    def devices_pools(self):
        print("ads")
