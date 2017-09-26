#-*- coding:utf-8 -*-
import os # 导入os模块，模块的概念后面讲到
#1.列表生成式
#列表生成器就是 list Comprehensions 是python内置的非常简单却强大的可以用来创建list的生成式
#1.1 举个列子 生成1-10的list集合
print(list(range(1,11)))
print([x * x for x in range(1,11)])
print([x * x for x in range(1,11) if x % 2 == 0])
#1.2生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])
#1.3列出当前的目录
print([d for d in os.listdir('.')])#os.listdir 可以列出文件和目录
print([d+'summer' for d in os.listdir('.')])#os.listdir 可以列出文件和目录
#输出的是 x * x ,m+n ,d  前面的是输出的
#1.4 for 循环其实可以通同时使用两个甚至更多的变量
d = {'X': 'A', 'Y': 'B', 'Z': 'C' }
print([k +'=' + v for k,v in d.items()])
#1.5 把数组里面的字符变成小写
print([k.lower() +'=' + v.lower() for k,v in d.items()])
#如果遍历的集合中，既有数字又有字母 会报错
L1 = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L1 if isinstance(s,str)])

#2.生成器