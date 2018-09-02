# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#### pipline
#pipline 功能：
#“验 “爬取的数据（检验item是否有特定的Field）
#”检查“数据是否重复
#”储存“到数据库
'''
#启用 pipeline:
# 默认状态下pipline 是关闭的
# 在 settings.py 下，解除注销
ITEM_PIPELINES= {
    'shiyanlou.pipelines.shiyanloupipeline':300
    }

这是个字典， key 表示开启多个 pipeline 时它的执行顺序，值小先执行 通常在100～1000
'''

### 使用 scrapy 
# scrapy crawl courses(需要启动的spider)

### mysql 命令
# select * from courses(表名) limit 3\G  
# limit 3\G 显示前三个数据


##################
#使用 session 创建 数据库 session 
# sessionmaker(bind=)  engine
from sqlalchemy.orm import sessionmaker
from shiyanlou.models import Course,engine

class ShiyanlouPipeline(object):
    def process_item(self, item, spider):
        '''
        parse 出来的 item 会被传入这里，这里编写的处理代码会作用到每一个 item 上面。这个方法必须要返回一个 item 对象。
        '''
        #改变数据的类型并储蓄
        item['students'] = int(item['students'])

        ### 根据item 创建 Course Model 对象 并添加到 session 
        #itme 可以当成字典来使用，所以可以使用字典结构，
        # 相当于
        '''
        course{
            name = item['name'],
            type = item['type']
            }
        
        '''
        if item['students'] < 1000:
            raise DropItem('Course students less than 1000.')
        else:
            self.session.add(Course(**item))
        return item
    
    def open_spider(self,spider):
        # 在爬虫被开启时， 创建数据库 session
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self,spider):
        # 爬虫关闭后，提交 session ，关闭 session
        self.session.commit()
        self.session.close()
