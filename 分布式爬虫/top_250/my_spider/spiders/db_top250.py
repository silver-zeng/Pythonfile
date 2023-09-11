import scrapy
import json

from scrapy_redis.spiders import RedisSpider

from ..items import MySpiderItem

class DbTop250Spider(RedisSpider):
    name = "db_top250"
    # 允许通过的域名
    # allowed_domains = ["movie.douban.com"]
    # 初始抓取的url
    # start_urls = ["https://movie.douban.com/top250"]
    redis_key = "db:start_urls"
    page = 0

    def parse(self, response):
        print("---------------这是2-------------------")
        # 在parse 中我们只需要关注怎么解析就行，因为response这个对象就有xpath属性
        node_list = response.xpath('//div[@class="info"]')
        if node_list:
            for i in node_list:
                # 标题
                movie_title = i.xpath('./div/a/span/text()').get()
                # 导演
                director = i.xpath('./div/p/text()').get().strip().replace(' ', ' ')
                # 分数
                score = i.xpath('.//span[@class="rating_num"]/text()').get()

                tong = {}
                tong['movie_title'] = movie_title
                tong['director'] = director
                tong['score'] = score

                # 电影详情页
                detail_url = i.xpath('./div/a/@href').get()
                yield scrapy.Request(detail_url, callback=self.get_detail, meta={"info":tong})
                # {"info":{"movie_title":"肖生克的救赎",'director':'导演的信息','score':'9.7'}}
            self.page+=1
            page_url = 'https://movie.douban.com/top250?start={}&filter='.format(self.page*25)
            yield scrapy.Request(page_url,callback=self.parse)
        else:
            return

    # 专门负责解析详情页的内容（次级页面解析函数）
    def get_detail(self, response):
        item = MySpiderItem()
        info = response.meta.get("info")
        item.update(info)
        desc = response.xpath('//span[@property="v:summary"]/text()').get().strip()
        item['desc'] = desc

        yield item





