# -*- coding: utf-8 -*-
import scrapy
from ..items import SpiderprojectItem


class CnblogSpider(scrapy.Spider):
    name = 'cn'
    allowed_domains = ['cnblogs.com']
    start_urls = ['http://www.cnblogs.com/']

    def start_requests(self):
        pass

    def parse(self, response):
        print("请求已发送,响应已返回")
        # print(response.text)
        print("scrapy框架已经运行了!!!!")

        # extract_first() 是老版本的 新版本用get
        # extract() 是老版本的 新版本用get_all()

        item = SpiderprojectItem()
        # 解析数据
        item["link"] = response.xpath('//div[@class="post_item"]/div[2]/h3/a/@href').get()
        item["name"] = response.xpath('//div[@class="post_item"]/div[2]/h3/a/text()').get()

        # 将item通由引擎交给管道(pipeline)
        yield item

