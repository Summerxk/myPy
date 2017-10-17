#-*- coding:utf-8 -*-
#再我们传入函数的时候，有时候不需要显示的定义函数，直接传入匿名函数更方便
#以map()函数为例，计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：
L = list(map(lambda x:x*x,[1,2,3,4,5]))
print(L)
#可以看出匿名函数lambda x:x * x 就是函数
def f(x):
        return x * x
#关键字，lambda 表示匿名函数，冒号前面的x参数，表示函数的参数

#匿名函数有个限制，就是只能有一个表达式，不用写return,返回值就是该表达式的结果
#用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
f = lambda x: x * x
print(f)#<function <lambda> at 0x7f7c120f50d0>
print(f(5))#25

#可以把匿名函数作为返回值返回，比如：
def build(x, y):
    return lambda x,y: x * x + y * y
#python 对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数
a = build(3,5)
print(a)#<function build.<locals>.<lambda> at 0x7f3b2cf551e0>
print(a(3,5))