#-*- conding:utf-8 -*-
#!/usr/bin/env python3
'''
rmon.common.rest

'''
from collections import Mapping
from flask import request,Response,make_response
from flask.json import dumps
from flask.views import MethodView

class RestException(Exception):
    # 作为 访问redis 时出错时返回的异常
    #创建方法 继承Exception 增加code message 属性
    def __init__(self,code,message):
        '''
        初始化异常
       
         Aargs(参数):
            code(int):http 状态码
            message(str): 错误码
        '''
        self.code = code
        self.message = message
        # RestException，继承RestException夫类__init__ 
        super(RestException,self).__init__()


class RestView(MethodView):

    content_type = 'application/json;charset=utf-8'
    method_decorators = []

    def handler_error(self,exception):
        #处理异常
        data = {
                'ok':False,
                'message':exception.message
        }

        result = dumps(data) + '\n'
        resp = make_response(result,exception.code)
        resp.headers['Content-Type'] = self.content_type
        return resp

    def dispath_request(self,*args,**kwargs):
        #取得 method,method is None 时 报错
        #
        method = getattr(self,request.method.lower(),None)

        if method is None and request.method == 'HEAD':
            method = getattr(self,'get',None)

        assert method is not None,'Unimplemented method %r'% request.method
        #########
        # 为 method 加 装饰器
        if isinstance(self.method_decorators,Mapping):
            decorators = self.method_decorators.get(request.method.lower(),[])
        else:
            decorators = self.method_decorators

        for decorator in decorators:
            method = decorator(method)
        ########
        # 使用 method() ,比如get方法， 生成 resp
        # 方法报错，将报错 用 handler_error 处理，身成一个 response
        try:
            resp = method(*args,**kwargs)
        except RestException as e:
            resp = self.handler_error(e)
        #######
        # 判断 resp 类型，不是Response 则继续处理，不是时为 method()类
        if isinstance(resp,Response):
            return resp
        #######
        # unpack 解开resp (method()),data,code,headers
        # 处理其中的数据 data,并序列化
        # 用 make_response()将data,code，生成 response
        data,code,headers = RestView.unpack(resp)

        if code >= 400 and isinstance(data,dict):
            for key in data:
                if isinstance(data[key],list) and len(data[key]) >0:
                    message = data[key][0]
                else:
                    message = data[key]
            data = {'ok':False,'message':message}
        result = dumps(data) + '\n'
        response = make_response(result,code)
        response.headers.extend(headers)

        response.headers['Content-Type'] = self.content_type
        
        return response
        #######
    #静态方法，RestView.unpack() 
    @staticmethod
    def unpack(value):
        headers = {}
        if not isinstance(value,tuple):
            return value,200,{}
        if len(value) == 3:
            data,code,headers = value
        elif len(value) == 2:
            data,code = value
        return data,code,headers


