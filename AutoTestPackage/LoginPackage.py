# -*- coding=utf-8 -*-

from AutoTestCommond.AutoTestDev import BrAppWebDriver

class LoginPackage (object):
    # 初始化方法
    def __init__(self):
       self.Br = BrAppWebDriver().dr

    # 定位元素，并返回，定位当前页面最小元素，只定位，不操作
    # 登录页面，手机号输入框
    def Login_UserNameP(self):
        try:
            self.UserNamePId = self.Br.find_element_by_id('com.doctor.yy:id/et_username')
        except Exception as e:
            assert False, "登录页面：手机号输入框未找到"

        return self.UserNamePId

    # 登录页面，密码输入框
    def Login_Password(self):
        try:
            self.PasswordId = self.Br.find_element_by_id('com.doctor.yy:id/et_password')
        except Exception as e:
            assert False, "登录页面：密码输入框未找到"

        return self.PasswordId

    # 登录页面，登录按钮
    def Login_LoginBtn(self):
        try:
            self.LoginBtnId = self.Br.find_element_by_id('com.doctor.yy:id/btn_login')
        except Exception as e:
            assert False,"登录页面：登录按钮未找到"

        return self.LoginBtnId