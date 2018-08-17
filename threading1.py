'''
获得线程的id：
threading.get_ident()

生成一个线程：
threading.Thread(target,args)

'''




# !/usr/bin/env python3
# -*- config:utf-8 -*-
import os
import threading

def hello(name):
    #.get_ident 获得当前线程 id
    print('child thread:{}'.format(threading.get_ident()))
    print('process:{}'.format(os.getpid()))
    print('Hello'+ name)

def main():
    #初始化一个线程，（target，args)
    t = threading.Thread(target=hello,args=('shiyanlou',))
    t.start()
    t.join()
    print('main thread:{}'.format(threading.get_ident()))

if __name__ == '__main__':
    main()
