import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import DtBqbItem


class DtImageSpider(CrawlSpider):
    name = "dt_image"
    # allowed_domains = ["qqtn.com"]
    start_urls = ["https://www.qqtn.com/bq/dtbq_1.html"]

    rules = (
        Rule(LinkExtractor(allow=r"/bq/dtbq_\d+.html"), callback="parse_item", follow=True),
        Rule(LinkExtractor(allow=r"/article/article_.*?.html"), callback="detail_image", follow=False),
    )

    def parse_item(self, response):
        img_list = response.xpath('//div/ul[@class="g-gxlist-imgbox"]/li')


    def detail_image(self, response):
        list = response.xpath('.//p[@align="center"]')
        title = response.xpath('//div[@class="g-cont-detail g-main-bg"]/h1/text()').get()
        for i in list:
            item = DtBqbItem()
            # 文件夹标题
            item["file_name"] = title
            # 图片链接
            item["img_url"] = i.xpath('./img/@src').get()
            # 图片名字
            item["img_name"] = item["img_url"].split("/")[-1]

            yield item
