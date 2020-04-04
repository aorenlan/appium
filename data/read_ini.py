import os
import configparser

#os.path.realpath：获取当前执行脚本的绝对路径。
#os.path.split：如果给出的是一个目录和文件名，则输出路径和文件名
proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.txt")


class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath,encoding="utf-8-sig")

    def get_vip_ihao(self, param):
        value = self.cf.get("testcase", param)
        return value

    def get_svip_ihao(self, param):
        value = self.cf.get("svip", param)
        return value

    def get_pop(self, param):
        # print(self.cf.read("config.txt"))
        value = self.cf.get("pop_config", param)
        return value


if __name__ == '__main__':
    test = ReadConfig()
    # LocalIp = test.get_http('baseurl')
    # print(LocalIp)
    asdLocalIp = test.get_pop('pop_dict')
    print(asdLocalIp)
