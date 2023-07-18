import json
from ..items import MySpiderItem  # 引入结构化数据字段
import scrapy


class DoubanTop250Spider(scrapy.Spider):
    name = "douban_top250"
    allowed_domains = ["movie.douban.com"]  # 允许哪些根域名访问，可以不填或者写多个
    start_urls = ["https://movie.douban.com/top250"]  # 豆瓣电影初始抓取的URL
    page = 0
    def parse(self, response):
        node_list= response.xpath('//div[@class="info"]')
        if self.page <= 10:
            for i in node_list:
                movie_title = i.xpath('./div/a/span/text()').get()  # 标题
                director = i.xpath('./div/p/text()').get().strip().replace('NBSP;',' ')  # 导演名称
                score = i.xpath('.//span[@class="rating_num"]/text()').get()  # 分数

                item= {}
                item['movie_title']=movie_title
                item['director']=director
                item['score'] = score

                # 次级详情页url
                detail_url=i.xpath('./div/a/@href').get()

                yield scrapy.Request(detail_url,callback=self.get_detail,meta={'info':item}) # meta可以将构造的字段传入回调函数get_detail
            self.page += 1
            page_url = 'https://movie.douban.com/top250?start={}&filter='.format(self.page*25)
            # 使用回调函数去调用列表解析，爬取分页数据
            yield scrapy.Request(page_url,callback=self.parse)
        else:
            return
    # 专门负责解析详情页内容
    def get_detail(self,response):
        item = MySpiderItem()
        info = response.meta.get("info")
        item.update(info)
        # 获取详情页的简介
        jianjie = response.xpath('//span[@property="v:summary"]/text()').get().strip()
        # 将详情页简介存入结构化数据字段
        item["jianjie"] = jianjie
        yield item



