# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhNovelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    type = scrapy.Field()
    book_name = scrapy.Field()
    number = scrapy.Field()
    status = scrapy.Field()
    intro = scrapy.Field()
    author = scrapy.Field()
    c_time = scrapy.Field()
    book_url = scrapy.Field()
    chapter_url = scrapy.Field()


class ChapterItem(scrapy.Item):
    chapter_list = scrapy.Field()

class ContentItem(scrapy.Item):
    chapter_url = scrapy.Field()
    content = scrapy.Field()