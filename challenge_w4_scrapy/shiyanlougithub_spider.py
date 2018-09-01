#-*- coding:utf-8 -*-
'''
scrapy spider 模型：
import scrapy
class ABC(scrapy.Spider):
    ＃定义要爬取的URL
    def start_urls(self):
        return 
    #对爬取的response处理，yield 返回值
    def parse(self,response):
       yield{
           'name':zxspython,
           '':
           }

命令行运行：scrapy runspider filename.py -o date.json
'''
'''
scrapy 数据提取器：
##  css:
一.筛选元素：
    <div id='abc'>
  1.  id提取元素：response.css('div#abc')
   <div class='abc'>
  2.  class提取元素：response.css('div.abc')
  3. 提取里面迭代的<a>元素：reaponse.css('div#abc a')
  4. 提取多个class :response.css('div[class="class1 class2"]')

二.筛选元素内部内容：
    提取元素里面文本：response.css('div#abc::text')
    提取元素里面的属性：response.css('div#adb a::attr(href)')

三.以上获得一个对象通过方法取得值
   .extract(default='none')提取操作,deault设置为找到默认值。
   .extract_first() 提取第一个

##  xpath:
节点概念：
    / :根节点
    //:不考虑位置
    .:当前节点
    ...:当前节点父节点

一.提取元素(使用定位 标签名[@attr="value"]) 
   筛选所有h2 元素：response.xpath('//h1')
   通过 属性 筛选元素：response.xpath('/p[@属性="value"]')
       通常属性值有多个，不好书写，可以使用唯一代表该div的类明：response.xpath('div[contain(@attr,"value")]') 

二.进一步筛选值/text;/@attr
   筛选元素里面文本：response.xpath('//h1/text()')
   筛选元素属性值： response.xpath('//img/@src')

'''

'''
数据进一步筛选：
正则表达式
'name:My image 1'.re('name:(.+)') 
...  'MY image 1'
只作用于第一个文本：re_first()

'''
import scrapy

class GithubSpider(scrapy.Spider):
    name = 'GithubSpider'
     
    @property
    def start_urls(self):
        url_tmpl='https://github.com/shiyanlou?page={}&tab=repositories'
        return(url_tmpl.format(i) for i in range(1,5))

    def parse(self,response):
        for course in response.css('div#user-repositories-list').xpath('//li[contains(@class,"col-12")]'):
            yield{
                    'name':course.css('div[class="d-inline-block mb-1"] a::text').extract()[0].strip(),
                    'date':course.css('relative-time::attr(datetime)').extract()[0]
                    }
