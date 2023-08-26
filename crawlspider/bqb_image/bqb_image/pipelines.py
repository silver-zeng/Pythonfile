# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os

class BqbImagePipeline:
    imagename = 1
    def process_item(self, item, spider):
        path = "./image/"+item['filename']

        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Folder '{path}' created.")
        else:
            print(f"Folder '{path}' already exists.")

        with open(f"{path}/{self.imagename}.jpg",'wb') as f:
            f.write(item["img_data"])
            self.imagename +=1
        return item
