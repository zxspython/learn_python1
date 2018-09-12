#!usr/bin/env python3
#-*- conding:utf-8 -*-
# rmon.model
# 所有的 model类 以及相应的 序列化类

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

if __name__ == '__main__':
    Server()
