'''
创建对象
pool = Pool(processes=,)

使用对象
pool.apply(函数,参数)
'''



# !/usr/bin/env python3
# -*- config:utf-8 -*-

from multiprocessing import Pool

def f(i):
    print(i,end='')

def main():
    #初始化一个3个进程的进程池
    pool =  Pool(processes=3)

    for i in range(30):
        #调用 apply方法开始处理任务，参数为f(任务函数)，i(参数)
        pool.apply(f,(i,))
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
