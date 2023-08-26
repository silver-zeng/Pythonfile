import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import PictureItem
# CrawlSpider
class ImgsNameSpider(CrawlSpider):
    # 一样的
    name = 'imgs_name'

    # allowed_domains = ['baidu.com']
    start_urls = ['https://www.qqtn.com/tp/wmtp_1.html']
    # 规则 元组
    rules = (
        # Rule(): 实例化对象
        # LinkExtractor： 链接提取器，提取url
        # allow：爬取的规则，对应的正则表达式。在源码当中找对应url，url请求所得到的数据由callback指定
        # callback:调用的函数，解析的方法名以字符串的形式传递
        # follow:根据规则从response提取出来的链接是否继续提取。如果是True，继续提取
        # /tp/wmtp_2.html  /tp/wmtp_3.html  /tp/wmtp_4.html  /tp/wmtp_5.html
        # \d匹配数字，\d只能匹配一个数字
        # 翻页爬取的规则
        # 数据之间是用逗号隔开
        Rule(LinkExtractor(allow=r'/tp/wmtp_\d+.html'), callback='parse_item', follow=True),
        # 定义一个爬取详情页url规则
        # /article/article_337656_1.html
        # /article/article_336391_1.html
        Rule(LinkExtractor(allow=r'/article/article_.*?.html'), callback='detail_item', follow=False),
    )

    def parse_item(self, response):
        imgs = response.xpath('//ul[@class="g-gxlist-imgbox"]/li/a/img')
        # 一页的数据是20张图片
        print(len(imgs))

    # 详情页图片的解析
    def detail_item(self, response):
        # 标题
        title = response.xpath('//div[@class="g-cont-detail g-main-bg"]/h1/text()').get()
        ps = response.xpath('//p[@align="center"]')
        for i in ps:
            item = PictureItem()
            item['title'] = title
            img_url = i.xpath('./img/@src').get()
            item['img_url'] = img_url
            # https://p.qqan.com/up/2023-8/16928473062247052.jpg"
            # 16928473062247052.jpg作为图片的名字
            # img_url
            print(img_url)  # 第一个爬取速度是否过快  是否提取到其他页面的url
            item['img_name'] = img_url.split('/')[-1]
            yield item

