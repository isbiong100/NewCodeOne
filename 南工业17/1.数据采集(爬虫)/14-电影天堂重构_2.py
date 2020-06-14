import requests
import re


class Dytt:
    def __init__(self):
        self.url = "https://www.dy2018.com/html/gndy/dyzz/index_{}.html"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        self.data_source = []
        self.sd = self.save_data()

    def get_data(self, url):
        """
        发送请求获取电影列表页数据
        :param url:
        :return:
        """
        response = requests.get(url=url, headers=self.header)
        return response.content.decode('gbk')

    def parse_movie_list_data(self, content, sd):
        """
        解析列表页数据
        需要保存电影的名称以及电影的二级地址
        :param content:
        :return:
        """
        # 0. 启动生成器
        next(sd)
        # 1. 定义正则的规则
        pattern = '<table width="100%".*?<td height="26">.*?<a href="(.*?)".*?title="(.*?)">'
        # 2. 根据规则匹配结果
        result_list = re.compile(pattern, re.S).findall(content)
        # 2.1 空字典变量
        film_dict = {}
        # 3. 遍历
        for rt in result_list:
            film_dict['film_name'] = rt[1]
            # 拼接电影详情的地址
            film_detail_link = "http://www.dy2018.com" + rt[0]
            # 发送二级请求 获取电影详情页面
            self.parse_movie_detail_data(film_detail_link, film_dict, sd)

    def parse_movie_detail_data(self, link, film_dict, sd):
        """
        解析电影详情页数据
        :param content:
        :param film_dict:
        :return:
        """
        print("-------------")
        # 1. 发送请求
        content = self.get_data(link)
        # 2. 根据规则提取下载地址
        pattern = '<td style="WORD-WRAP.*?<a href="(.*?)">'
        # pattern = '<table style="BORDER-BOTTOM.*?<tbody>.*?<tr>.*?<td style="WORD-WRAP.*?<a href.*?>(.*?)</a>'
        result_list = re.compile(pattern, re.S).findall(content)

        if len(result_list) > 0:
            film_dict['download_link'] = result_list[0]
        sd.send(film_dict)

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

    def running(self):
        """
        爬虫启动
        :return:
        """
        # 1. 构造地址
        for index in range(2, 4):
            # print("------------------")
            url = self.url.format(index)
            # 2. 发送请求
            content = self.get_data(url)
            # 3. 解析列表页数据
            self.parse_movie_list_data(content, self.save_data())
            # print("解析第一页数据----------------------->ok!")


if __name__ == '__main__':
    Dytt().running()