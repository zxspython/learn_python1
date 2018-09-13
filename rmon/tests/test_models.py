#-*- coding:utf-8 -*-
#!/usr/bin/env python
# test_seve  ; test_delete
from rmon.models import Server
from rmon.common.rest import RestException

class TestServer:
    def test_save(self,db):
        assert Server.query.count() == 0
        server = Server(name='test',host='127.0.0.1')
        server.save()
        assert Server.query.count() == 1
        assert Server.query.first() == server

    def test_delete(self,db,server):
        assert Server.query.count() == 1
        server.delete()
        assert Server.query.count() == 0

    def test_ping(self,db,server):
        assert server.ping() is True

    def test_ping_failed(self,db):

        server = Server(name='test',host='127.0.0.1',port=6399)
        try:
            server.ping()
        except RestException as e:
            assert e.code == 400
            assert e.message == 'redis server %s can not connected'% server.host

    def test_get_metrics(self,db,server):
        assert server.get_metrics()

    def test_get_metrics_failed(self,db):

        server = Server(name='test',host='127.0.0.1',port=6399)
        try:
            server.get_metrics()
        except RestException as e:
            assert e.code == 400
            assert e.message == 'redis server %s can not connected'% server.host
