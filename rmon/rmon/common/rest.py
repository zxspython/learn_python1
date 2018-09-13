#-*- conding:utf-8 -*-
#!/usr/bin/env python3
'''
rmon.common.rest

'''

class RestException(Exception):
    #??????????

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
