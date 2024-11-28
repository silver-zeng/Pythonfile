# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class NovelItem(scrapy.Item):
    category = scrapy.Field()
    book_name = scrapy.Field()
    auathor = scrapy.Field()
    status = scrapy.Field()
    book_nums = scrapy.Field()
    description = scrapy.Field()
    c_time = scrapy.Field()
    book_url = scrapy.Field()
    catalog_url = scrapy.Field()


class ChapterItem(scrapy.Item):
    chapter_list = scrapy.Field()
