#-*- coding:utf-8 -*-
import os # 导入os模块，模块的概念后面讲到
from collections import Iterable,Iterator
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
#在那次调用next()的时候执行，遇到yield语句返回，再次执行时候从上次返回的yield语句处继续执行.
print('************************** yield **********')
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 1
    print('step 3')
    yield 1
o = odd()
next(o)
next(o)
print('************************** end ***************')
for n in fib(6):
    print(n)
#但是在for循环调用generator 时，发现拿不到generator的return 语句的返回值，如果想要拿到返回值，必须捕捉StopIteration错误，返回值包含在StopIteration的value中：
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break
#要理解generator 的工作原理：他是在for 循化的过程中不断计算处下一个元素，并在适当的条件结束for循环，对于函数改成generator
#来说， 遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束


####？？？
def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i-1]+L[i] for i in range(len(L))]

n=0
a = input("请输入杨辉三角的行数：")
for t in triangles():
    print(t)
    n = n+1
    if n == int(a):
        break

#3.迭代器
#直接作用于for循环的数据类型有以下几种
#一类是集合数据类型 ：如 list tuple dict set str
#一类是：generator，包括生成器和待yield的generator function
#这些可以直接作用于for循化的对象可成为迭代对象：Iterable/
#可以使用isinstance()判断一个对象是Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))
print(isinstance(100, int))
#而生成器不但可以作用于for循环，还可以被next（）函数不断调用并返回下一个值，直到最后抛处StopIteration 错误并表示无法执行下一个值了
#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
#可以使用isinstance()判断一个对象是否是Iterator对象：
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
print(isinstance((x for x in range(10)), Iterator))
print(isinstance(100, Iterator))
print(isinstance(100, Iterator))
#generator(生成器)都是Iterator（迭代器）对象，但是list，dict ,str 虽然是Iterable 但是不是Iterator
#把list dict str 等Iterable 变成Iterator可以使用 iter()函数获得一个Iter()函数获得一个Iterator对象

#python 的本质是通过不断调用next()函数实现的
for x in [1, 2, 3, 4, 5]:
    pass
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break