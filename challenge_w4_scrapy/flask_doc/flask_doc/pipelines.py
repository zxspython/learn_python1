# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import redis
import json

class FlaskDocPipeline(object):
    def process_item(self, item, spider):
        # 将item 结果以 json 形式保存到 Redis 数据库的 list 结构中
        #re.sub(pattern(真则表达式规则),替换的字符串，需要替换的整个字符串)
        item['text'] = re.sub('\s+',' ',item['text'])
        # redis 接口：
        # 连接服务器 redis.StrictRedis(host='',port= ,db= )
        # 输入接口 self.redis.lpush 

        # json 
        # 对象序列化：json.dumps()
        self.redis.lpush('flask_doc:items',json.dumps(dict(item)))
        return item

    def open_spider(self,spider):
        self.redis = redis.StrictRedis(host='localhost',port=6379,db=0)
