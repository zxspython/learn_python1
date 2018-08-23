#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#sys ,在命令行上获取参数，user_id:  sys.argv[1]
import sys
#pymongo 导入mongoclient 连接数据库
from pymongo import MongoClient
# 引用pandas 数据数据框架 DataFrame处理数据
import pandas as pd


#获得排位，分数，时间
def get_rank(user_id):
    #关联 MongoClient 数据库
    client = MongoClient()
    #关联 数据库 shiyanlou
    db = client.shiyanlou
    #关联 表 contests
    contests = db.contests
    
    #使用 pandas.DataFrame数据框架，传入 列表
    data = pd.DataFrame(list(contests.find()))

    #data['user_id'] 获得所有 user_id
    #判断传入参数是否在列表里
    if user_id in list(data['user_id']):
        #找出以 相同user.id 的用户数据，计算总 score and submit_time 
        group_data = data.groupby(['user_id'])['score','submit_time'].sum()
        #以 score and submit_time 数值大小排序
        rank_data = group_data.sort_values(['submit_time']).sort_values(['score'],ascending=False)
        #导出排名后的索引
        reindex_data = rank_data.reset_index()
        #在reindex_data表中创建一列 作为排名序号
        reindex_data['rank'] = reindex_data.index + 1

        #在表reindex_data 中查找 User.id匹配的数据
        user_data = reindex_data[reindex_data['user_id'] == user_id]
        rank = int(user_data['rank'].values)
        score = int(user_data['score'].values)
        submit_time = int(user_data['submit_time'].values)

    else:
        print('NotFound')
        exit()
    return rank,score,submit_time


if __name__ == '__main__':
    #判断是否有两个参数
    if len(sys.argv) != 2 :
        print('Parameter Error')
        #退出执行
        sys.exit(1)
    user_id = int(sys.argv[1])
    userdata = get_rank(user_id)
    print(userdata)
