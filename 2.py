#!/usr/bin/env python
# -*- coding:utf-8 -*-
num=input("请输入当月利润:(unit is million)\n")
num2=float(num)
if num2<=0:
    print("输入有误!")
elif num2<=10:
    print ("奖金为%f元."%(num2*1.1),end=" ")
elif num2<=20:
     print ("奖金为%f元."%(11+(num2-10)*1.075),end=" ")
elif num2<=40:
    print ("奖金为%f元."%(21.75+(num2-20)*1.05),end=" ")
elif num2<=60:
    print ("奖金为%f元."%(42.75+(num2-40)*1.03),end=" ")
elif num2<=100:
    print ("奖金为%f元."%(63.35+(num2-60)*1.015),end=" ")
else:
    print ("奖金为%f元."%(103.95+(num2-100)*1.01),end=" ")