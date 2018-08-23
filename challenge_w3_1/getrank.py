#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#sys ,���������ϻ�ȡ������user_id:  sys.argv[1]
import sys
#pymongo ����mongoclient �������ݿ�
from pymongo import MongoClient
# ����pandas �������ݿ�� DataFrame��������
import pandas as pd


#�����λ��������ʱ��
def get_rank(user_id):
    #���� MongoClient ���ݿ�
    client = MongoClient()
    #���� ���ݿ� shiyanlou
    db = client.shiyanlou
    #���� �� contests
    contests = db.contests
    
    #ʹ�� pandas.DataFrame���ݿ�ܣ����� �б�
    data = pd.DataFrame(list(contests.find()))

    #data['user_id'] ������� user_id
    #�жϴ�������Ƿ����б���
    if user_id in list(data['user_id']):
        #�ҳ��� ��ͬuser.id ���û����ݣ������� score and submit_time 
        group_data = data.groupby(['user_id'])['score','submit_time'].sum()
        #�� score and submit_time ��ֵ��С����
        rank_data = group_data.sort_values(['submit_time']).sort_values(['score'],ascending=False)
        #���������������
        reindex_data = rank_data.reset_index()
        #��reindex_data���д���һ�� ��Ϊ�������
        reindex_data['rank'] = reindex_data.index + 1

        #�ڱ�reindex_data �в��� User.idƥ�������
        user_data = reindex_data[reindex_data['user_id'] == user_id]
        rank = int(user_data['rank'].values)
        score = int(user_data['score'].values)
        submit_time = int(user_data['submit_time'].values)

    else:
        print('NotFound')
        exit()
    return rank,score,submit_time


if __name__ == '__main__':
    #�ж��Ƿ�����������
    if len(sys.argv) != 2 :
        print('Parameter Error')
        #�˳�ִ��
        sys.exit(1)
    user_id = int(sys.argv[1])
    userdata = get_rank(user_id)
    print(userdata)
