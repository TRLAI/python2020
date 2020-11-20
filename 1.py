#!/usr/bin/env python 
# -*- coding:utf-8 -*-
a=['1','2','3','4']
b=[]
for i in a:
   print(i)
   for j in [x for x in a if x!=i]:
       print(j)
       for k in[x for x in a if x!=i and x!=j]:
         print(k)
         b.append(int(i+j+k))
print(b)
print('能组成%s个互不相同且无重复数字的三位数'%len(b))
