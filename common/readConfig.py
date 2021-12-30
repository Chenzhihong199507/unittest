from configparser import ConfigParser
import os

class ReadConfigFile(object):
    def read_config(self,para):
        conn = ConfigParser()
        #file_path = os.path.join(os.path.abspath('.'),path)
        file_path = "D:\\Projects\\PycharmProjects\\unittest\\config\\conf.ini"
        if not os.path.exists(file_path):
            raise FileNotFoundError("文件不存在")

        conn.read(file_path)
        host = conn.get('conf',para)

        return [host]
#
rc = ReadConfigFile()
print(rc.read_config("test_host"))