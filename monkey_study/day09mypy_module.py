#模块是一组python代码集合，可以使用其他模块，也可以被其他模块使用
#创建自己的模块时，要注意：
#模块名要遵循python变量命名规范，不要使用中文、特殊字符
#模块名不要喝系统模块名冲突，最好先查看系统是否已存在该模块，检查方法实在python
#交互环境执行import 模块名，若成功则说明系统存在此模块
#demo
#!/usr/bin/enc python3
#-*- coding utf-8 -*-

'a test module'

__author__ = 'MonkeyKing'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('hello world')
    elif len(args)==2:
        print('hello,%s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()


#---------------------------------------------------
print('---------------------------面向对象编程----------------------------------------')
#类和实例 demo
#注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。

#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改
class Student(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
        # self.name = name
        # self.score = score
        # self.__name = name
        # self.__score = score
    # def set_score(self,score):
    #     self.__score = score
    # def set_name(self,name):
    #     self.__name = name
    # def get_score(self):
    #     return self.__score
    # def get_name():
    #     return self.__name
    def set_gender(self,gender):
        self.gender = gender
    def get_gender(self):
        return self.gender
    def print_score(self):
        # print('%s : %s' % (self.name,self.score))
        print('%s : %s' % (self.__name,self.__score))
    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
# bart1 = Student('MonkeyKing01',59)
# print(bart1.get_name)
# print(bart1.get_score)
# bart1.print_score()
# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
#数据封装  面向对象编程的一个重要特点就是数据封装

# lisa = Student('Lisa', 99)
# bart = Student('Bart', 59)
# print(lisa.name, lisa.get_grade())
# print(bart.name, bart.get_grade())

print('---------------------------访问限制----------------------------------------')
#注意
#需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
# 特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名
#有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
# 但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”
#双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
# 所以，仍然可以通过_Student__name来访问__name变量