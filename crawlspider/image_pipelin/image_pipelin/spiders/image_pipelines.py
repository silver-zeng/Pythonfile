import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ImagePipelinItem


class ImagePipelinesSpider(CrawlSpider):
    name = "image_pipelines"
    allowed_domains = ["www.wxbqb.com"]
    start_urls = ["https://www.wxbqb.com/weixin/index_1.html"]

    rules = (
        Rule(LinkExtractor(allow=r"https://www.wxbqb.com/weixin/index_\d+.html"), callback="parse_item", follow=True),
        # 详情页的图片地址，与外面列表的data-original属性值一样，所以只用一个规则
        # Rule(LinkExtractor(allow=r"https://www.wxbqb.com/res/2023/07-27/17/39d971dddded1ff14ee38379c17fc558.gif"), callback="parse_item", follow=False),
        #                           "https://www.wxbqb.com/res/2023/07-27/17/39d971dddded1ff14ee38379c17fc558.gif"

             )

    def parse_item(self, response):
        # 图片对象列表
        image_list = response.xpath('//div[@class="col-sm-12 col-md-3 col-lg-3 mb-20"]')
        for i in image_list:
            item = ImagePipelinItem()
            item["image_name"] = i.xpath('./p/a/img[@class="lazy"]/@alt').get()
            item["image_url"] = i.xpath('./p/a/img[@class="lazy"]/@data-original').get()
            return item
