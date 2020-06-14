# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from Spiderproject.Spiderproject  import settings
import scrapy


class SpiderprojectPipeline(object):
    def process_item(self, item, spider):
        print("管道1------------------->")
        print(item)
        return item


class SpiderprojectPipeline2(object):
    def process_item(self, item, spider):
        print("管道2------------------->")
        print(item)
        return item


class BMWImagePipline(ImagesPipeline):

    def get_media_requests(self, item, info):
        print("-------------------------get_media_requests-------------------------")
        # for url in item["image_urls"]:
        #     print(scrapy.Request(url))
        #     yield scrapy.Request(url)

        request = super(BMWImagePipline, self).get_media_requests(item, info)
        for obj in request:
            obj.item = item
            # print(obj.item.get('image_urls'))
        return request

    def file_path(self, request, response=None, info=None):
        """重写此方法,来自定义保存路径"""
        print("-----------file_path-------------------")
        path = super(BMWImagePipline, self).file_path(request, response, info)
        # 获取分类
        category = request.item.get('category')
        # 获取最后的存储路径
        full_path = settings.IMAGES_STORE
        # 图片根据分类存储路径
        category_path = settings.os.path.join(full_path, category)
        # print(category_path)
        # 如果文件夹已经注册过了,就不创建了
        # 南工业/Spiderproject/images/分类的名称/当前分类下的所有的图片
        if not settings.os.path.exists(category_path):
            # 如果没有分类文件夹就创建该文件夹
            settings.os.mkdir(category_path)
            print("创建文件夹----ok!")
        # 图片名称
        img_name = path.replace("full/", "")
        # 生成最终的路径 + 图片名称
        return settings.os.path.join(category_path, img_name)


class DMPipeline(object):
    def process_item(self, item, spider):
        pass

    def open_spider(self, spider):
        """在管道被启用的时候会被执行一次"""
        # 打开文件或者打开数据库连接
        # self.file = open("./")
        pass

    def close_spider(self, spider):
        """在管道关闭的时候会被执行一次"""
        # 关闭数据库 关闭文件流
        pass
