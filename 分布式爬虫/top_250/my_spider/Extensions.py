import time

import logging

from scrapy import signals  # 引入信号
from scrapy.exceptions import NotConfigured  # 在settings 设置是否开启这个拓展

logger = logging.getLogger(__name__)


# 继承的是object也就是说放在什么地方都能使用,耦合度非常低
class ResdisSpiderSmartClosedExtensions(object):

    def __init__(self, idle_number, crawler):
        # 没有请求之后就会触发空转的信号,如果一直没有,就会持续触发，我们可以设置一个数量值，你达到设置的值之后就结束掉
        # crawler 就是我们写到settings的一些配置
        self.idle_number = idle_number
        self.crawler = crawler
        self.idle_list = []  # 专门记录触发信号的时间
        self.idle_count = 0  # 记录次数,进行对比

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getbool('MYEXT_ENABLED'):
            raise NotConfigured

        # 判断下是不是 redis的爬虫
        if not 'redis_key' in crawler.spidercls.__dict__.keys():
            raise NotConfigured('Only Support Redis Version')

        idle_number = crawler.settings.getint('IDLE_NUMBER', 10)  # 取值 没有就10次
        ext = cls(idle_number, crawler)

        # 课件上三次信号 open 和 close 可以不写 我们只是打印了时间
        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)  # 属于回调函数
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(ext.spider_idle, signal=signals.spider_idle)

        return ext

    def spider_opened(self, spider):
        logger.info("opened spider %s redis spider Idle, Continuous idle limit: %d" % (spider.name, self.idle_count))

    def spider_closed(self, spider):
        logger.info("closed spider %s, idle count %d, Continuous idle count: %d" % (
        spider.name, self.idle_count, len(self.idle_list)))

    def spider_idle(self, spider):
        self.idle_count += 1
        self.idle_list.append(time.time())
        idle_list_len = len(self.idle_list)  # 主要是判断list的长度

        # 大于2证明idle多次                      如果这个key没有的就证明开始爬取了
        if idle_list_len > 2 and spider.server.exists(spider.redis_key):
            # 如果出现持续空闲 但是key又还存在就证明还没有抓取完
            self.idle_list = [self.idle_list[-1]]  # 变成了长度为1的
        elif idle_list_len > self.idle_number:
            logger.info('\n continued idle number exceed{} Times'
                        '\n meet the idle shutdown conditions, will close the reptile operation'
                        '\n idle start time: {},close spider time: {}'.format(self.idle_number,
                                                                              self.idle_list[0],
                                                                              self.idle_list[-1]))
            self.crawler.engine.close_spider(spider, 'closespider_pagecount')