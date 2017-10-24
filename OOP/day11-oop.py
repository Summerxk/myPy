#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#面向对象最重要的概念就是类（class） 和实例（Instance）
class Student(object):
    pass
#class 后面紧接着的是类名，即Student，类名通常是大写开头的单词,紧接着是（object） 表示该类是从哪个类继承下来的，通常
#没有合适的继承类就使用object类，这是所有类最终会继承的类。

bart = Student()
bart
print(bart)#<__main__.Student object at 0x7fcb4e766358>
print(Student)#<class '__main__.Student'>
#可以看到，变量bart指向的就是一个Student的实例，后面的0x7fcb4e766358 是内存地址每个object的地址都不一样，而Student本身则是一个类

#变量绑定一个属性
bart.name = 'summer'
print(bart.name)
#由于类可以起到模板的作用，因此，可以再创建实例的时候，把我们然为必须绑定的属性，绑定进去。通过一个特殊的__init__ 方法，在创建实例的
#时候，把name，score等属性绑定上去：
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
#注意：特殊方法init前后有两个下划线

#init方法的第一个参数永远是self，表示创建的实例本身，因此，再init方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。

bart = Student('summer',10)
print(bart.name)
print(bart.score)
#总结
#和普通的函数相比，再类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，嗲用时，不用传递该参数，除此之外，类的方法和普通
#函数没有什么区别，所以，你仍然可以用默认参数，可变参数，关键字参数和命名关键字参数。

#数据封装

#面向对象编成3的一个重要特点就是数据封装，在上面的student类中，每个实例就拥有各自的name 和 score 这些数据。我们可以通过函数来进行访问这些数据
#比如打印学生的成绩：
def print_score(std):
    print('%s:%s' % (std.name,std.score))
print_score(bart)


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))
bart = Student('summer',90)
bart.print_score()

#小结：
#类时创建实例的模板，而实例则是一个具体的对象，各个实例拥有的数据相互独立，互不影响；
#方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
#通过在实例上调用的方法，我们就直接操作了对象内部的数据，但是无需知道方法内部的实现细节
#和景泰语言不同，python荀彧对实例比呐量绑定任何数据，也就是说，对于两个实例变量，虽然他们都是同一个类的不同实例，但是拥有的实例变量名称都可能不同

