# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BqbImageItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    img_data = scrapy.Field()
    filename = scrapy.Field()
