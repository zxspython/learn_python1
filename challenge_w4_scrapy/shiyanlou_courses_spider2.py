
import scrapy

class ShiyanlouCoursesSpider(scrapy.Spider):

    name = 'shiyanlou-course'

    @property
    def start_urls(self):
        url_tmpl = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
        #这里需要返回一个可迭代对象，列表、元组、或者生成器（这里是生成器）
        return (url_tmpl.format(i) for i in range(1,23))

    def parse(self,response):
        #css 语法获得div中 class=course-body的内容
        for course in response.css('div.course-body'):
            yield{
                    'name':course.css('div.course-name::text').extract_first(),
                    'description':course.css('div.course-desc::text').extract_first(),
                    'type':course.css('div.course-footer span.pull-right::text').extract_first(default='Free'),
                    'students':course.xpath('.//span[contains(@class,"pull-left")]/text()[2]').re_first('[^\d]*(\d+)[^\d]*')

                    }

