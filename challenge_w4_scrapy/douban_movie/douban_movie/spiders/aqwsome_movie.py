# -*- coding: utf-8 -*-
# 创建类
import scrapy
# CrawlSpider，创建rules
from scrapy.spider import Rule
from scrapy.linkextractors import LinkExtractor
# 创建 items
from douban_movie.items import MovieItem

class AwesomeMovieSpider(scrapy.spider.CrawlSpider):
    name = 'awesome-movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/subject/3011091/']

    rules = (
             #字符串前面加 r 原生字符串（不对后面字符进行转义
             #etc : '\\' 默认转义为 '\'； r'\\' 不变
             Rule(LinkExtractor(allow=r'https://movie.douban.com/subject/.+/?from=subject-page'),callback='parse_pate',follow=True),        
    )

    def parse_movie_item(self,response):
        item = MovieItem()
        item['url'] = response.url
        item['name'] = response.xpath('//span[@property="v:itemreviewed"]/text()').extract_first()
        item['summary'] = response.xpaht('//span[@property="v:summary"]/text()').extract_first()
        item['score'] =  response.xpath('//strong[@property="v:average"]/text()').extract_first()
        retrun item

    def parse_start_url(self,response):
        yield self.parse_movie_item(response)

    def parse_pate(self, response):
        yield self.parse_movice_item(response)
