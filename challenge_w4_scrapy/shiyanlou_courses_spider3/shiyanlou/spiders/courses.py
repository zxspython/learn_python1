# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import CoursesItem

class CoursesSpider(scrapy.Spider):
    name = 'courses'

    #可以爬取的域名
    allowed_domains = ['shiyanlou.com']
    @property
    def start_urls(self):
        url_tmpl = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
        return(url_tmpl.format(i) for i in range(1,23))

    def parse(self, response):
        for courses in response.css('div.course-body'):
            item=CoursesItem({
                'name':courses.css('div.course-name::text').extract_first(),
                'description':courses.css('div.course-desc::text').extract_first(),
                'type':courses.css('div.course-footer span.pull-right::text').extract_first(default='免费'),
                'students':courses.xpath('.//span[contains(@class,"pull-left")]/text()[2]').re_first('[^\d]*(\d*)[^\d]*')
                })
            yield item
