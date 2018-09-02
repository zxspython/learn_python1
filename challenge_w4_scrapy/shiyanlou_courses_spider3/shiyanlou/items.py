# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CoursesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #爬虫scrapy 爬取的数据为一个字典，字典是无序的
    #scrapy 推荐使用Item容器来存放数据
    name = scrapy.Field()
    description = scrapy.Field()
    type = scrapy.Field()
    students = scrapy.Field()
