import requests


class LTBar:

    def __init__(self, name):
        """
        初始化方法, 当创建一个类的对象的时候,该方法会被自动执行,不需要手动调用
        """
        self.bar_name = name
        self.url = "https://tieba.baidu.com/f?kw=" + self.bar_name + "&ie=utf-8&pn={}"

    def get_urls(self):
        """该方法用来构造所有的url"""
        # 列表生成式
        return [self.url.format(50 * i) for i in range(4)]

    def parse_url(self, url):
        """发送请求并解析数据"""
        response = requests.get(url)
        return response.content.decode()

    def save_data(self, content, page_count):
        """保存数据"""
        file_name = "{}吧-第{}页".format(self.bar_name, page_count)
        with open('./tieba/' + file_name, 'w', encoding='utf-8') as f:
            f.write(content)

    def run(self):
        """爬虫程序启动"""
        # 1. 构造url地址
        request_list = self.get_urls()

        # 2. 在地址池中进行遍历, 每遍历出一个地址就向该地址发送请求, 获取响应得到内容
        for url in request_list:
            # 2.1 发送请求
            html_content = self.parse_url(url)
            # 2.2 二次提取网页中的数据,比如帖子的标题,帖子中首页的图片/音频文件等等
            # 2.3 直接保存网页内容到本地
            page_count = request_list.index(url) + 1
            self.save_data(html_content, page_count)


if __name__ == '__main__':
    # 1. 创建爬虫对象
    lt = LTBar("李毅")
    # 2. 启动爬虫程序
    lt.run()


