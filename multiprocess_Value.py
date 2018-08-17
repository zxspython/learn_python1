# !/usr/bin/env python3
# -*- config:utf-8 -*-

import time
from multiprocessing import Process,Value,Lock

def func(val):
    for i in range(50):
        time.sleep(0.01)
        ###
        # with lock语句是对下面语句的缩写：
        #
        #lock.acquire()     acquire 获得
        #val.value +=1
        #lock.release()     release 释放
        with lock:
            val.value += 1
        ###
if __name__ == '__main__':
    #多进程无法使用全局变量,multiprocessing提供的 Value是一个代理器，可以实现多进程中共享这个变量
    #参数 'i'指的是ctyps.c_int就是整数，0是Value对象共享的值，在进程中可以通过val.value获得
    v = Value('i',0)
    #创建一个进程列表
    ### 初始化锁
    lock = Lock()
    ###
    procs = [Process(target=func,args=(v,)) for i in range(10)]
    
    #执行进程
    #由于多进程推进顺序是无法预测的，有可能几个进程对i＋1，但是CPU 和内存的机制造成只有一个＋1会被记录下来，结果可能小于500,需要加入lock.(详见＃＃＃)
    for p in procs:
        p.start()
    for p in procs:
        #等待子进程执行完后，再执行下面的操作
        p.join()

    print(v.value)
