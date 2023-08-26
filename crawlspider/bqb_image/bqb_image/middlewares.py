# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import requests
import random
from My_config import user_agent_list
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class BqbImageSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class BqbImageDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)

# 自定义类
class User_AgentMiddleware:
    # 从user_agent_list随机获取一个user-agent伪装
    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(user_agent_list)
        return None

class ProxyMiddleware:
    # 从流冠官网api随机获取一个ip
    def process_request(self, request, spider):
        url='http://ecs.hailiangip.com:8422/api/getIpEncrypt?dataType=1&encryptParam=SlDyzgfgDW12vuaMHmQkMz9pKEmWH7kDAoD1ZC4KkxpHXuvLm%2B3L9xWaasGPtq4ToBLdEhC0fc8Cl3Rk7UuZyG25yJU7qaNHua2FDWHe9PJHJHwIXpXaJ0%2FambDJtU%2FA15qKLtNiqA6CuATqLBz%2BYxauUKrUKPonN4D%2FUXe1xVUfFaJxyBo8680oTdrXHKDtWhSglUCiFW5HEXHAbvQib9zbJ280PfgKxcbaM9RRtYCtxFCQehkdZXg2FiRfhV0V'
        data = requests.get(url)
        request.meta['proxy'] = 'https://' + data.text
        return None