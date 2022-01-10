# # -*- coding:utf-8 -*-
# # 单个用例执行
# # 1、导入模块
# import unittest
# import requests
# import json
# from ddt import ddt, data, file_data, unpack
# from common.readConfig import ReadConfigFile
# from common.setting import file_path
#
# rc = ReadConfigFile()
# host = rc.read_config("test_host")
# fp = file_path()
#
# # 2、继承自unittest.TestCase类
# @ddt
# class TestSensWord(unittest.TestCase):
#     # 3、配置环境：进行测试前的初始化工作
#     def setUp(self):
#         #print('\ncases before')
#         pass
#
#     # 4、定义测试用例，名字以“test”开头
#     @file_data(fp.get_data_path("sensWordDetect.yaml"))
#     def test_sensWord(self,**kwargs):
#         """sensWordDetect"""
#         caseName = kwargs.get("caseName")
#         payloads = kwargs.get("payloads")
#         expectResult =kwargs.get("expectResult")
#
#         print(caseName)
#         print(payloads)
#         url = host[0] + "/Judgements/SensitiveDetect"
#
#         headers = {
#             'Content-Type': 'application/json'
#         }
#         response = requests.post(url,json.dumps(payloads),headers=headers,verify=False)
#         try:
#             res = response.json()["detections"][0]["corrections"][0]
#             print("期望返回:" + str(expectResult) + "\n" + "实际返回:" + str(res))
#             self.assertEqual(expectResult,res)
#
#         except:
#             res = response.json()["detections"]
#             print("期望返回:" + str(expectResult) + "\n" + "实际返回:" + str(res))
#             self.assertEqual(expectResult,res)
#
#
#     # 6、清理环境
#     def tearDown(self):
#         #print('case after')
#         pass
#
#
# # 7、该方法会搜索该模块下所有以test开头的测试用例方法,并自动执行它们
# if __name__ == '__main__':
#     unittest.main()