
import requests
import re
import json

class Txzp:
    def __init__(self):
        self.url = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1587864644714&countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        self.data_list = []
        self.sd = self.save_data()

    def get_data(self, url):
        """
        发送请求获取电影列表页数据
        :param url:
        :return:
        """
        response = requests.get(url=url, headers=self.header)
        # print(response.content.decode())
        return response.content.decode()

    def parse_list_data(self, content,sd):
        next(sd)
        """解析数据"""
        # print()
        # 1. 将json转成python对象
        data_dict = json.loads(content)
        # 2. 提取相应的数据
        for work_info in data_dict["Data"]["Posts"]:
            work_dict = {}
            work_dict["work_name"] = work_info["RecruitPostName"]
            work_detail_link = work_info["PostId"]
            self.parse_detail_data(work_detail_link, work_dict, sd)




    def parse_detail_data(self, link, work_dict, sd):#
        """
        解析电影详情页数据
        :param content:
        :param film_dict:
        :return:
        """
        print("-------------")
        # 1. 发送请求
        link = "https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1587867088030&postId="+link+"&language=zh-cn"
        content = self.get_data(link)
        # 2. 根据规则提取下载地址
        data_dict = json.loads(content)
        work_dict['work_requirement'] = data_dict["Data"]["Requirement"]
        sd.send(work_dict)

    def save_data(self):
        """
        保存数据的方法
        :param data:
        :return:
        """
        print("---------- 写入数据 ---------------->")
        while True:
            data = yield
            if not data:
                return
            # 写入文件.....
            print(data)
            # 写入文件.....
            with open("data.txt", "a", encoding="utf-8") as f:
                f.write("work_name：")
                f.write(data["work_name"])
                f.write("\n")
                f.write("work_requirement：")
                f.write(data["work_requirement"])
                f.write("\n\n")
                f.close()



    def running(self):
        """
        爬虫启动
        :return:
        """
        # 1. 构造地址
        for index in range(2, 3):
            # print("------------------")
            url = self.url.format(index)
            # 2. 发送请求
            content = self.get_data(url)
            # 3. 解析列表页数据
            self.parse_list_data(content, self.sd)


if __name__ == '__main__':
    Txzp().running()