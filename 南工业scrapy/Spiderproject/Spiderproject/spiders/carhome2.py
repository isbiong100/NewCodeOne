# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import CarItem


class Carhome2Spider(CrawlSpider):
    name = 'ch2'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    # /pic/series/65-12.html
    # /pic/series/65-51.html
    # 查找更多图片的链接地址

    rules = (
        Rule(LinkExtractor(
            allow=r'https://car.autohome.com.cn/pic/series/65.+'),
            callback='parse_item'),
    )

    def parse_item(self, response):
        # 获取分类
        category = response.xpath('//div[@class="uibox"]/div[1]/text()').get()
        print(category)
        # 获取链接
        links = response.xpath('//div[contains(@class, "uibox-con")]/ul/li/a/img/@src').getall()
        new_links = list(map(lambda url: response.urljoin(url.replace("240x180_0_q95_c42", "1024x0_1_q95")), links))

        yield CarItem(category=category, image_urls=new_links)
