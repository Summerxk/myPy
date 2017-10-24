#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#在oop程序设计中，当我们定一个class的时候，可以从某个现有的class继续。新的class 称为字类（Subclass）
#而被继承class称为基类，或者父类（base class, super class）

#继承与java类似

class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    pass

class Cat(Animal):
    pass
dog = Dog()
dog.run()

cat = Cat()
cat.run()
#当字类和父类都存在相同的方法的时候，我们说，子类的方法覆盖了父类的方法，在代码运行时候，会调用子类的方法，这样我们就
#获取了继承的另一个好处，：多态

class Dog(Animal):
    
    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')

a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型
#静态语言 VS 动态语言
#对于静态语言，java 如果需要传入Animal类型，则传入的对象必须是Animal类型或者他的子类，否则，将无法调用run()方法。
#对于python这样的动态语言来说，则不需要传入Animal类型，我们只需要保证传入的对象有一个run()方法就可以了

class Timer(object):
    def run(self):
        print('Start...')
#这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

#Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。
#但是，许多对象，只要有read()方法，都被视为“file-like object“。许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，
#完全可以传入任何实现了read()方法的对象。