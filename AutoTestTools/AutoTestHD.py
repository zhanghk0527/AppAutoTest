# -*- coding=utf-8 -*-

from AutoTestCommond.AutoTestDev import BrAppWebDriver

class AutoTestHD(object):
    def __init__(self):
        self.br = BrAppWebDriver().dr
        # 获取当前屏幕的横向尺寸
        self.x = self.br.get_window_size()['width']
        # 获取当前屏幕的纵向尺寸
        self.y = self.br.get_window_size()['height']

    def App_Zuohua(self):
        # swipe语法：swipe(x0,y0,x1,y1,time),从x0,y0的坐标点，滑动到x1,y1的坐标点，所需时间为n毫秒，1000毫秒等于1秒
        self.App_Zuohuadong = self.br.swipe(self.x*0.9,self.y*0,self.x*0.1,self.y*0,1000)
        return self.App_Zuohuadong

    def App_Youhua(self):
        self.App_Youhuadong = self.br.swipe(self.x*0.1,self.y*0,self.x*0.9,self.y*0,1000)
        return self.App_Youhuadong

    def App_Enter(self):
        try:
            self.App_EnterId = self.br.find_element_by_id('com.doctor.yy:id/iv_enter')
        except Exception as e:
            assert False, "滑动页面：未找到‘立即体验’按钮元素"

        return self.App_EnterId