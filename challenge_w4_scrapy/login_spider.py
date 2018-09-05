# -*- coding:utf-8 -*-
import scrapy

class LoginSpiderSpider(scrapy.Spider):
    name = 'login_spider'

    start_urls = ['https://www.shiyanlou.com/login']

    def parse(self,response):
        '''
        模拟登录的核心 scrapy.FormRequest 模拟一个 POST请求。
        .from_response 用于快速构建一个 FormRequest对象.从response中获取 请求的url、form表单信息
        我们只需要 指定必要的表单和回调函数就好了。

        '''
        csrf_token = response.xpath('//div[@class="login-body"]//input[@id="csrf_token"]/@value').extract_first()
        self.logger.info(csrf_token)

        return scrapy.FormRequest.from_response(
                response,
                formdata={
                    'csrf_token':csrf_token,
                    'login':'4454230.hi@163.com',
                    'password':'zxs2014911'
                },
                callback=self.after_login
                )
    def after_login(self,response):
        return [scrapy.Request(
            url='https://www.shiyanlou.com/user/84362/',callback=self.parse_after_login)]

    def parse_after_login(self,response):
        return {
                'lab_count':response.xpath('(//span[@class="info-text"])[2]/text()').re_first('[^\d]*(\d*)[^\d*]'),
                'lab_minutes':response.xpath('(//span[@class="info-text"])[3]/text()').re_first('[^\d]*(\d*)[^\d*]')
                }

