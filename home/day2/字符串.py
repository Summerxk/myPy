#!/usr/lib/env python3
# -*- coding:utf-8 -*-

name = 'summer'

print(name.capitalize())#Summer

print(name.count('m'))#2

print(name.casefold())

print(name.center(50,'-'))#----------------------summer----------------------

print(name.encode())#可以转为二进制

print(name.endswith('r'))#判断以什么结尾

n = 'my \tname is summer'
print(n.expandtabs(tabsize=8))#my      name is summer tab 打印多少个空格

print(name.find('m'))#2 查找index 第一个字母的地方  可以用这个进行字符串的切片

myname = 'my name is {name}, age is {age}'
print(myname.format(name = 'summer',age = '18'))#my name is summer, age is 18

print(myname.format_map({'name':'xiakai','age':'19'}))#my name is xiakai, age is 19

print('ab23'.isalnum())#包含数字字母 true

print('abA'.isalpha)#包含字母，大写

print('1.23'.isdecimal())#判断十进制

print('1A'.isdigit)#判断是不是整数

print('1A'.isidentifier())#判断是不是一个合法的变量名 

print('1A'.islower())#判断是不是小写

print('1A'.isnumeric())#判断是不是数字 小数不会为true 判断是不是只有数字在里面

print('1A'.isspace())#判断是不是空格

print('1A'.istitle())#判断是不是每个首字母大写

print('1A'.isprintable())#判断是不是能打印 tty file drive file

print('1A'.isupper())#是不是都是大写

print('='.join(['1','2']))#1=2 要进行拼接的放在前面

print(name.ljust(8,'*'))#summer** 8位 不够补齐
print(name.rjust(8,'*'))#**summer

print('summer'.upper())
print('SUMMER'.lower())

print('   \n Summer  \n  '.strip())#去掉空格和回车
print('   \n Summer  \n  '.lstrip())#去左边
print('   \n Summer  \n  '.rstrip())#去右边

p = str.maketrans('abcdef','123456')#写个随机的密码 可以这样转一下

print('abcSU'.translate(p))#123SU

print('Summer'.replace('m','M',1))#SuMmer

print('summer'.rfind('m'))#找到最后的那个m index返回 3

print('summer'.split('u'))#['s', 'mmer'] u被当成分隔符 u没了

print('summ\ner'.splitlines())#按照换行符进行换行，不同系统的换行不一样

print('SuMMer'.swapcase())#大小写换过来 sUmmER

print('Summer'.zfill(8))# 00Summer 位数不够的可以用0填充

