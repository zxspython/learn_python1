'''
  reģ�飺
      re.findall(pattern,string) ͨ��ĳ��ģʽ(pattern),�ָ�string,����list

  collections����Counterģ��
      Counter(list) ����һ���ֵ�[('Ԫ��',����)]

  datetimeģ�飺������������
      �ַ���ʱ�� ��ʽ����datetime.strptime(string,format) 
      ��ʽ��ʱ�� �ַ�����datetime.strftime(format)

'''

#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re
from datetime import datetime
from collections import Counter

#ʹ��������ʽ������־�ļ������������б�
def open_parser(filename):
    with open(filename) as logfile:
        #ʹ��������ʽ������־�ļ�
        #\dƥ������ \sƥ������հ׷� \wƥ����ĸ�����»��� /�����
        #() ���淽��Ҫ���������
        pattern = (
                   r'(\d+.\d+.\d+.\d+)\s-\s-\s'#ƥ��IP
                   r'\[(.+)\]\s'  #ƥ��ۣ������� Ҳ��������ʱ��
                   r'"GET\s(.+)\s\w+/.+"\s'  #����·��
                   r'(\d+)\s'   #״̬��
                   r'(\d+)\s'   #���ݴ�С
                   r'"(.+)"\s'  #����ͷ
                   r'"(.+)"'    #�ͻ�����Ϣ
                  )
        parsers = re.findall(pattern,logfile.read())
        return parsers

#ɸѡ��������������
def logs_count():

    logs = open_parser('/home/shiyanlou/Code/nginx.log')
    print(logs[1])
    ip_list = []
    request404_list = []
     
    for log in logs:

        dt = datetime.strptime(log[1][:-6],"%d/%b/%Y:%H:%M:%S")
        #�ҵ�2017.1.11������
        if int(dt.strftime("%d")) == 11:
            #��ӵ��յ�IP ���б���
            ip_list.append(log[0])

        #��ȡ״̬��Ϊ 404 ������
        if int(log[3]) == 404:
            #���������ʵ�·�����б���
            request404_list.append(log[2])
    return ip_list,request404_list

def main():
    #�����б�ͳ��ÿ�����ݳ��ֵĴ���
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
