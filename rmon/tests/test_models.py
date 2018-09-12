#��������������
# test_seve  ; test_delete
from rmon.models import Server

class TestServer:
    # ����Server ��ع���
    def test_save(self,db):
        # ���� Server.save �������������
        assert Server.query.count() == 0
        server = Server(name='test',host='127.0.0.1')
        server.save()
        assert Server.query.count() == 1
        assert Server.query.first() == server

    def test_delete(self,db,server):
        # ���� Server.dalete ɾ��������
        assert Server.query.count() == 1
        server.delete()
        assert Server.query.count() == 0
