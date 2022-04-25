import requests
import json
import unittest
import re
from common.readConfig import ReadConfigFile
from common.setting import file_path
from ddt import ddt, data, file_data, unpack

rc = ReadConfigFile()
host = rc.read_config("test_host")
fp = file_path()

@ddt
class TestCatalog(unittest.TestCase):
  @file_data(fp.get_data_path("catalog.yaml"))
  def test_catalog(self,**kwargs):
    gid = kwargs.get("gid")
    name = kwargs.get("name")
    print("test:"+name)
    url = host[0] + "/library/law/info"
    payload = json.dumps({
      "gid": gid
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    res = response.json()["data"]["fullText"]
    reg = "<div class=\"(s_center|c_zhang)\">目[\\s]?[　]?录</div>"
    match = re.search(reg,res)
    if match:
      if 'Catalog' in res:
        print('\033[1;32;40m'+"sucess")
      # self.assertIn('Catalog',res)
      else:
        print('\033[1;33;40m'+"有目录没有Catalog")
    else:
      print('\033[1;31;40m'+"fail")


if __name__ == '__main__':
    unittest.main()
