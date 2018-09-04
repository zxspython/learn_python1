# -*- coding: utf-8 -*-
import scrapy


class CoursesFollow1Spider(scrapy.Spider):
    name = 'Courses_follow'
    #设定开始的url 网址
    start_urls = ['https://shiyanlou.com/courses/63']

    def parse(self, response):
        #每个页面返回的 数据
        yield{
            'name':response.xpath('//h4[@class="course-infobox-title"]/span/text()').extract_first(),
            'author':response.xpath('//div[@class="mooc-info"]/div[@class="name"]/strong/text()').extract_first()
        }
        #同时在每个页面 找寻下一个爬取对象的URL
        # scrapy shell 查看爬取得到 ‘course/1’
        # scrapy.Response() 函数 定义爬取 URL ，和 callback 函数
        # response.url() 根据参数获得URL，self.parse 为callback;
        for url in response.xpath('//div[@class="sidebox-body course-content"]/a/@href').extract():
            yield scrapy.Request(url=response.urljoin(url),callback=self.parse)


