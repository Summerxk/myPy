#高阶函数
#函数本身可以赋值给变量，即变量可以指向函数
f = abs
x = f(-10)
print (x)
#既然变量可以指向函数，函数的参数能接收变量，
#那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def test(x,y,f):
    return f(x)+f(y)
f =  test(-1,-2,abs)
print (f)

#编写高阶函数，就是让函数的参数能够接收别的函数。
#把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。

#map()/reduce()函数
#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x * x
list = map(f,[1,2,3,4,5,6,7,8,9])
for i in list:
    print(i)
list = map(str,[1,2,3,4,5])
for x in list:
    print(x)

#看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce

def add(x,y):
    return x+y
a = reduce(add,[1,2,3])
print(a)

#map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(x):
    return x % 2 == 1
list = (filter(is_odd,[1,2,3,4,5,6,7,8]))
for x in list:
    print(x)
#Python内置的sorted()函数就可以对list进行排序：
#list = sorted([36, 5, -12, 9, -21])
list = sorted([36, 5, -12, 9, -21], key=abs)
for x in list:
    print (x)

