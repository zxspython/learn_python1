#!/usr/bin/env python3

import sys
star_money = 3500
tax_rate = [0.03,0.1,0.2,0.25,0.3,0.35,0.45]
tax_deduction = [0,105,555,1005,2755,5505,13505]
try:
    salary = int(sys.argv[1])
    tax_money = salary - star_money
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
        tax = tax_money * tax_rate[i] - tax_deduction[i]
    else:
        tax = 0
    print(format(tax,".2f"))  
except:
    print("Parameter Error")
