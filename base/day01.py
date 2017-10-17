# -*- coding: utf-8 -*-
#1.数据类型和变量
#2.使用list 和 tuple
classmates = ['summer','winter']
print(classmates)
#2.1长度
print("classmates length:", len(classmates))
#2.2 获取每一个元素
print("第一个元素为",classmates[0])
#2.3 获取最后一个元素
print("最后一个元素为：" ,classmates[-1])
#2.4 list是一个可变的有序列表，所以list中追加元素到末尾
classmates.append('xiakai')
print(classmates)
#2.5 在固定的位置添加一个元素
classmates.insert(0,'heihei')
print(classmates)
#2.5 删除list的末尾的元素,和固定位置的元素
classmates.pop()
classmates.pop(0)
print(classmates)
#2.6 可以将某个索引位置的元素替换为别的元素 
classmates[0] = 'Summer_xk'
print(classmates)
#2.7 list 中的元素也可以不相同
L = ['summer',1,True]
print("不同的数据元素：",L)
#2.8 list 中也可以放入另一个lit
s = ['difference list', L, classmates]
print(s)

#2.9tuple 另外一种有序列表叫做元组 tuple 类似于final 一但初始化 不能做更改
#2.9.1 example 有个事情 当tuple中的元素只有一个的时候 （） 按照小括号进行表示
t = (1)
print("这时候输出的就是：",t,"并不是（1）")
print("需要注意的一点是 tuple 所指的不变是指指向的不变，并不是元素的不变，当元素中有list的时候可以改变")
t = ('1','2',['3','4'])
print(t)
t[2][0] = '5'
print(t)

summery = '好吧，做一个总结：类似java中的数组，有list，tupe ,list有API len,append,insert,pop List 中可一个放不同的元素集合，tuple 不可改变的是指向的内存空间'
print(summery)

#3.条件的判断
print('if , elif, else')
age = 3
if age >= 18:
    print('you name is:',age)
    print('adult')
else:
    print('teenager')
print('注意不要少写了冒号： python 中没有大括号 if 后面不用小括号')

#4.循环 
names = ['s','u','m','m','e','r']
for name in names:
    print(name)

#5.使用dict 和 set
#5.1 dict 类似HashMap
#5.1.1
print('在python中的dict相当于map （k-v）存储')
d_5 = {'summer':'prefect','Pennix':'good','fengjunjie':'....'}
print(d_5)
print(d_5['summer'])
print('for in 也可用于 dict的遍历')
for face in d_5:
    print(face)
#5.1.2将指定的value 放入 key中
d_5['summer'] = '太他吗的帅了'
print(d_5)
d_5['fengjunjie'] = classmates# 可以将list 放入key中
print(d_5)
#5.1.3也可用get获取
print(d_5['summer'])
print(d_5.get('summer'))
#5.1.4删除
d_5.pop('fengjunjie')
print(d_5)

#5.2 set :set 存不可重复的元素
#5.2.1 add 
s = set([1,2,3,4])
print(s)
s.add(5)
print(s)
#5.2.2 remove
s.remove(5)
print(s)
#5.2.3 & |
s2 = set([1,3])
print(s & s2)
s3 = set([4,5])
print(s2 | s3)

