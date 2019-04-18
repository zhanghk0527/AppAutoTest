# -*- coding=utf-8 -*-

from AutoTestCommond.AutoTestDev import BrAppWebDriver

class AppMenuPackage(object):
    def __init__(self):
        self.br = BrAppWebDriver().dr

    def Menu_Xiaoxi(self):
        try:
            self.Menu_XiaoxiId = self.br.find_elements_by_id('com.doctor.yy:id/tab_bar')[0]
        except Exception as e:
            assert False, f"底部菜单：未找到‘消息’元素，错误信息为‘{e}’"

        return self.Menu_XiaoxiId

    def Menu_Huanzhe(self):
        try:
            self.Menu_HuanzheId = self.br.find_elements_by_id('com.doctor.yy:id/tab_bar')[1]
        except Exception as e:
            assert False, "底部菜单：未找到‘患者’元素"

        return self.Menu_HuanzheId

    def Menu_Guanli(self):
        try:
            self.Menu_GuanliId = self.br.find_elements_by_id('com.doctor.yy:id/tab_bar')[2]
        except Exception as e:
            assert False, "底部菜单：未找到‘管理’元素"

        return self.Menu_GuanliId

    def Menu_Yaoqing(self):
        try:
            self.Menu_YaoqingId = self.br.find_elements_by_id('com.doctor.yy:id/tab_bar')[3]
        except Exception as e:
            assert False, "底部菜单：未找到‘邀请’元素"

        return self.Menu_YaoqingId

    def Menu_Wode(self):
        try:
            self.Menu_WodeId = self.br.find_elements_by_id('com.doctor.yy:id/tab_bar')[4]
        except Exception as e:
            assert False, "底部菜单：未找到‘我的’元素"

        return self.Menu_WodeId