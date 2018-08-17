# !/usr/bin/env python3
# -*- config:utf-8 -*-

from multiprocessing import Process,Queue

#一个可以在多进程下使用的queue(队列)结构,maxsize最大容量
queue = Queue(maxsize=10)

def f1(q):
    q.put('Hello shiyanlou')
    print('f1')    

def f2(q):
    data = q.get()
    print(data)
    # Queue.empty()方法判断队列是否为空，空时返回True
    if q.empty():
        print('Queue is empty')

#args的参数是列表
def main():
    Process(target=f1,args=(queue,)).start()
    Process(target=f2,args=(queue,)).start()

if __name__ == '__main__':
    main()
