import scrapy
import datetime
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import NovelItem,ChapterItem



class ZonghengSpider(CrawlSpider):
    name = "zongheng"
    allowed_domains = ["book.zongheng.com"]
    start_urls = ["https://book.zongheng.com/store/c0/c0/b0/u0/p1/v0/s1/t0/u0/i1/ALL.html"]

    rules = (
            Rule(LinkExtractor(allow=r"https://book.zongheng.com/book/\d+.html"), callback="parse_book", follow=True),
            Rule(LinkExtractor(allow=r"https://book.zongheng.com/showchapter/\d+.html"), callback="parse_catalog", follow=True),
# https://book.zongheng.com/showchapter/1066246.html
        )
    # 得到的是二级页面--小说详情页
    def parse_book(self, response):
        # 类型
        category = response.xpath('//div[@class="crumb"]/a[2]/text()').get()
        # 书名
        book_name = response.xpath('//div[@class="book-name"]/text()').get().strip()
        # 字数
        book_nums = response.xpath('//div[@class="nums"]/span[1]/i/text()').get()
        # 状态
        status = response.xpath('//div[@class="book-label"]/a[1]/text()').get()
        # 简介
        description = response.xpath('//div[@class="book-dec Jbook-dec hide"]/p/text()').get()
        # 作者
        auathor = response.xpath('//div[@class="au-name"]/a/text()').get()
        # 抓取的时间
        c_time = datetime.datetime.now()
        # 小说的url
        book_url = response.url
        # 章节的url
        catalog_url = response.xpath('//div[@class="fr link-group"]/a[1]/@href').get()


        item = NovelItem()
        item['category'] = category
        item['book_name'] = book_name
        item['auathor'] = auathor
        item['status'] = status
        item['book_nums'] = book_nums
        item['description'] = description
        item['c_time'] = c_time
        item['book_url'] = book_url
        item['catalog_url'] = catalog_url

        return item

    def parse_catalog(self, response):
        tags = response.xpath('//ul[@class="chapter-list clearfix"]/li/a')
        chapter_list = []
        catalog_url = response.url
        for i in tags:
            # 标题
            title = i.xpath('./text').get ()
            # 章节url
            chapter_url = i.xpath('./@href').get()
            # 抓的是所有的章节信息和url
            chapter_list.append((title, chapter_url, catalog_url))

        item = ChapterItem()
        item['chapter_list'] = chapter_list
        yield item




