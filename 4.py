#!/usr/bin/env python 
# -*- coding:utf-8 -*-
def clonelist(li1):
    li_copy = list(li1)
    return li_copy


li1 = [1, 2, 3, 4, 5,6]
li2 = clonelist(li1)
print("原始列表:", li1)
print("复制后列表:", li2)