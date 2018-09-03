# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#打开pipline 在 setting 文件中

from datetime import datetime
from sqlalchemy.orm import sessionmaker
from shiyanlou.models import Course,User,engine
from shiyanlou.items import CoursesItem,UserItem

class ShiyanlouPipeline(object):

    #收到 item 后处理
    def process_item(self, item, spider):
        #判断 如果是 CourseItem 的 item 做_process_course_item 处理
        if isinstance(item,CoursesItem):
            self._process_course_item(item)
        #否则._process_user_item
        else:
            self._process_user_item(item)
        return item
    
    #定义函数具体的操作
    def _process_course_item(self,item):
        item['students'] = int(item['students'])
        self.session.add(Course(**item))

    def _process_user_item(self,item):
        item['level'] = int(item['level'][1:])
        item['join_date'] = datetime.strptime(item['join_date'].split()[0],'%Y-%m-%d').date()
        item['learn_courses_num'] = int(item['learn_courses_num'])
        self.session.add(User(**item))

    #打开爬虫前 关联数据库
    def open_spider(self,spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    #关闭爬虫后 提交数据，关闭关联
    def close_spider(self,spider):
        self.session.commit()
        self.session.close()
