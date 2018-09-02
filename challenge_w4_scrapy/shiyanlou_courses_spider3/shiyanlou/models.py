# create_engine 绑定一个数据库（参数为数据库类型密码 编码）
from sqlalchemy import create_engine
# declarative_base 为创建 表格的基类
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer

engine = create_engine('mysql+mysqldb://root@localhost:3306/shiyanlou?charset=utf8')
Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer,primary_key=True)
    name = Column(String(64),index=True)
    description = Column(String(1024))
    type = Column(String(64),index=True)
    students = Column(Integer)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
