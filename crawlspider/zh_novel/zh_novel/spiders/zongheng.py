'''
生成命令
1、先创建scrapy项目 zh_novel：   scrapy startproject zh_novel
2、cd进入zh_novel 项目文件夹下，创建继承crawlspider   项目名称  爬取路径网址：scrapy genspider -t crawl zongheng zongheng.com

'''
import scrapy
import datetime
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ZhNovelItem,ChapterItem


class ZonghengSpider(CrawlSpider):
    name = "zongheng"
    allowed_domains = ["book.zongheng.com"]
    start_urls = ["https://book.zongheng.com/store/c0/c0/b0/u0/p1/v9/s1/t0/u0/i1/ALL.html"]  # 小说列表,翻页https://book.zongheng.com/store/c0/c0/b0/u0/p{页数}}/v9/s1/t0/u0/i1/ALL.html

    rules = (
        #  小说详情页
        Rule(LinkExtractor(allow=r"https://book.zongheng.com/book/\d+.html"), callback="parse_book", follow=True),
        #  小说章节页
        Rule(LinkExtractor(allow=r"https://book.zongheng.com/showchapter/\d+.html"), callback="parse_chapter", follow=True),

    )

# 得到的是二级页面--小说详情页
    def parse_book(self, response):
        # 类型
        type = response.xpath('//div[@class="book-label"]/a[@class="label"]/text()').get()
        # 书名
        book_name = response.xpath('//div[@class="book-name"]/text()').get().strip()  # .strip()去空格
        # 字数
        number = response.xpath('//div[@class="nums"]/span[1]/i/text()').get()
        # 状态
        status = response.xpath('//div[@class="book-label"]/a[@class="state"]/text()').get()
        # 简介
        intro = response.xpath('//div[@class="book-dec Jbook-dec hide"]/p/text()').get()
        # 作者
        author = response.xpath('//div[@class="au-name"]/a/text()').get()
        # 抓取时间(获取当前爬虫运行的时间)
        c_time = datetime.datetime.now()
        # 小说url
        book_url = response.url
        # 章节url
        chapter_url = response.xpath('//div[@class="fr link-group"]/a[@class="all-catalog"]/@href').get()

        # 序列化参数
        item = ZhNovelItem()
        item['type'] = type
        item['book_name'] = book_name
        item['number'] = number
        item['status'] = status
        item['intro'] = intro
        item['author'] = author
        item['c_time'] = c_time
        item['book_url'] = book_url
        item['chapter_url'] = chapter_url
        return item  # yield 返回多个

    # 章节信息解析
    def parse_chapter(self, response):
        tags = response.xpath('//ul[@class="chapter-list clearfix"]/li/a')
        chapter_list = []
        catalog_url = response.url
        for i in tags:
            # 标题
            title = i.xpath('./text').get()
            # 章节url
            chapter_url = i.xpath('./@href').get()
            # 抓的是所有的章节信息和url
            chapter_list.append((title, chapter_url, catalog_url))

        item = ChapterItem()
        item['chapter_list'] = chapter_list
        yield item
