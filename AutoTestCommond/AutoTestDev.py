# -*- coding=utf-8 -*-

# 导入appium的webdriver类
from appium import webdriver
# 导入单例函数，作用：过滤重复请求，保持同一个通信
from AutoTestTools.AutoTestDL import singleton
from AutoTestTools import PhoneSetting

@singleton
class BrAppWebDriver(object):
    # 初始化方法
    def __init__(self):
        # 定义空字典，并加入设备信息
        desired_caps = {}
        desired_caps['platformName'] = PhoneSetting.platformName
        desired_caps['platformVersion'] = PhoneSetting.platformVersion
        desired_caps['deviceName'] = PhoneSetting.deviceName
        desired_caps['appPackage'] = PhoneSetting.appPackage
        desired_caps['appActivity'] = PhoneSetting.appActivity
        desired_caps['unicodeKeyboard'] = PhoneSetting.unicodeKeyboard
        desired_caps['resetKeyboard'] = PhoneSetting.resetKeyboard
        desired_caps['automationName'] = 'uiautomator2'
        # 使用webdriver与appium创建连接（session）
        self.dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)