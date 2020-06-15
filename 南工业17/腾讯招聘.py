import json

import requests
import re


class TctOffer:
    def __init__(self):
        self.url = "https://careers.tencent.com/tencentcareer/api/post/Query?pageIndex={}&pageSize=10"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/79.0.3945.88 Safari/537.36 "
        }
        self.sd = self.save_data()

    @staticmethod
    def save_data():
        print("-" * 5 + "写入数据" + "-" * 5)
        while True:
            data = yield
            if not data:
                return
            for item in data:
                result = "名称: {}\n简介: {}\n\n".format(item["RecruitPostName"], item["Responsibility"]);
                with open('./腾讯招聘数据结果.txt', 'a', encoding='utf-8') as f:
                    f.write(result)

    def fetch_dict(self, url, sd):
        response = requests.get(url=url, headers=self.header)
        content = json.loads(response.content.decode())
        next(sd)
        sd.send(content["Data"]["Posts"])

    def run(self):
        for i in range(1, 3):
            url = self.url.format(i)
            self.fetch_dict(url, self.sd)


if __name__ == '__main__':
    TctOffer().run()
