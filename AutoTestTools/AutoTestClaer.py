# -*- coding=utf-8 -*-

from AutoTestCommond.AutoTestDev import BrAppWebDriver

class AutoTestClaer(object):

    def __init__(self):
       self.br = BrAppWebDriver().dr

    # 键码：123 对应的键码为“光标移动到末尾”
    def TestAppCode123(self):
       self.TestAppCode123 = self.br.keyevent(123)
       return self.TestAppCode123

    # 键码：29，28672 对应的键码为“Ctrl+A”的组合键
    def TestAppCodeAll(self):
        self.TestAppCodeAll = self.br.keyevent(29,28672)
        return self.TestAppCodeAll

    # 键码：112 对应的键码为“删除键”操作
    def TestAppCodeDel(self):
        self.TestAppCodeDel = self.br.keyevent(112)
        return self.TestAppCodeDel