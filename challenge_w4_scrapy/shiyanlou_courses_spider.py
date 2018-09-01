
import scrapy

class ShiyanlouCoursesSpider(scrapy.Spider):
    name = 'shiyanlou-course'

    #����scrapy ��Щ��ҳ��Ҫ��ȡ
    #����һ���ɵ������󣬿�����һ���б���ߵ�����
    #�������������Ԫ��Ϊ scrapy.Request(url,callback)
    #scrapy.Request ����һ��request����
    #url:����Ҫ��ȡ����ҳ��callback һ���ص������������ص���ҳ��ɸѡ��Ϣ��
    def start_requests(self):
        url_tmpl = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
        urls = (url_tmpl.format(i) for i in range(1,23))
        for url in urls:
            #����ص������� parse
            yield scrapy.Request(url=url,callback=self.parse)

    #scrapy �ڲ�����������ÿ��request,��װ��һ��response
    #������Ҫ����response ��Ϊ����
    def parse(self,response):
        #css �﷨���div�� class=course-body������
        for course in response.css('div.course-body'):
            yield{
                    'name':course.css('div.course-name::text').extract_first(),
                    'description':course.css('div.course-desc::text').extract_first(),
                    'type':course.css('div.course-footer span.pull-right::text').extract_first(default='Free'),
                    'students':course.xpath('.//span[contains(@class,"pull-left")]/text()[2]').re_first('[^\d]*(\d+)[^\d]*')

                    }

