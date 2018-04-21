#! /usr/local/bin/python3
# -*- coding:UTF-8 -*-
class MyClass(object):
    i = 123
    def __init__(self,name):
        self.name = name
    def f(self):
        return 'hello,' + self.name
use_class = MyClass('Summer')
print(use_class.i)
print(use_class.f())