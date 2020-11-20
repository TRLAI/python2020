#!/usr/bin/env python 
# -*- coding:utf-8 -*-
times = 10
height_sum = 100
height_list = [100]  # 第一次落下的高度为height_list[0]=100米
for i in range(1, times):
    # 每次下落的高度均为上次高度的一半
    height_list.append(height_list[i-1] / 2)
    height_sum += height_list[i] * 2

print("第10次落地时，共经过 %f 米" % height_sum)
# 第十次反弹的高度即第九次下落的高度一半
print("第10次反弹 %.8f 米" % (height_list[times - 1] / 2))