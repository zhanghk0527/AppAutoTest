# -*- coding=utf-8 -*-

from time import sleep
import unittest
from AutoTestCommond.AutoTestDev import BrAppWebDriver
from AutoTestTools.AutoTestHD import AutoTestHD
from AutoTestPackage.LoginPackage import LoginPackage
from AutoTestTools.Get_toast import Get_toast
from AutoTestPackage.AppMenuPackage import AppMenuPackage
from AutoTestPackage.MyPackage import MyPackage


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 初始化，打开应用，只执行一次
        cls.br = BrAppWebDriver().dr

    def setUp(self):
        pass

    def test_case001(self):
        # 初始化变量Hd
        Hd = 0
        # 循环三次滑动操作，间隔时间为1秒
        for i in range(3):
            Hd = Hd + 1
            sleep(1)
            AutoTestHD().App_Zuohua()

        # 点击立即体验按钮
        sleep(1)
        AutoTestHD().App_Enter().click()

        # 输入用户手机号
        sleep(1)
        LoginPackage().Login_UserNameP().send_keys('13600000015')

        # 输入用户密码
        sleep(1)
        LoginPackage().Login_Password().send_keys('1115454')

        # 点击登录按钮
        sleep(1)
        LoginPackage().Login_LoginBtn().click()

        # 断言：正确手机号，错误密码，点击登录按钮提示：帐号或者密码错误！
        sleep(1)
        toast = Get_toast().Get_toast_text(BrAppWebDriver().dr,'帐号或者密码错误！')
        try:
            self.assertEqual(toast,"帐号或者密码错误！")
            print (f"找到toast元素：{toast}")
        except Exception as e:
            print (f'请检查元素断言内容：{e}')

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # 执行完毕，关闭应用
        cls.br.close_app()

if __name__ == '__main__':
    unittest.main()