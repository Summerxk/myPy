#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#使用__slots__
from types import MethodType
#正常的情况下，当我们定义了一个class,创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，
#这就是动态语言的灵活性。
class Student(object):
    pass
#1.先给实例绑定一个属性
s = Student()

s.name = 'summer'
print(s.name)

#2 给实例绑定一个方法
def set_age(self, age):# 定义一个函数作为实例方法
    self.age = age
s.set_age = MethodType(set_age,s)# 给实例绑定一个方法
s.set_age(25)

print(s.age)

#3但是给一个实例绑定的方法，对另一个实例是不起作用的：
s2 = Student() # 创建新的实例
#s2.set_age(33)

#print(s2.age)#AttributeError: 'Student' object has no attribute 'set_age'

#4 为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self, score):
    self.score = score
Student.set_score = set_score

s = Student()
s.set_score(100)
print(s.score)

#使用__slots__ 
#但是，如果我们想限制实例的属性，比如只允许在实例中添加 name ， age属性

#python允许在定义class的时候，定义一个特殊的__slots__变量来限制class实例能添加的属性：
class Student(object):
    __slots__ = ('name','age')

s = Student()

s.name = 'summer'
s.age = 25
#s.score = 100#AttributeError: 'Student' object has no attribute 'score'
print(s)

#由于‘score’ 没有被放到__slots__ 中，所以不能绑定score属性，试图绑定score属性，就会得到 attributeErroe

#使用__slots__要注意，__slots__ 定义的属性仅仅对于当前的实例起到了作用，对于继承的子类是不会起作用的

#除非在子类中定义 __slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的 __slots__
