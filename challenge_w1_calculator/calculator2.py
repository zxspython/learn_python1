#!/usr/bin/env python3


import sys

def tax(salary):  # 计算工资
    star_money = 3500
    tax_rate =[0.03,0.1,0.2,0.25,0.3,0.35,0.45]
    tax_dedution = [0,105,555,1005,2755,5505,13505]
    
    tax_money = salary * (1-0.165) - star_money
    if tax_money > 0:
        if tax_money <= 1500:
            i = 0
        elif tax_money <= 4500:
            i = 1
        elif tax_money <= 9000:
            i = 2
        elif tax_money <= 35000:
            i = 3
        elif tax_money <= 55000:
            i = 4
        elif tax_money <= 80000:
            i = 5
        else :
            i = 6
        tax = tax_money * tax_rate[i] - tax_dedution[i]
    else:
        tax = 0
    return tax


#获取输入（转化）并生成列表
tax_list = sys.argv[1:]
man_dic = {}
#print(tax_list)
try:
    for man in tax_list:
        number,salary = man.split(":")
        # print(number,salary)
        man_dic[int(number)] = int(salary)
except:
    print("Paramete Error")

#计算税后工资，并生成列表

for number,salary in man_dic.items():
    man_dic[number] = salary - tax(salary) - salary*0.165

#打印新列表：
for number,tax_end in man_dic.items():
    print("{}:{:.2f}".format(number,tax_end))
