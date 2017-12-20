#!/usr/lib/env python3
# -*- coding:utf-8 -*-
names = 'xiakai summer'
#取出来？ 改动？ 不好整

names = ['xiakai','summer','A','B']
#1.切片 查
print(names);#['xiakai', 'summer']

print(names[0],names[1])#xiakai

print(names[1:2])#['summer']
print(names[1:3])#['summer', 'A']  切片前闭后开
print(names[3])#B 切片
print(names[-2])#A 切片
#print(names[-1:-3]) error 应该从左往后数
print(names[-3:-1])#['summer', 'A'] 前闭后开
print(names[-3:])#['summer', 'A', 'B']
print(names[:3])#['xiakai', 'summer', 'A']

#2.插入， 没有批量插入
names.append('C')
print(names)#['xiakai', 'summer', 'A', 'B', 'C']
#放在随意的位置
names.insert(1,'D')
print(names)#['xiakai', 'D', 'summer', 'A', 'B', 'C']

#3.改
names[2] = 'E'
print(names)#['xiakai', 'D', 'E', 'A', 'B', 'C']

#4删除
names.remove('E')
print(names)#['xiakai', 'D', 'A', 'B', 'C']
del names[1]
print(names)#['xiakai', 'A', 'B', 'C']

names.pop() #删除最后一个
print(names)#['xiakai', 'A', 'B']
#del names[1] = names.pop(1)

#各种方法
print(names.index('A'))#1
print(names[names.index('A')])
names.append('A')
print(names.count('A'))#2
names.clear()
print(names)#[]

names.append('Summer')
names.append('A')
print(names)#['Summer', 'A']
names.reverse()
print(names)#['A', 'Summer']
names.sort()
#合并
names2=[1,2,3,4]
names.extend(names2)
print(names)
print(names2)
#删掉names2变量
del names2

#print(names2)#name 'names2' is not defined

names2 = names.copy()
print(names)#['A', 'Summer', 1, 2, 3, 4]
print(names2)#['A', 'Summer', 1, 2, 3, 4]
names[1] = '夏天'
print(names)#['A', '夏天', 1, 2, 3, 4]
print(names2)#['A', 'Summer', 1, 2, 3, 4]


names.append([1,3,2])#['A', '夏天', 1, 2, 3, 4, [1, 3, 2]]
print(names)
names[6][0] = 'A'
print(names)#['A', '夏天', 1, 2, 3, 4, ['A', 3, 2]]#里面中的list实际上是一个内存地址

import copy
names2 = copy.deepcopy(names)#这里存在一个深copy和一个浅copy的事情
print(names2)#这样names2就是一个独立的了

#列表的循环
for i in names:
    print(i)

#range(1,10,2)
#步长的切片
print(names)#['A', '夏天', 1, 2, 3, 4, ['A', 3, 2]]
print(names[0:-1:2])#从0切到最后一个，跳着切 ['A', 1, 3] 0和-1可以省略
print(names[::2])#['A', 1, 3, ['A', 3, 2]]
print(names[:])#['A', '夏天', 1, 2, 3, 4, ['A', 3, 2]]

#浅copy 和深copy
#浅copy names2 中的元素是names 中元素的引用

person = ['name',['A','B']]
#浅copy的三种实现方式
p1 = copy.copy(person)
p2 = person[:]
p3 = list(person)

per1 = person[:]
per2 = person[:]
print(per1)
print(per2)
per1[0] = 'Summer'
per2[0] = '夏天'
print(per1)
print(per2)

per1[1][1] = 'C' #里面的列表中的数据进行了更改
print(per1)#['Summer', ['A', 'C']]  
#mmp讲的这个复杂 实际上就是person中的list存储的是一个引用，这个引用指向的内存不管在哪里进行
#更改，对于全局都是有效的
print(per2)#['夏天', ['A', 'C']]



