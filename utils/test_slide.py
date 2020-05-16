import os

_right_x_bottom = 800
_right_y_bottom = 1500

_right_x2_bottom = 800
_right_y2_bottom = 1000

_left_x_bottom = 300
_left_y_bottom = 700

_left_x2_bottom = 300
_left_y2_bottom = 300

class TestSlide:
    def __init__(self):
        pass
    def slide_r(self):

        os.popen("adb shell input swipe "+_right_x_bottom+" "+_right_y_bottom+" "+_right_x_bottom+" "+_right_y_bottom)

    def slide_l(self):

        os.popen("adb shell input swipe "+_left_x_bottom+" "+_left_y_bottom+" "+_left_x_bottom+" "+_left_y_bottom)
