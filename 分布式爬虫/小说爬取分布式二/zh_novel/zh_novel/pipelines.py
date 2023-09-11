# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import datetime

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from scrapy.exceptions import DropItem

from .items import ZhNovelItem,ChapterItem,ContentItem

class ZhNovelPipeline:
    def open_spider(self, spider):
        # mysql数据库链接
        data_cofig = spider.settings['DATABASE_CONFIG']
        if data_cofig['type'] =='mysql':
            self.conn = pymysql.connect(**data_cofig['config'])
            self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        if isinstance(item, ZhNovelItem):
            # 确保数据库中没有重复数据
            sql = 'select book_name from novel_briefs  where book_name=%s and author=%s'
            if not self.cursor.execute(sql, (item['book_name'], item['author'])):
                # 写入小说
                sql = 'insert into novel_briefs (book_name,type,number,status,intro,author,c_time,book_url,chapter_url)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                # 补充数据并执行
                self.cursor.execute(sql,(
                    item.get('book_name'),
                    item.get('type'),
                    item.get('number'),
                    item.get('status'),
                    item.get('intro'),
                    item.get('author'),
                    item.get('c_time'),
                    item.get('book_url'),
                    item.get('chapter_url'),
                ))
                self.conn.commit()
            return item
        # 判断是不是ChapterItem小说章节信息
        elif isinstance(item, ChapterItem):
            data_list = []
            sql = 'insert into novel_chapter(title,ordernum,chapter_url,catalog_url,c_time) values (%s,%s,%s,%s,%s)'
            for index,chapter in enumerate(item.get('chapter_list')):
                c_time = datetime.datetime.now()
                # 章节序号
                ordernum = index+1
                # 拆包，分别存chapter为元祖
                title, chapter_url, catalog_url = chapter
                data_list.append((title, ordernum, chapter_url, catalog_url, c_time))
            self.cursor.executemany(sql, data_list)
            self.conn.commit()
        elif isinstance(item,ContentItem):
            sql = 'update novel_chapter set content=%s where chapter_url =%s'
            content = item.get('content')
            chapter_url = item.get('chapter_url')
            self.cursor.execute(sql, (content, chapter_url))
            self.conn.commit()
            return item
        else:
            return DropItem

    def close_spider(self, spider):
        # 关闭连接
        data_cofig = spider.settings['DATABASE_CONFIG']
        if data_cofig['type'] =='mysql':
            self.cursor.close()
            self.conn.close()
