# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class MySpiderPipeline:
    def open_spider(self,spider):
        self.f = open('movie.txt', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        s = json.dumps(dict(item), ensure_ascii=False)  # 将字典转换为json传输储存
        self.f.write(s + '\n')
        return item
    def close_spider(self,spider):
        self.f.close()
