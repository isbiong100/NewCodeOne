import requests
import json
import random


class DouBanTv:

    def __init__(self):
        # 1. 请求的地址
        self.url = "https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={}"

        # 2. 构造请求头列表
        self.headers = [
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
            },
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"
            },
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2"
            }
        ]

        # 3. 数据源
        self.data_list = []

        # 4. 构造url地址
        self.urls = [self.url.format(i*20) for i in range(10)]

    def get_data(self, url):
        """根据传入的url地址 发送请求 得到响应"""
        # 1. 先取请求头
        header = self.headers[random.randint(0, len(self.headers)-1)]
        # 2. 发送请求得到响应
        response = requests.get(url=url, headers=header)
        # 3. 通过得到的response来解析想要保存的数据
        self.parse_data(response.content.decode())

    def parse_data(self, content):
        """解析数据"""
        # 1. 将json转成python对象
        data_dict = json.loads(content)
        # 2. 提取相应的数据
        for tv_info in data_dict["subjects"]:
            tv_dict = {}
            # 保存信息到tv_dict中
            tv_dict["tv_name"] = tv_info["title"]
            tv_dict["tv_rate"] = tv_info["rate"]
            tv_dict["tv_url"] = tv_info["url"]
            # 添加电视tv到数据源中
            self.data_list.append(tv_dict)
        return self.data_list

    def save_data(self, data):
        """保存数据"""
        with open("tv.txt", "a", encoding="utf-8") as f:
            for content in data:
                f.write(json.dumps(content, ensure_ascii=False, indent=4))
                f.write("\n")
            f.close()

    def run(self):
        """爬虫程序启动"""
        # 1. 取地址
        for url in self.urls:
            print(url)
            # 1.1 发送请求
            self.get_data(url)
        # 2. 保存
        self.save_data(self.data_list)


if __name__ == '__main__':
    DouBanTv().run()
