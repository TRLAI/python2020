#!/usr/bin/env python 
# -*- coding:utf-8 -*-
def classify_count2(arg):
    letters_num,table_num,figure_num,other_num=0,0,0,0
    for i in arg:
        if i.isalpha():
            letters_num+=1
        elif i.isdigit():
            figure_num+=1
        elif i.isspace():
            table_num+=1
        else:
            other_num+=1
    print("字符串中字母个数为：{}，空格个数为：{}，数字个数为：{}，其他字符个数为：{}".format(letters_num,table_num,figure_num,other_num))


if __name__ == '__main__':
    classify_count2("sjakhu（）*#")