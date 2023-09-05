# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

import scrapy
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import requests
import os


class DtBqbPipeline:
    def process_item(self, item, spider):

        img_url = item["img_url"]
        filename = item["file_name"]
        img_name = item["img_name"]
        res = requests.get(img_url)
        path = f"./images/{filename}"
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Folder '{path}' created.")

        with open(f"{path}/{img_name}", "wb") as f:
            f.write(res.content)
