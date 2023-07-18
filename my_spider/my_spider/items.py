# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MySpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_title = scrapy.Field()
    director = scrapy.Field()
    score = scrapy.Field()
    jianjie = scrapy.Field()
