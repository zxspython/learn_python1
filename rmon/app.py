# -*- conding:utf-8 -*-
#!/usr/bin/env python3
import urllib
from rmon.app import create_app
from rmon.models import db
# 使用FLASK_APP=app.py flask run 启动时 调用 app.py 文件中的 flask 应用。
app = create_app()



#app.cli.command 装饰器，使得 FLASK_APP=app.py flask init_db 可以执行init_db函数。
@app.cli.command()
def init_db():
    '''
    初始化数据库
    '''
    print('sqlite3 database file is %s'% app.config['SQLALCHEMY_DATABASE_URI'])
    db.create_all()
