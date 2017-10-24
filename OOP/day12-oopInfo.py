#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import types
#在我们拿到一个对象的引用的时候，如何知道这个对象是一个什么样的类型
#1，使用type()
print(type(123))#<class 'int'>
print(type(abs))#<class 'builtin_function_or_method'>
print(type(None))#<class 'NoneType'>

#type返回的是Class类型。
type(123)==type(456)#True
type(123)==int#True
type('abc')==type('123')#True
type('abc')==str#True
type('abc')==type(123)#False
#判断基本数据类型可以直接写int，str等，但是如果要判断一个对象是否是函数，可以用 types 模块中定义的常量
def fn():
    pass
type(fn)==types.FunctionType#True
type(abs)==types.BuiltinFunctionType#True
type(lambda x: x)==types.LambdaType#True
type((x for x in range(10)))==types.GeneratorType#True

#2, 使用isinstance()
#对于class的继承关系来说，使用type()很不方便。我们要判断class的类型，可以使用isinstance() 函数

#object -> Animal -> Dog -> Husky
#那么isinstance就可以告诉我们，一个对象是否是某种类型
class Animal(object):
    pass
class Dog(Animal):
    pass
class Husky(Dog):
    pass
a = Animal()
d = Dog()
h = Husky()
print(isinstance(h,Husky))#True
print(isinstance(h,Animal))#True
print(isinstance(h,Dog))#True
print(isinstance(d,Husky))#False

#能用type 进行判断的即被类型可以用isinstance()判断
#要获取一个对象的全部的属性和方法，可以使用dir()函数，他返回一个包含字符串的list，比如，获取一个str对象的所有的属性和方法：

print(dir('ABC'))
#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
#'__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', 
#'__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', 
#'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '
#__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 
#'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 
#'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 
#'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 
#'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 
#'translate', 'upper', 'zfill']


#类似__xxx__ 的属性和方法在python中都是有特殊用途的
