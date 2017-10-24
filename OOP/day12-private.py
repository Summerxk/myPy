#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#如果让内部属性不让外部访问，可以把属性的名称前面加上两个下划线__ ，在puthon中实例的变量如果以__开头，就变成一个私有的变量
#（private） ，只有内部可以访问，外部不能访问：so
class Student(object):
    
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
bart = Student('Bart Simpson', 98)

#如果要外部访问name 和 score 可以使用 get_name 和 get_score 这样的方法：
class Student(object):

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
#如果要修改，可以使用set方法
class Student(object):
    def set_score(self, score):
        self.__score = score


#需要注意的是，在python中，变量名类似__XXX__的，也就是以双下划线开头，以双下划线结尾的，是特殊变量，特殊变量是可以
#直接访问的，不是private变量，所以，不能用__name__, __score__这样的变量名字。

#_name,这样的实例变量外部是可以进行访问的，但是，按照约定的规定，当你看到这样的遍历个的时候，意思就是“虽然我可以被访问
#但是，请把我看作私有的变量，不要随意访问”。

bart = Student('Bart Simpson', 98)
bart.get_name()#'Bart Simpson'

bart.__name = 'New Name' # 设置__name变量！
bart.__name#'New Name'

#表面上看，外部代码成功的设置了__name 变量，但是实际上_name 变量和class内部的__name 变量不是一个变量，
#内部的__name 变量已经被Python 翻译器自动改称了_student__name,而外部代码给bart新曾了一个 __name 变量

