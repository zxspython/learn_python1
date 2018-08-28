'''
  知识点：
  sys 模块
      sys.argv 获得命令行参数

  socket 模块
      s = socket.socket() 生成对象
      s.settimeout(0.1) 设置超时，防止脚本卡住
      s.connect_ex(IP,port) 判断端口是否打开的方法 .connect_ex()
'''

#!/usr/bin/env python3
#-*- conding:utf-8 -*-

import sys
import socket

#获得参数 地址host 端口port 
def get_args():
    args = sys.argv[1:]

    try:
        #获得 命令行中 --host 和 --port 的索引号
        host_index = args.index('--host')
        port_index = args.index('--port')
        
        #获得对应的 host post 参数
        host_temp = args[host_index + 1]
        port_temp = args[port_index + 1]
        
        #确保ip地址为四位数字
        if len(host_temp.split('.')) !=4 :
            print('Parameter Error')
            exit()
        else:
            host = host_temp

        #判断post 参数是个数字还是 一个范围
        #一个范围，将前后数字生成一个列表
        if '-' in port_temp:
            port = port_temp.split('-')
        #不是一个范围，将两个相同的端口数值 ,放入列表。
        else:
            port = [port_temp,port_temp]

        return host,port
    except(ValueError,IndexError):
        print('Parameter Error')
        exit()


#扫描函数
def scan():
    #获得host port 
    host = get_args()[0]
    port = get_args()[1]

    #创建一个列表，记录端口开放的端口
    open_list = []

    #从port 列表里取出端口范围，遍历
    for i in range(int(port[0]),int(port[1]) + 1):
        #创建socket 对象
        s = socket.socket()

        #设置超时，防止脚本卡住
        s.settimeout(0.1)

        #使用 socket 对象的.connect_ex(host,port) 方法，判断目标IP 的端口是否打开

        if s.connect_ex((host,i)) == 0:
            open_list.append(i)
            print(i,'open')
        else:
            print(i,'closed')
        s.close()
    print(open_list)
    print('Complted scan. Opening ports at {}'.format(open_list))

if __name__ == '__main__':
    scan()

        


