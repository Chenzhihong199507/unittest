#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#配置文件
TEST_CONFIG =  os.path.join(BASE_DIR,"config", "../config/conf.ini")
# 测试用例模板文件
SOURCE_FILE = os.path.join(BASE_DIR,"datas","cases.xlsx")
# excel测试用例结果文件
TARGET_FILE = os.path.join(BASE_DIR,"report","excelReport","DemoAPITestCase.xlsx")
# 测试用例报告
TEST_REPORT = os.path.join(BASE_DIR,"report")
# 测试用例程序文件
TEST_CASE = os.path.join(BASE_DIR,"Case")
# 测试数据文件
TEST_DATA = os.path.join(BASE_DIR,"datas")

class file_path():
    def get_file_path(self,file=None,fileName=None):
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        target = os.path.join(BASE_DIR,file,fileName)
        return target

    def get_config_path(self,fileName=None):
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        target = os.path.join(BASE_DIR,"config",fileName)
        return target

    def get_case_path(self,fileName=None):
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        target = os.path.join(BASE_DIR,"Case",fileName)
        return target
    def get_data_path(self,fileName=None):
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        target = os.path.join(BASE_DIR,"datas",fileName)
        return target

    def get_report_path(self,fileName=None):
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        target = os.path.join(BASE_DIR,"report",fileName)
        return target

if __name__ == '__main__':
    fp = file_path()
    res = fp.get_file_path("","cases.xlsx")
    print(res)