#!/usr/lib/env python
#-*- coding: utf-8 -*-

#当我们需要定义常量的时候，一个办法是用大写变量通过整数来定义，例如月份：
'''JAN = 1
FEB = 2
MAR = 3
...
NOV = 11
DEC = 12'''

#更好的办法就是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。
#Python 提供了Enum 类来实现这个功能
from enum import Enum,unique
Month = Enum('month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#这样就获得了 Month类型的枚举类，可以直接使用 Month.Jan 来引用一个常量，或者枚举它的所有成员:

for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)
#value 属性则是自动赋给成员的int常量，默认从1 开始计数。
'''Jan => month.Jan , 1
Feb => month.Feb , 2
Mar => month.Mar , 3
Apr => month.Apr , 4
May => month.May , 5
Jun => month.Jun , 6
Jul => month.Jul , 7
Aug => month.Aug , 8
Sep => month.Sep , 9
Oct => month.Oct , 10
Nov => month.Nov , 11
Dec => month.Dec , 12
'''
#如果需要更加年精确的控制枚举类型，可以从Enum派生出自定义类
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
#@unique 装饰器，可以帮助我们检查有没有重复的值

#访问这些枚举类型可以用多种方法
print('------------------------------------')
day1 = Weekday.Mon
print(day1)#Weekday.Mon

print(Weekday.Tue)#Weekday.Tue

print(Weekday['Tue'])#Weekday.Tue

print(Weekday.Tue.value)#2

print(day1 == Weekday.Mon)#True

print(day1 == Weekday.Tue)#False

print(Weekday(1))#Weekday.Mon

print(day1 == Weekday(1))#True

#小结：
#Enum 可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较

