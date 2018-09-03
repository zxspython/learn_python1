# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

#使得 爬取的 字典类型数据（无序）,改变成结构型数据item

import scrapy


class UserItem(scrapy.Item):
    name = scrapy.Field()
    type = scrapy.Field()
    status = scrapy.Field()
    job = scrapy.Field()
    school = scrapy.Field()
    join_date = scrapy.Field()
    level = scrapy.Field()
    learn_courses_num = scrapy.Field()

class CoursesItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    type = scrapy.Field()
    students = scrapy.Field()
