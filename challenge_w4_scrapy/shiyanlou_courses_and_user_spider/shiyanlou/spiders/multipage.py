# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import MultipageCourseItem

class MultipageSpider(scrapy.Spider):
    name = 'multipage'
    start_urls = ['https://shiyanlou.com/courses']

    def parse(self, response):
        for course in response.css('a.course-box'):
            item = MultipageCourseItem()
            item['name'] = course.xpath('.//div[@class="course-name"]/text()').extract_first()
            item['image'] = course.xpath('.//img/@src').extract_first()

            # response.urljoin（） 可以身成URL
            course_url = response.urljoin(course.xpath('@href').extract_first())
            # yield request 会身成一个response
            # scrapy.Request(url,callback) 产生一个request
            # request.mata[''] 可以在 request中存放 内容 （实现页面跟随）
            request = scrapy.Request(course_url,callback=self.parse_author)
            request.meta['item'] = item
            yield request

    def parse_author(self,response):
        #response.meta[''] 提取 request中的meta
        item = response.meta['item']
        # 继续爬取 内容 放入 item
        item['author'] = response.xpath('//div[@class="mooc-info"]/div[@class="name"]/strong/text()').extract_first()
        yield item

