# -*- coding: utf-8 -*-
import scrapy


class CoursesFollowSpider(scrapy.Spider):
    name = 'Courses_follow'
    #设定开始的url 网址
    start_urls = ['https://shiyanlou.com/courses/63']

    def parse(self, response):
        #每个页面返回的 数据
        yield{
            'name':response.xpath('//h4[@class="course-infobox-title"]/span/text()').extract_first(),
            'author':response.xpath('//div[@class="mooc-info"]/div[@class="name"]/strong/text()').extract_first()
        }
        # response.follow(obj,callback) 根据参数获得URL，self.parse 为callback;
        for url in response.xpath('//div[@class="sidebox-body course-content"]/a/@href'):
            yield response.follow(url,callback=self.parse)


