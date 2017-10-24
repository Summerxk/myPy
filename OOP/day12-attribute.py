#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#类属性，相当于成员变量；
class Student(object):
    name = 'summer'
s = Student()
print(s.name)#summer

print(Student.name)#Student

s.name = 'winter'
print(s.name)# 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性 #winter
print(Student.name)# 但是类属性并未消失，用Student.name仍然可以访问 #summer


print('----------del------------')
del s.name#如果删除实例的name属性
print(s.name)# 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了

#从上面的栗子中可以总结：在便编写程序的时候，千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性
#将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问的将是类的属性

