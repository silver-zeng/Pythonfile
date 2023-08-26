# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class ImagePipelinPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_url = item['image_url']
        yield scrapy.Request(image_url)

    # 重新设置路径
    def file_path(self, request, response=None, info=None, *, item=None):
        url = item['image_url']
        houzhui =url.split(".")[-1]
        img_name = item['image_name']
        return f'images/{img_name}.{houzhui}'