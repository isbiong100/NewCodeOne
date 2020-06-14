import requests
from lxml import etree


# //ul[@class="sellListContent"]/li[@class="clear LOGCLICKDATA"]

class LianHome:

    def __init__(self):
        self.url = "https://nj.lianjia.com/ershoufang/pg{}/"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }

    def get_data(self, url):
        return requests.get(url=url, headers=self.header).content.decode()

    def parse_data(self, content):
        # 1. 创建对象
        ph = etree.HTML(content)

        # 2. 定位li基准节点
        li_node = ph.xpath('//ul[@class="sellListContent"]/li[@class="clear LOGCLICKDATA"] | '
                 '//ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')

        home_dict = {}
        for li in li_node:
            home_dict['house_name'] = li.xpath('.//div[@class="title"]/a/text()')[0]
            home_dict['house_price'] = li.xpath('.//div[@class="totalPrice"]/span/text()')[0] + \
                                       li.xpath('.//div[@class="totalPrice"]/text()')[0]

            print(home_dict)

    def running(self):
        # 构造请求地址
        for index in range(1, 3):
            url = self.url.format(index)
            # 发送请求
            content = self.get_data(url)
            # 解析
            self.parse_data(content)


if __name__ == '__main__':
    LianHome().running()