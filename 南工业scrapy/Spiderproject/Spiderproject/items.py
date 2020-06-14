# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # 定义解析需要保存的数据
    name = scrapy.Field()
    link = scrapy.Field()


class CarItem(scrapy.Item):
    # 保存汽车的分类
    category = scrapy.Field()
    # 汽车的图片
    image_urls = scrapy.Field()
    # 图片信息字段
    images = scrapy.Field()


class DMItem(scrapy.Item):
    # 小说的名称
    fiction_name = scrapy.Field()
    # 章节
    section = scrapy.Field()
    # 章节名称
    section_name = scrapy.Field()
    # 章节连接
    section_link = scrapy.Field()
    # 内容
    section_content = scrapy.Field()
