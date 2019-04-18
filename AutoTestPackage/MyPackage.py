# -*- coding=utf-8 -*-

from AutoTestCommond.AutoTestDev import BrAppWebDriver

class MyPackage(object):
    def __init__(self):
        self.br = BrAppWebDriver().dr

    def My_Xinxi(self):
        try:
            self.My_XinxiClass = self.br.find_elements_by_class_name('android.widget.RelativeLayout')[0]
        except Exception as e:
            assert False, "我的页面：未找到‘个人信息’元素"

        return self.My_XinxiClass

    def My_Renzheng(self):
        try:
            self.My_RenzhengClass = self.br.find_elements_by_class_name('android.widget.RelativeLayout')[1]
        except Exception as e:
            assert False, "我的页面：未找到‘资质认证’元素"

        return self.My_RenzhengClass

    def My_Anquan(self):
        try:
            self.My_AnquanClass = self.br.find_elements_by_class_name('android.widget.RelativeLayout')[2]
        except Exception as e:
            assert False, "我的页面：未找到‘安全设置’元素"

        return self.My_AnquanClass

    def My_Bangzhu(self):
        try:
            self.My_BangzhuClass = self.br.find_elements_by_class_name('android.widget.RelativeLayout')[3]
        except Exception as e:
            assert False, "我的页面：未找到‘帮助’元素"

        return self.My_BangzhuClass

    def My_Fankui(self):
        try:
            self.My_FankuiClass = self.br.find_elements_by_class_name('android.widget.RelativeLayout')[4]
        except Exception as e:
            assert False, "我的页面：未找到‘反馈’元素"

        return self.My_FankuiClass

    def My_Kefu(self):
        try:
            self.My_KefuClass = self.br.find_elements_by_class_name('android.widget.RelativeLayout')[5]
        except Exception as e:
            assert False, "我的页面：未找到‘客服’元素"

        return self.My_KefuClass

    def My_Guanyu(self):
        try:
            self.My_GuanyuClass = self.br.find_elements_by_class_name('android.widget.RelativeLayout')[6]
        except Exception as e:
            assert False, "我的页面：未找到‘关于’元素"

        return self.My_GuanyuClass