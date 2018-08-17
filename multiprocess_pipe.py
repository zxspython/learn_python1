# !/usr/bin/env python3
# -*- config:utf-8 -*-

from multiprocessing import Process,Pipe

#Pipe连接两个进程，返回一个tuple(元组)，管道为全双工的：任何一段send(写)，recv(读)数据
#conn1,conn2是进出口
conn1,conn2 = Pipe()

def f1():
    conn1.send('Hello shiyanlou')
    print('f1 process:{}'.format(get))

def f2():
    data = conn2.recv()
    print(data)

def main():
    Process(target=f1).start()
    Process(target=f2).start()

if __name__ == '__main__':
    main()
