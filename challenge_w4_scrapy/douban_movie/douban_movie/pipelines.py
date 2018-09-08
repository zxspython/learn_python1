# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
import redis
import json
from scrapy.exceptions import DropItem

import codecs

class DoubanMoviePipeline(object):
    def __init__(self):
        self.file = codecs.open('data.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        item['summary'] = re.sub('\s+',' ',item['summary'])
        if not float(item['score']) >= 8.0:
            raise DropItem('score less than 8.0')
        self.redis.lpush('douban_movie:items',json.dumps(dict(item)))
        line = json.dumps(dict(item),ensure_ascii=False) + '\n'
        self.file.write(line)
        return item

    def open_spider(self,spider):
        self.redis = redis.StrictRedis(host='localhost',port=6379,db=0)
    
    def spider_closed(self,spider):
        self.file.close()
