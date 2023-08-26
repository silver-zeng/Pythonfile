import requests
import scrapy
from ..items import BqbImageItem


class BqbEmoteSpider(scrapy.Spider):
    name = "bqb_emote"
    allowed_domains = []
    page = 1
    start_urls = ["https://www.qqtn.com/tp/dmtp_1.html"]

    def parse(self, response):
        if self.page<3:
            img_url_list = response.xpath('//ul[@class="g-gxlist-imgbox"]/li')
            print(len(img_url_list))
            for i in img_url_list:
                url = i.xpath('./a/@href').get()
                # 次级页面表情包路径
                url_end = 'https://www.qqtn.com/'+url
                # 表情包名称
                filename = i.xpath('./a/@title').get()
                item_fack = {}
                item_fack['url_end'] = url_end
                item_fack['filename'] = filename
                # cb_kwargs传参需要用不定长参数接收，meta=  这种形式传参不用，会直接传到response里面
                yield scrapy.Request(url_end,callback=self.emot_image,cb_kwargs=item_fack)
            self.page += 1
            page_url = "https://www.qqtn.com/tp/dmtp_{}.html".format(self.page)
            yield scrapy.Request(page_url,callback=self.parse)


    def emot_image(self, response, **kwargs):
        # 次级页面下图片url
        image_url_list = response.xpath('//p[@align="center"]/img/@src').getall()
        item = BqbImageItem()
        for img_url in image_url_list:
            image_data = requests.get(img_url)
            item['img_data'] = image_data.content
            item['filename'] = kwargs['filename']
            yield item

