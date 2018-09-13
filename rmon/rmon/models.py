#!usr/bin/env python3
#-*- conding:utf-8 -*-
# rmon.model
# 所有的 model类 以及相应的 序列化类

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# Redis 服务器客户点连接Redis服务器，python 访问Redis客户端　redis-py
# 目标在　server　中实现一个　redis 属性，对应redis 客户端
from redis import StrictRedis,RedisError
from rmon.common.rest import RestException

#创建一个映射类
#使用 db.session.add().delete().commit()
db = SQLAlchemy()


#创建一个表,使用映射类的模板
#创建实例方法 save delete实现实例保存，删除
class Server(db.Model):

    __tablename__ = 'redis_server'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    description = db.Column(db.String(512))
    host = db.Column(db.String(15))
    port = db.Column(db.Integer,default=6379)
    password = db.Column(db.String)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow)
    create_at = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
        return '<Server(name=%s)>'%self.name

    @property
    def redis(self):
        # 基于redis.StrictRedis　实现访问Redis
        # 客户端访问　Redis　可能会遇到一系列问题，这时候会抛出rediserror，我们要捕获异常，并成为我们自定义的异常。common
        return StrictRedis(host=self.host,
                           port=self.port,
                           password=self.password)


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def ping(self):
        # 检查Redis 服务器是否可访问
        try:
            return self.redis.ping()
        except RedisError:
            raise RestException(400,'redis server %s can not connected'% self.host)


    def get_metrics(self):
        # 获得　Redis 服务器监控信息
        #　通过　Redis　服务器指令info 返回监控信息，参考　
        try:
            return self.redis.info()
        except RedisError:
            raise RestException(400,'redis server %s can not connected'% self.host)
if __name__ == '__main__':
    Server()
