# -*- coding=utf-8 -*-

# ————————————————————————————————————————————————————— 封装toast元素定位方法 ————————————————————————————————————————————————————— #

# 导入 WebDrivierWait 方法
from selenium.webdriver.support.ui import WebDriverWait
# 导入support的expected_conditions模块，用来判断元素是否存在
from selenium.webdriver.support import expected_conditions as EC
# 导入By方法
from selenium.webdriver.common.by import By

class Get_toast(object):
    # 定义Get_toast_text方法，参数为：driver,toast_text
    # —— driver：接收传递的webdriver
    # —— toast_text：接收传递的toast内容

    def Get_toast_text(self,driver,toast_text):
        # 添加错误处理机制，判断是否找到相应的toast元素
        # 如找到相应toast元素，便返回toast元素文本内容
        try:
            # 自定义查找元素内容的方法，也可叫做定位器
            toast_element = (By.XPATH, f".//*[contains(@text,'{toast_text}')]")

            # EC：expected_conditions的缩写或叫变量，判断当前页面是否存在定位的元素，locator是定位器
            # 官方文档提供的方法为：class selenium.webdriver.support.expected_conditions.presence_of_element_located(locator)

            # WebDriverWait的两种方式：
            # —— 当元素出现时，条件成立，继续执行：
            #    —— until：WebDriverWait(driver=webdriver, timeout=超时时间, poll_frequency=调用频率, ignored_exceptions=忽略异常).until(self,可执行方法,异常信息)
            #
            # —— 当元素消失时，条件成立，继续执行：
            #    —— until_not：WebDriverWait(driver=webdriver, timeout=超时时间, poll_frequency=调用频率, ignored_exceptions=忽略异常).until(self,可执行方法,异常信息)

            toast = WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located(toast_element))

            # 返回toast内容
            return toast.text
        # 如未找到相应toast元素，打印错误信息
        except Exception as e:
            print (f"当前页面toast元素未找到！错误为：{e}")