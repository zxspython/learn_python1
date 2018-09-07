# -*- coding:utf-8 -*-
# 这里在测试 flask_doc:items 是否储存内容
import redis

r = redis.StrictRedis(host='127.0.0.1',port=6379)

llen = r.llen('flask_doc:items')

assert llen >=70
