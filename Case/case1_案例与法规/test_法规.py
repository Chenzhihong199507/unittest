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
#
# # 通过yaml文件读取数据
# # wryaml = WRYaml()
# # ym = wryaml.read_yaml('D:\\Projects\\PycharmProjects\\unittest\\datas\\CaseInfo.yaml')
#
# # 2、继承自unittest.TestCase类
# @ddt
# class TestLawInfo(unittest.TestCase):
#     # 3、配置环境：进行测试前的初始化工作
#     def setUp(self):
#         # print('\ncases before')
#         pass
#
#     # 4、定义测试用例，名字以“test”开头
#     @file_data(fp.get_data_path("Laws.yaml"))
#     def test_Laws(self, **kwargs):
#         """法规查询结果接口"""
#         caseName = kwargs.get("caseName")
#         payloads = kwargs.get("payloads")
#         expectResult = kwargs.get("expectResult")
#         expectResult2 = kwargs.get("expectResult2")
#
#         print(caseName)
#         url = host[0] + "/library/laws"
#
#         headers = {
#             'Content-Type': 'application/json'
#         }
#         response = requests.post(url, json.dumps(payloads), headers=headers, verify=False)
#         res = response.json()
#         print("期望返回1:" + str(expectResult) + "\n" + "实际返回1:" + str(res["totalResults"]))
#         print("期望返回2:" + str(expectResult2) + "\n" + "实际返回2:" + str(len(res["data"])))
#         self.assertGreaterEqual(res["totalResults"], expectResult)
#         self.assertEqual(len(res["data"]), expectResult2)
#
#     @file_data("D:\\Projects\\PycharmProjects\\unittest\\datas\\LawInfo.yaml")
#     def test_LawInfo(self, **kwargs):
#         """法规详情接口"""
#         caseName = kwargs.get("caseName")
#         payloads = kwargs.get("payloads")
#         expectResult = kwargs.get("expectResult")
#
#         print(caseName)
#         url = host[0] + "/library/law/info"
#
#         headers = {
#             'Content-Type': 'application/json'
#         }
#         response = requests.post(url, json.dumps(payloads), headers=headers, verify=False)
#         res = response.json()["data"]["lawInfoSchema"]["chapters"]
#         print("期望返回:" + str(expectResult) + "\n" + "实际返回:" + str(len(res)))
#         self.assertEqual(len(res), expectResult)
#
#     # 6、清理环境
#     def tearDown(self):
#         # print('case after')
#         pass
#
#
# # 7、该方法会搜索该模块下所有以test开头的测试用例方法,并自动执行它们
# if __name__ == '__main__':
#     unittest.main()
