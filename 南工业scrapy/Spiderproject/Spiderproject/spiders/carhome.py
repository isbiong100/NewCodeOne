# -*- coding: utf-8 -*-
import scrapy
from ..items import CarItem


# 高清
# car3.autoimg.cn/cardfs/product/g26/M08/5A/55/1024x0_1_q95_autohomecar__ChcCP12J_XGAXP0pAAtylyqMfeQ144.jpg
# 缩略
# car3.autoimg.cn/cardfs/product/g26/M08/5A/55/240x180_0_q95_c42_autohomecar__ChcCP12J_XGAXP0pAAtylyqMfeQ144.jpg


class CarhomeSpider(scrapy.Spider):
    name = 'ch'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    # def start_requests(self):
    #     print("-------------start_requests-----------------")
    #     delegate = "http://117.158.65.216:36412"
    #     url = 'https://car.autohome.com.cn/pic/series/65.html'
    #     yield scrapy.Request(url=url, callback=self.parse, meta={'proxy': delegate})

    def parse(self, response):
        div_node = response.xpath('//div[@class="uibox"]')[1:]
        for car_info in div_node:
            # print("-----------parse------------")
            item = CarItem()
            # 获取分类的名称
            item["category"] = car_info.xpath("./div[1]/a/text()").get()
            # print(item["category"])

            # item["image_urls"] = car_info.xpath("./div[2]/ul/li/a/img/@src").getall()
            img_urls = car_info.xpath("./div[2]/ul/li/a/img/@src").getall()
            # print(img_urls)
            # https://car1.autoimg.cn/upload/2012/8/22/240x180_0_q95_c42_autohomecar__201208221938156714122.jpg
            # 将第二个参数中的可迭代对象中的每一个元素进行某种(函数)处理
            item["image_urls"] = list(map(lambda url: response.urljoin(url.replace("240x180_0_q95_c42", "1024x0_1_q95")), img_urls))
            yield item

