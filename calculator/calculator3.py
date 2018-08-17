#! /usr/bin/env python3

import sys
import os
import csv

#获得各文件的地址 Args.get_c .get_d .get_o
class Args(object):
    def __init__(self):
        #获得除，执行文件外的所有字符串为一个列表
        args = sys.argv[1:]
        #列表args.index(x) 方法获得x元素的下标A
        #列表args[A]，获得地址  
        self.get_c = args[args.index('-c')+1]
        self.get_d = args[args.index('-d')+1]
        self.get_o = args[args.index('-o')+1]


#Args() 获得文件地址参数
args = Args()

#获取配置文件里的配置函数
class Config(object):

    def __init__(self):
        #对象self.config，使用._read_config()函数，
        #获得一个字典传入参书获得数值
        self.config = self._read_config()

    def _read_config(self):
        #创建一个字典，初始化一个数据
        config = {'s': 0}
        #打开文件
        with open(args.get_c) as f:
            #遍历每一行，获得每一行的 字符串 对象
            for line in f:
                #字符串   .strip() 去除两边空格； 
                #         .split('=') 以‘＝’将字符串变为列表
                a = line.strip().split('=')
                
                #判断列表第二个元素，小于1，则将 浮点数类型的值 相加
                #求出除了社保上下限以外的值的和
                if float(a[1].strip()) < 1:
                    config['s'] += float(a[1].strip())
                #将其余的 属性和值 放入 字典
                else:
                    config[a[0].strip()] = float(a[1].strip())
        #返回一个字典，可以传入 JiShuL ,JishuH,s 属性查数值
        return config


    #下面封装接口：self.JiShuL .JiShuH .s
    def JiShuL(self):
        return self.config['JiShuL']

    def JiShuH(self):
        return self.config['JiShuH']

    def s(self):
        return self.config['s']


#使用Args()文件地址，创建Config()，处理文件，获得社保参数
config = Config()


class UserData(object):
    
    #初始化对象时使用._read_users_data()方法 
    #.userdata属性获取员工的数据，数据类型为 列表
    def __init__(self):
        self.userdata = self._read_users_data()
    
    #获得员工信息列表
    def _read_users_data(self):
        #创建空列表
        userdata = []
        #每一行字符串,转化成列表
        #读取每一行
        with open(args.get_d) as f:
            for line in f:
                #字符串去䒈我去空格，以 ‘，’号分开成，列表
                a = line.strip().split(',')
                #列表的前两个值转为int类型，作为userdata列表的一个元素
                userdata.append((int(a[0]),int(a[1])))
        #返回一个userdata列表
        return userdata

#使用Args()文件地址，创建UserData(),处理文件，获得员工参数
userdata = UserData().userdata


#工资单数据
class Calculator(object):
 
    #计算 员工工资单数据
    def calc_for_all_userdata(self):
        line = []
        JiShuL = config.JiShuL()
        JiShuH = config.JiShuH()
        s = config.s()         
        for i in userdata:
            number = i[0]
            salary = i[1]
            #计算社保金 salary_security
            if salary < JiShuL:
                social_security = JiShuL * s
            elif salary >JiShuH:
                social_security = JiShuH * s
            else :
                social_security = salary * s
            #计算要交的税 tax
            #需要交税的钱 money_tex
            money_tax = salary - social_security - 3500
            if money_tax <= 0:
                tax = 0
            elif money_tax <= 1500:
                tax = money_tax * 0.03 - 0
            elif money_tax <= 4500:
                tax = money_tax * 0.1 - 105
            elif money_tax <= 9000:
                tax = money_tax * 0.2 - 555
            elif money_tax <= 35000:
                tax = money_tax * 0.25 - 1005
            elif money_tax <= 55000:
                tax = money_tax * 0.3 - 2755
            elif money_tax <= 80000:
                tax = money_tax * 0.35 - 5505
            else:
                tax = money_tax * 0.4 - 13505
            
            #计算最后工资
            # 最终工资 ＝ 工资－ 社保金 － 税收
            end_money =  salary - social_security - tax

            #将数据写入列表
            line.append((number,'{:.2f}'.format(salary),'{:.2f}'.format(social_security),'{:.2f}'.format(tax),'{:.2f}'.format(end_money)))
        return line

    #输出为 CSV 文件
    def export(self,default='csv'):
        #获得工资表
        result = self.calc_for_all_userdata()
        #写模式打开 文件
        with open(args.get_o,'w',newline='') as f:
            # csv 写文件
            writer = csv.writer(f)
            writer.writerows(result)

def main():    

    #使用Config(),UserData(),创建Calculator(),计算员工工资表，输出文件
    a = Calculator()
    a.export()
    print(a.calc_for_all_userdata())
    print(args.get_o)
if __name__ == '__main__':
    main()
