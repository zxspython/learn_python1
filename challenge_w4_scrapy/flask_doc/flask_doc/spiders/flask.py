# -*- coding: utf-8 -*-

# 解析爬取的页面连接,在后面爬取用

#CrawlSpider,的rules属性
#rules 是一个包含 Rule 对象的列表，每个Rule 定义了，解析爬取页面连接，后面使用的规则。
#scrapy.spider.Rule


#爬取 URL 和 TEXT 字段，放入item 
#item 存入 redis数据库 

import scrapy
from scrapy.spider import Rule
from flask_doc.items import PageItem
# 新加内容 用于添加Rule
from scrapy.linkextractors import LinkExtractor


class FlaskSpider(scrapy.spider.CrawlSpider):
    name = 'flask'
    allowed_domains = ['flask.pocoo.org']
    start_urls = ['http://flask.pocoo.org/docs/0.12/']

    rules = (
            Rule(LinkExtractor(allow='http://flask.pocoo.org/docs/0.12/.*'),callback='parse_page',follow=True),
                )

    def parse_page(self, response):
        item = PageItem()
        item['url']=response.url
        item['text']=' '.join(response.xpath('//text()').extract())
        yield item
