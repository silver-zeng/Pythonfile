# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline


#
class PicturePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_url = item['img_url']
        yield scrapy.Request(image_url)

    # 重新设置路径
    def file_path(self, request, response=None, info=None, *, item=None):
        file_path = item['title']
        img_name = item['img_name']
        return f'{file_path}/{img_name}'
