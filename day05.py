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
#我们可以通过rang（） 生成100万个元素的列表，但是如果我们仅仅需要前面的几个元素参与计算，那么会浪费大量的内存空间，
#python中有一边循环一边计算的机制，成为生成器：generator
L = [x * x for x in range(1,11)]
print(L)
#我们只要将[] 改为（） 就是一个generator
g = (x * x for x in range(1,11))
print(g)
print(next(g))#通过next() 函数获得 generator 下一个值
for x in g:
    print(x)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
fib(5)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
#如果函数中包含yield关键字，那个这个函数就不再是一个普通的函数，而是一个generator
#这里难理解的是 generator和函数的执行流程不一样，函数是顺序执行，遇到return 语句或者最后一行函数语句就返回。而变成generator
#在那次调用next()的时候执行，遇到yield语句返回，再次执行时候从上次返回的yield语句处继续执行