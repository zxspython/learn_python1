# rmon.config 

# rmon 配置文件


import os


# 开发环境的 配置
class DevConfig:

    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #配置数据库地址为 sqlit3 内存地址，flask app 退出后数据就会丢失。
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    TEMPLATES_AUTO_RELOAD = True

# 生产环境的配置
class ProductConfig(DevConfig):
    DEBUG = False

    path = os.path.join(os.getcwd(),'rmon.db').replace('\\','/')
    #改变数据地址，为项目目录下的 rmon.db.全路径 /home/shiyanlou/Code/rmon/rmon.db。
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % path
