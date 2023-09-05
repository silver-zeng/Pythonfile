# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MySpiderItem(scrapy.Item):

    movie_title = scrapy.Field()
    director = scrapy.Field()
    score = scrapy.Field()
    desc = scrapy.Field()


