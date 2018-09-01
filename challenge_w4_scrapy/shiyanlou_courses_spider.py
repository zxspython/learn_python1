
import scrapy

class ShiyanlouCoursesSpider(scrapy.Spider):
    name = 'shiyanlou-course'

    #告诉scrapy 那些网页需要爬取
    #返回一个可迭代对象，可以是一个列表或者迭代器
    #迭代对象里面的元素为 scrapy.Request(url,callback)
    #scrapy.Request 创造一个request请求
    #url:告诉要爬取的网页；callback 一个回调函数，处理返回的网页，筛选信息。
    def start_requests(self):
        url_tmpl = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
        urls = (url_tmpl.format(i) for i in range(1,23))
        for url in urls:
            #这里回调函数用 parse
            yield scrapy.Request(url=url,callback=self.parse)

    #scrapy 内部下载器下载每个request,封装成一个response
    #这里需要传入response 作为参数
    def parse(self,response):
        #css 语法获得div中 class=course-body的内容
        for course in response.css('div.course-body'):
            yield{
                    'name':course.css('div.course-name::text').extract_first(),
                    'description':course.css('div.course-desc::text').extract_first(),
                    'type':course.css('div.course-footer span.pull-right::text').extract_first(default='Free'),
                    'students':course.xpath('.//span[contains(@class,"pull-left")]/text()[2]').re_first('[^\d]*(\d+)[^\d]*')

                    }

