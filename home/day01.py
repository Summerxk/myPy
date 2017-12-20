#!/usr/lib/env python3
# -*- coding:utf-8 -*-
#Author:Summer
#两个标准库，一个 sys 一个os

import sys
print(sys.path)
print('summer')# 打印环境变量
print(sys.argv)#当前文件的相对路径
#print(sys.argv[2])#python day01.py 1 2 3 ---> 2
#python 中存在小数字池：-5--257

#三元运算
a,b,c = 1,3,5
d = a if a > b else c
print(d)

#bytes 类型
#在python3 里面二进制和 文本不能进行拼接

