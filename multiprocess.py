# !/usr/bin/env python3
# -*- config:utf-8 -*-

import os
from multiprocessing import Process

#定义一个函数，输入参数，打印参数，和所在的进程 id
def hello(name):
    # 使用os.getpid()获得当前进程id
    print('child process:{}'.format(os.getpid()))
    print('Hello' + name)

def main():
    #创建 Process 进程对象，参数为（进程里的函数target,函数的参数args）
    p = Process(target=hello,args=('shiyanlou',))
    #Process.start()方法，执行进程
    p.start()
    #.join()方法，等待子进程结束后继续执行
    p.join()
    print('parent process: {}'.format(os.getpid()))

if __name__ == '__main__':
    main()

