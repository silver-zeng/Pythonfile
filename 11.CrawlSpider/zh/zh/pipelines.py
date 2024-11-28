# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from .items import NovelItem,ChapterItem

class ZhPipeline:
    def open_spider(self, spider):
        # mysql数据库链接
        data_cofig = spider.settings['DATABASE_CONFIG']
        if data_cofig['type'] =='mysql':
            self.conn = pymysql.connect(**data_cofig['config'])
            self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        if isinstance(item, NovelItem):
            # 确保数据库中没有重复数据
            sql = 'select book_name from novel where book_name=%s and auathor=%s'
            if not self.cursor.execute(sql, (item['book_name'], item['auathor'])):
                # 写入小说
                sql = 'insert into novel(category,book_name,auathor,status,book_nums,description,c_time,book_url,catalog_url)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                # 补充数据并执行
                self.cursor.execute(sql,(
                    item.get('category'),
                    item.get('book_name'),
                    item.get('auathor'),
                    item.get('status'),
                    item.get('book_nums'),
                    item.get('description'),
                    item.get('c_time'),
                    item.get('book_url'),
                    item.get('catalog_url'),
                ))
                self.conn.commit()
            return item
        elif isinstance(item, ChapterItem):
            pass


    def close_spider(self, spider):
        # 关闭连接
        data_cofig = spider.settings['DATABASE_CONFIG']
        if data_cofig['type'] =='mysql':
            self.cursor.close()
            self.conn.close()
