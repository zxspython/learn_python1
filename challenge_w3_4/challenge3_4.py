'''
  re模块：
      re.findall(pattern,string) 通过某种模式(pattern),分割string,生成list

  collections包，Counter模块
      Counter(list) 返回一个字典[('元素',个数)]

  datetime模块：处理日期数据
      字符串时间 格式化：datetime.strptime(string,format) 
      格式化时间 字符化：datetime.strftime(format)

'''

#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re
from datetime import datetime
from collections import Counter

#使用真则表达式解析日志文件，返回数据列表
def open_parser(filename):
    with open(filename) as logfile:
        #使用正则表达式解析日志文件
        #\d匹配数字 \s匹配任意空白符 \w匹配字母数字下划线 /定界符
        #() 里面方需要提出的数据
        pattern = (
                   r'(\d+.\d+.\d+.\d+)\s-\s-\s'#匹配IP
                   r'\[(.+)\]\s'  #匹配［］中内容 也就是请求时间
                   r'"GET\s(.+)\s\w+/.+"\s'  #请求路径
                   r'(\d+)\s'   #状态码
                   r'(\d+)\s'   #数据大小
                   r'"(.+)"\s'  #请求头
                   r'"(.+)"'    #客户端信息
                  )
        parsers = re.findall(pattern,logfile.read())
        return parsers

#筛选符合条件的数据
def logs_count():

    logs = open_parser('/home/shiyanlou/Code/nginx.log')
    print(logs[1])
    ip_list = []
    request404_list = []
     
    for log in logs:

        dt = datetime.strptime(log[1][:-6],"%d/%b/%Y:%H:%M:%S")
        #找到2017.1.11的数据
        if int(dt.strftime("%d")) == 11:
            #添加当日的IP 到列表中
            ip_list.append(log[0])

        #获取状态码为 404 的数据
        if int(log[3]) == 404:
            #返回他访问的路径到列表中
            request404_list.append(log[2])
    return ip_list,request404_list

def main():
    #处理列表，统计每个数据出现的次数
    ip_count = Counter(logs_count()[0])
    request404 = Counter(logs_count()[1])
 
    sorted_ip = sorted(ip_count.items(),key=lambda x:x[1])
    sorted_request404 = sorted(request404.items(),key=lambda x:x[1])

    ip_dict = dict([sorted_ip[-1]])
    url_dict = dict([sorted_request404[-1]])

    return ip_dict,url_dict

if __name__ == '__main__':
    ip_dict,url_dict = main()
    print(ip_dict,url_dict)
