#!/usr/lib/env python
#-*- coding: utf-8 -*-

#type()
#动态语言和静态语言的最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。

#比如说我们定义一个Hello 的class,就写一个hello.py模块
class Hello(object):
    def hello(self, name = 'world'):
        print('hello,%s' %name)
#当Python解释器载入hello模块时，就会依次执行该模块的所有的语句，执行结果就是动态创建一个Hello 的calss对象

#from hello import Hello
#h = Hello()
#h.hello()# hello,world.
#print(type(Hello))#<class 'type'>
#print(type(h))#<class 'hello.Hello'>

#type（）函数可以查看一个类型或者变量的类型，Hello是一个class,它的类型就是 type,而h是一个是哦里，它的类型就是 class Hello.

#class的定义是运行时动态创建的，而创建 class的方法就是使用 type()函数。

#type() 函数即可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过 type()函数创建出Hello类，而不用通过
# class Hello(object).... 的定义
print('----------- type create hello class ---------------')
def fn(self,name = 'world'):#先定义函数
    print('hello,%s' %name)
Hello = type('Hello',(object,),dict(hello = fn))#创建 Hello class
h = Hello()
h.hello()
print(type(Hello))#<class 'type'>

print(type(h))#<class '__main__.Hello'>

#要创建一个class对象，type()函数依次传入3个参数：
#1.class的名称
#2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，要用tuple的单元素写法
#3.class 的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上面

#metaclass
#除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。

#metaclass 元类 简单的解释就是：
#当我们定义了类以后，就可以根据这个类创建出实例，所以先定义类，然后创建实例。
#but 如果想直接创建出类，那必须根据mataclass创建出类，所以：先定义metaclass，然后创建类。
#连接起来就是：先定义metaclass，就可以创建类，最后创建实例
#所以，metaclass允许创建类或者修改类，换句话说，可以把类看成是metaclass创建出来的‘实例’

#好吧，mateclass是python面形对象中最难理解的。正常情况下，你不会碰到需要使用metaclass的情况，所以基本不会用到
#就瞅瞅
#https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319106919344c4ef8b1e04c48778bb45796e0335839000
