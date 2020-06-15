import requests
import json
import time


class TxZp:
    def __init__(self):
        self.ts = str(int(round(time.time() * 1000)))
        self.url = "https://careers.tencent.com/tencentcareer/api/post/Query?pageIndex={}&pageSize=10&timestamp="+self.ts
        self.data_source = []
        self.sd = self.save_data()


    def get_data(self, url):
        """
        发送请求获取电影列表页数据
        :param url:
        :return:
        """
        response = requests.get(url=url)
        return response.content.decode()

    def parse_recruit_list_data(self, content, sd):
        """
        解析列表页数据
        需要保存电影的名称以及电影的二级地址
        :param content:
        :return:
        """
        # 0. 启动生成器
        next(sd)
        # 1. json格式化
        data = json.loads(content)
        # 2. 从json对象中提取招聘岗位列表
        result_list = data["Data"]["Posts"]
        # print(result_list)
        # 2.1 空字典变量
        # 3. 遍历
        for rt in result_list:
            # 拼接招聘详情的地址
            recruit_detail_link = "https://careers.tencent.com/tencentcareer/api/post/ByPostId?postId=" + rt["PostId"] + "&timestamp="+self.ts
            # 发送二级请求 获取招聘详情页面
            self.parse_recruit_detail_data(recruit_detail_link, sd)

    def parse_recruit_detail_data(self, link, sd):
        """
        解析电影详情页数据
        :param content:
        :return:
        """
        # 1. 发送请求
        content = self.get_data(link)
        # 2. json格式化，并提取相关信息
        detail = json.loads(content)["Data"]
        # print(detail)
        result_list = {}
        result_list["岗位名称"] = detail["RecruitPostName"]
        result_list["职责"] = detail["Responsibility"]
        result_list["要求"] = detail["Requirement"]
        sd.send(result_list)

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
            with open("txzp.txt", "a", encoding="utf-8") as f:
                f.write("岗位名称：")
                f.write(data["岗位名称"])
                f.write("\n\n")
                f.write("岗位职责：")
                f.write("\n")
                f.write(data["职责"])
                f.write("\n\n")
                f.write("岗位要求：")
                f.write("\n")
                f.write(data["要求"])
                f.write("\n-----------------\n")
                f.close()
        # for content in data:
        #             f.write(json.dumps(content, ensure_ascii=False, indent=4))
        #             f.write("\n")
        #         f.close()
            print(data)

    def running(self):
        """
        爬虫启动
        :return:
        """
        # 1. 构造地址
        for index in range(2):
            # print("------------------")
            url = self.url.format(index)
            # 2. 发送请求
            content = self.get_data(url)
            # 3. 解析列表页数据
            self.parse_recruit_list_data(content, self.save_data())


if __name__ == '__main__':
    TxZp().running()
