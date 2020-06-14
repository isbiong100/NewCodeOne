import requests
import re
import time
import json


class Kuai:
    def __init__(self):
        # 访问地址
        self.url = "https://www.kuaidaili.com/free/inha/{}/"
        # 请求头
        self.header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        # 数据源
        self.data_source = []

    def get_data(self, url):
        """发送请求获取响应"""
        response = requests.get(url=url, headers=self.header)
        # 响应内容
        content = response.content.decode()
        return content

    def parse_data(self, data):
        """解析数据的方法"""
        # print(data)
        # 正则提取规则
        pattern = '<td data-title="IP">(.*?)</td>.*?<td data-title="PORT">(.*?)</td>.*?data-title="类型">(.*?)<'

        # 根据规则匹配数据
        result_list = re.compile(pattern, re.S).findall(data)

        if len(result_list) == 0:
            return
        else:
            self.save_data(result_list)

    def save_data(self, data):
        """存储数据"""
        for delegate in data:
            delegate_dict = dict()
            delegate_dict['ip'] = delegate[0]
            delegate_dict['port'] = delegate[1]
            delegate_dict['type'] = delegate[2]

            self.data_source.append(delegate_dict)

        # 写入文件
        self.write_data()

    def write_data(self):
        """写入文件"""
        json_dict = {}
        json_dict['data'] = self.data_source

        with open('./delegate.json', 'w', encoding='utf-8') as f:
            json.dump(json_dict, f, ensure_ascii=False, indent=4)
        print("写入成功!")

    def running(self):
        """爬虫启动程序"""
        # 1. 构造地址
        for index in range(1, 10):
            url = self.url.format(index)
            # 2. 发送请求获取响应
            content = self.get_data(url)
            # 3. 解析数据
            self.parse_data(content)
            # 4. 停顿1s
            time.sleep(1)


if __name__ == '__main__':
    Kuai().running()
