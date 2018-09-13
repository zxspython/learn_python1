#-*- conding:utf-8 -*-
#!/usr/bin/env python3
'''
rmon.common.rest

'''

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
