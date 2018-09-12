#初始化falsk 应用的代码

import os
from flask import Flask

#导入蓝图 api
from rmon.views import api
#导入 SQLAlchemy 对象
from rmon.models import db
#配置类
from rmon.config import DevConfig,ProductConfig

def create_app():
    app = Flask('rmon')

    #根据不同的环境变量（RMON_ENV）值 选择开发环境
    env = os.environ.get('RMON_ENV')

    if env in ('pro','prod','product'):
        app.config.from_object(ProductConfig)
    else :
        app.config.from_object(DevConfig)
    

    app.config.from_envvar('RMON_SETTINGS',silent=True)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    #在Flask 类中注册 蓝图 
    app.register_blueprint(api)
    #使用了flask_sqlalchemy 扩展，db.init_app(app)会自动在配置文件中查找
    #SQLALCHEMY_DATABASE_URI 配置项 配置数据库地址。
    db.init_app(app)
    
    #开发环境中，自动在 内存数据库中创建数据库。
    if app.debug:
        with app.app_context():
            db.create_all()
    return app
