'''
生成命令
1、先创建scrapy项目 zh_novel：   scrapy startproject zh_novel
2、cd进入zh_novel 项目文件夹下，创建继承crawlspider   项目名称  爬取路径网址：scrapy genspider -t crawl zongheng zongheng.com

'''
import scrapy
import datetime
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ZhNovelItem,ChapterItem,ContentItem


class ZonghengSpider(CrawlSpider):
    name = "zongheng"
    allowed_domains = ["book.zongheng.com"]
    start_urls = ["https://book.zongheng.com/store/c0/c0/b0/u0/p1/v9/s1/t0/u0/i1/ALL.html"]  # 小说列表,翻页https://book.zongheng.com/store/c0/c0/b0/u0/p{页数}}/v9/s1/t0/u0/i1/ALL.html

    rules = (
        #  小说详情页
        Rule(LinkExtractor(allow=r"https://book.zongheng.com/book/\d+.html"), callback="parse_book", follow=True, process_links='limit'), # process_links 也是回调函数，限制抓取小说的数量
        #  小说章节页
        Rule(LinkExtractor(allow=r"https://www.zongheng.com/detail/\d+?tabsName=catalogue"), callback="parse_chapter", follow=True),
        # 小说内容  https://book.zongheng.com/chapter/1258513/70741220.html
        Rule(LinkExtractor(allow=r"https://book.zongheng.com/chapter/\d+/\d+.html"), callback="get_content",follow=False),

    )

    # 限制下载小说数量
    def limit(self, links):
        # 处理LinkExtractor提取到的小说url
        for index, link in enumerate(links):
            if index==0:
                yield link
            else:
                return

# 得到的是二级页面--小说详情页
    def parse_book(self, response):
        # 类型
        type = response.xpath('//div[@class="book-info--tags"]/span[@class="cateFineId"]/text()').get()
        # 书名
        book_name = response.xpath('//div[@class="book-info--title"]/span/text()').get().strip()  # .strip()去空格
        # 字数
        number = response.xpath('//div[@class="book-info--nums"]/span[1]/i/text()').get()
        # 状态
        status = response.xpath('//div[@class="book-info--tags"]/span[@class="serialStatus"]/text()').get()
        # 简介
        intro = response.xpath('//section[@class="detail-work-info--introduction"]/text()').get()
        # 作者
        author = response.xpath('//div[@class="author-info--name"]/text()').get()
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

    # 章节目录信息解析
    def parse_chapter(self, response):
        tags = response.xpath('//ul[@class="chapter-list clearfix"]/li/a')
        chapter_list = []
        # 该章节详情的请求URL
        catalog_url = response.url
        for i in tags:
            # 标题
            title = i.xpath('./text()').get()
            # 章节url--小说内容
            chapter_url = i.xpath('./@href').get()
            # 抓的是所有的章节信息和url
            chapter_list.append((title, chapter_url, catalog_url))

        item = ChapterItem()
        item['chapter_list'] = chapter_list
        yield item

    # 解析小说内容
    def get_content(self, response):
        chapter_url = response.url
        content_list= response.xpath('//div[@class="content "]/p/text()').getall()
        content = ''.join(content_list)
        # 向管道传输数据
        item = ContentItem()
        item['chapter_url'] = chapter_url
        item['content'] = content
        yield item


