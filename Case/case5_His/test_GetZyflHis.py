# # -*- coding:utf-8 -*-
# # 单个用例执行
# # 1、导入模块
# import unittest
# import requests
# import json
# from ddt import ddt, data, file_data, unpack
# from common.readConfig import ReadConfigFile
# from common.setting import file_path
# from common.readWord import duqu
# import urllib3
#
# rc = ReadConfigFile()
# host = rc.read_config("test_host")
# fp = file_path()
#
# # 2、继承自unittest.TestCase类
# @ddt
# class TestCheck(unittest.TestCase):
#     # 3、配置环境：进行测试前的初始化工作
#     def setUp(self):
#         #print('\ncases before')
#         pass
#
#     # 4、定义测试用例，名字以“test”开头
#     @file_data(fp.get_data_path("check.yaml"))
#     def test_check(self,**kwargs):
#         """fees"""
#         caseName = kwargs.get("caseName")
#         payloads = kwargs.get("payloads")
#         expectResult =kwargs.get("expectResult")
#         txt = duqu(payloads)
#
#         print('\033[1;31;40m'+caseName)
#         url = host[0] + "/library/law/check"
#         print(payloads)
#
#         payload = json.dumps({
#             "documentId": "string",
#             "judgeId": 3,
#             "textContent": txt,
#             "paragraphs": [],
#             "rawParagraphs": [
#                 {
#                     "index": 0,
#                     "content": "string"
#                 }
#             ],
#             "sentences": [
#                 "string"
#             ],
#             "caseNumber": {
#                 "orgString": "string",
#                 "year": 0,
#                 "courtCode": "string",
#                 "caseType": "string",
#                 "caseNO": 0
#             },
#             "nationalPersons": [
#                 {
#                     "orgString": "string",
#                     "paragraphIndex": 0,
#                     "name": "string",
#                     "gender": "string",
#                     "birthday": "string",
#                     "address": "string",
#                     "province": "string",
#                     "city": "string",
#                     "addressMode": "string",
#                     "partyType": "string",
#                     "race": "string"
#                 }
#             ]
#         })
#         headers = {
#             'token': 'E925BA9D876E8777453D7277D0F53372221ED2C4DB28964BB5A2E4ECE75EBF33DACA4A65A6F3FCFE9651973A702895AE784601B6DB4434F4B99B5117DD1AE4EE95C560166F34EDF9B1AB967ED23430B746E17FD16A94E659291FEE42DE2238DA3E9FE8C5AF4B4150AD86775FB144C6FFEFCF63B9D0A23AC2FFBC164AB1A30A8E6FC6524983443A8BE0E83E32A014AC41C634667EB8814AC1149A67113ABF0270151FFCB10D747E2E073AFA64FAEBC6D4',
#             'Authorization': 'Bearer E925BA9D876E8777453D7277D0F53372221ED2C4DB28964BB5A2E4ECE75EBF33DACA4A65A6F3FCFE9651973A702895AE784601B6DB4434F4B99B5117DD1AE4EE95C560166F34EDF9B1AB967ED23430B746E17FD16A94E659291FEE42DE2238DA3E9FE8C5AF4B4150AD86775FB144C6FFEFCF63B9D0A23AC2FFBC164AB1A30A8E6FC6524983443A8BE0E83E32A014AC41C634667EB8814AC1149A67113ABF0270151FFCB10D747E2E073AFA64FAEBC6D4',
#             'Content-Type': 'application/json'
#         }
#         urllib3.disable_warnings()
#         response = requests.request("POST", url, headers=headers, data=payload, verify=False)
#         print(json.dumps(response.json(), indent=2).encode('utf-8').decode('unicode_escape'))
#         res = response.json()['totalResults']
#         print("期望返回:" + str(expectResult) + "\n" + "实际返回:" + str(res))
#         self.assertEqual(expectResult,res)
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