#!/usr/bin/env python 
# -*- coding:utf-8 -*-
count = 0
for i in range(100, 1000):
    f = i
    a = int(f / 100)
    f -= a*100
    b = int(f / 10)
    c = f - b*10
    if a**3 + b**3 + c**3 == i:
        print(i)
        count += 1
print("共有 %d 个水仙花数" % count)