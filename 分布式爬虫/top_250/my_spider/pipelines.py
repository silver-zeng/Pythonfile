# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class MySpiderPipeline:
    def open_spider(self, spider):
        # 配置mysql 数据库
        self.f = open('movie.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # 写sql语句
        s = json.dumps(dict(item), ensure_ascii=False)
        self.f.write(s + '\n')

        return item



    def close_spider(self, spider):
        # 关闭连接
        self.f.close()


