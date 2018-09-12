import pytest

from rmon.app import create_app
from rmon.models import Server
from rmon.models import db as database

#db 继承 app; server继承db;因为 db 依赖于 app;server依赖于app :解决了依赖问题；
@pytest.fixture
def app():
    return create_app()

# 这里使用了 yield关键字，每创建数据库，通过database.drop_all()销毁数据库
@pytest.yield_fixture
def db(app):
    with app.app_context():
        database.create_all()
        yield database
        database.drop_all()

@pytest.fixture
def server(db):
    server = Server(name='redis_test',description='this is a test record',
            host= '127.0.0.1',port='6379')
    server.save()
    return server
