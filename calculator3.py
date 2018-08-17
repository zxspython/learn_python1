#! /usr/bin/env python3

import sys
import os
import csv

class Args(object):
    def __init__(self):
        args = sys.argv[1:]
        self.get_c = args[args.index('-c')+1]
        self.get_d = args[args.index('-d')+1]
        self.get_o = args[args.index('-o')+1]

args = Args()

class Config(object):

    def __init__(self):
        self.config = self._read_config()

    def _read_config(self):
        config = {'s': 0}
        with open(args.get_c) as f:
            for line in f:
                a = line.strip().split('=')
                if float(a[1].strip()) < 1:
                    config['s'] += float(a[1].strip())
                else:
                    config[a[0].strip()] = float(a[1].strip())
        return config



    def JiShuL(self):
        return self.config['JiShuL']

    def JiShuH(self):
        return self.config['JiShuH']

    def s(self):
        return self.config['s']

config = Config()

class UserData(object):
    
    def __init__(self):
        self.userdata = self._read_users_data()
    
    def _read_users_data(self):
        userdata = []
        with open(args.get_d) as f:
            for line in f:
                a = line.strip().split(',')
                userdata.append((int(a[0]),int(a[1])))
        return userdata
    
userdata = UserData().userdata


class Calculator(object):

    def userdata(self):
        line = []
        JiShuL = config.JiShuL()
        JiShuH = config.JiShuH()
        s = config.s()         
        for i in userdata:
            number = i[0]
            salary = i[1]
         #计算社保金
            if salary < JiShuL:
                social_security = JiShuL * s
            elif salary >JiShuH:
                social_security = JiShuH * s
            else :
                social_security = salary * s
         #计算tax
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
            end_money =  salary - social_security - tax
            line.append((number,'{:.2f}'.format(salary),'{:.2f}'.format(social_security),'{:.2f}'.format(tax),'{:.2f}'.format(end_money)))
        return line

    def export(self,default='csv'):
        result = self.userdata()
        with open(args.get_o,'w',newline='') as f:
            writer = csv.writer(f)
            writer.writerows(result)
print(args.get_o)
a = Calculator()
a.export()
print(a.userdata())
if __name__ == '__main__':
    pass
