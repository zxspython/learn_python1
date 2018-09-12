#两个测试用例子
# test_seve  ; test_delete
from rmon.models import Server

class TestServer:
    # 测试Server 相关功能
    def test_save(self,db):
        # 测试 Server.save 保存服务器方法
        assert Server.query.count() == 0
        server = Server(name='test',host='127.0.0.1')
        server.save()
        assert Server.query.count() == 1
        assert Server.query.first() == server

    def test_delete(self,db,server):
        # 测试 Server.dalete 删除服务器
        assert Server.query.count() == 1
        server.delete()
        assert Server.query.count() == 0
