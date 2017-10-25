#!/usr/lib/env python
#-*- coding: utf-8 -*-
#在属性绑定的时候，如果我们直接把属性暴露出去，简单，但是没办法检查参数。
#这显然是不合逻辑的，为了显示score的范围，可以通过set_score() 方法来设置成绩，再通过一个 get_score() 来获取成绩，
class Student(object):
    
    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
    #raise ： 抛出异常

#太复杂，来个简单的

#装饰器，decorator 可以给函数动态加上功能，对于类的方法，装饰器起一样的作用。python内置的 @property 装饰器就是负责把一个方法编成
#属性调用

class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100')
        self._score = value

#@property 本身又创建了另一个装饰器 @score.setter, 负责把一个setter方法编成属性赋值，于是 我们就拥有了一个可控的属性的操作：

s = Student()
s.score = 60#OK，实际转化为s.set_score(60) 
print(s.score)# OK，实际转化为s.get_score() 
#s.score = 9999#ValueError: score must between 0 ~ 100

