#-*- coding:utf-8 -*-
import functools
#装饰器
#由于函数也是一个对象，而且函数对象也可以被赋值给变量，所以通过变量也能调用该函数
def summer():
    print('summer')

f = summer
print(f)#<function name at 0x7f93034eae18>
f()#summer

#函数对象有一个__name__ 属性，可以拿到函数的名字

print('summer函数名字',summer.__name__)
print('f函数名字',f.__name__)

#假设要增强summer函数的功能，比如，再函数调用前后自动打印日至，但又不希望修改now()函数的定义，这种再代码运行期间
#动态增加功能的方式，称之为‘装饰器(decorator)’

#再本质上，decorator就是一个返回函数的高阶函数，所以我们要定义一个能打印日至的decorator,可以这样定义
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' %func.__name__)
        return func(*args ,**kw)
    return wrapper
@log
def now(a):
    print('now is 2017-10-16',a)

now(11)
#call now():
#now is 2017-10-16

#把@log放到now()函数的定义处，相当于执行了语句：
print('...........')
now = log(now(1))
print(now)
print('...........')
#把@log放在decorator，返回一个函数，所以原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行
#新的函数，即在log()函数中返回的wrapper()函数。

#wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
#如果decorator本身需要传入参数，就需要编写一个返回decorator的高阶函数。比如
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s()' %(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print('summer')

now()
print(now.__name__)#wrapper
#这时候now 的__name__属性值 已经从now 变成了wrapper,因为返回的wrapper()函数名字就是wrapper，所以要把院士函数的
#__name__等属性赋值到wrapper()函数中，否则，有些以来函数签名的代码就会执行错误。

#一个完整的decorator的写法如下
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('Summer')
now()
print(now.__name__)
#或者带参数的
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
#在面向对象（OOP）的设计模式中，decorator被成为装饰模式，OOP的装饰模式，需要通过继承和组合来实现，而python除了能支持
#opp的decorator外，直接冲语法层次支持decorator,python 的decorator可以用函数实现，也可以用类进行实现
#decorator用来增强函数。
