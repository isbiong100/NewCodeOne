from selenium import webdriver
import time


class JD:

    def __init__(self, product_name):
        self.url = 'https://www.jd.com'
        self.product_name = product_name

        # 设置对象
        self.options = webdriver.ChromeOptions()
        # 无头浏览器模式
        self.options.add_argument('--headless')
        # 禁止弹出页面
        self.options.add_argument('--disable-popup-blocking')

        # 创建浏览器对象
        self.chrome_driver = webdriver.Chrome(options=self.options)
        self.chrome_driver.maximize_window()

    def get_data(self):
        # 1. 模拟用户打开浏览器
        self.chrome_driver.get(self.url)
        # 2. 寻找商品输入的input
        self.chrome_driver.find_element_by_xpath('//*[@id="key"]').send_keys(self.product_name)
        # 3. 点击搜索按钮
        self.chrome_driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
        # 4. 停顿
        # time.sleep(2)

    def parse_data(self):
        # 1. 加载数据
        self.chrome_driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight);'
        )

        # 2. 匹配所有商品
        li_node = self.chrome_driver.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')

        for li in li_node:
            # 获取商品的名称
            print(li.text)
            print("*" * 50)

    def running(self):
        # 1. 请求数据
        self.get_data()
        # 循环解析数据
        while True:
            # 2. 解析数据
            self.parse_data()
            # 跳出循环的条件(没有数据解析了就停止)
            # 在网页源码中查找"pn-next disabled", 如果值为-1 说明没有找到, 那么意味着下一页按钮可用(可以点击)
            if self.chrome_driver.page_source.find("pn-next disabled") == -1:
                # 如果能来到这里面,说明不是最后一页,还有下一页可以访问
                self.chrome_driver.find_element_by_class_name("pn-next").click()
                time.sleep(0.5)
            else:
                break


if __name__ == '__main__':
    JD("玩具").running()