#!/usr/lib/env python
#-*- coding: utf-8 -*-
#定制类
#__slots__ 是限定可定义的属性的名称，在python中有很多这样有特殊用途的函数，可以帮助我们定制类；
#1.__str__

class Student(object):
    def __init__(self, name):
        self.name = name
print(Student('summer'))#<__main__.Student object at 0x7f66724d6550>
#打印的是地址，我么定义一个 __str__() 方法，返回一个好看的字符串就可以了：
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'summer name is(name: %s)' % self.name
print(Student('xiakai'))#summer name is(name: xiakai)
#相当于toString 方法

print('------------------')
s = Student('heihei')
s#<__main__.Student object at 0x109afb310>
#这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，
#而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__

#2.__iter__
#如果一个类想被用于for ..... in 循环，类似list或 tuple 那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python 的for 循化就会
#不断调用该迭代对象的 __next__() 方法，拿到循化的下一个值，知道遇到StopIteration 错误的时候，退出循环。

class Fib(object):
    def __init__(self):
        self.a, self.b = 0,1 # 初始化两个计数器 a,b
    def __iter__(self):
        return self# 实例本身就是迭代对象，所以返回自己
    def __next__(self):
        self.a ,self.b = self.b, self.a + self.b #计算下一个值
        if self.a > 100:
            raise StopIteration()
        return self.a
for n in Fib():
    print(n)
#3.__getitem__
#Fib 实例虽然能作用于for循环，看起来和list有点像，但是，把它当作list使用还是不可以的，比如，取出第五个元素：
#Fib()[5] #TypeError: 'Fib' object does not support indexing
#如果要按照下标取出元素，需要 __getitem__()方法：

print('-------------__getitem__()-----------------')
class Fib(object):
    def __getitem__(self,n):
        a,b = 1,1
        for x in range(n):
            a,b = b,a+b
        return a
f = Fib()[6]
print(f)

#但是list有一个切片方法：
print(list(range(100))[5:10])

print('range(0) ----> ',range(2))
#对于Fib会报错，原因是 __getitem__()传入的参数可能是一个int 也可能是一个 slice，所以要进行判断：
class Fib(object):
    def __getitem__(self, n):
        if isinstance (n, int):
            a,b = 1,1
            for x in range(n):
                a,b = b, a+b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a,b= 1,1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b, a+b
            return L
f = Fib()
print('f[0:10] ---->',f[0:10])

#but 没有对负数做处理，也没有对step 参数做处理，所以要正确实现一个__getitem__() 还有很多工作要做。
print('f[:10:2] ---->',f[:10:2])

#此外，如果把对象看作dict,__getitem__()的参数也可能是一个可以做key 的object,例如 str.

#与之对应的是__setitem__()方法，把对象看作 list 或者 dict 来对集合赋值。最后，还有一个 __delitem__() 方法，用于删除某个元素。

#总之，通过上面的方法，我们自己定一个的类的表现形式，和python 自带的list tuple,dict没有什么区别，这完全是
#归功于动态语言的‘鸭子类型’，不需要强制继承某一个接口。

#4.__getattr__
print('-----------__getattr__()-------------')
 #正常情况下，如果我们调用类的某个属性和方法，如果没有的话，就会报错，比如定义 Student类：
class Student(object):
     def __init__(self):
         self.name = 'summer'
s = Student()
print(s.name)
#print(s.age) #AttributeError: 'Student' object has no attribute 'age'
#错误信息是，没有找到这个age这个 attribute

#为了避免这个错误，除了可以加上一个age属性外,python 还有一个机制，就是写一个__getattr__()方法，动态的返回一个属性。

class Student(object):
    def __init__(self):
        self.name = 'xiakai'
    def __getattr__(self,attr):
        if attr == 'age':
            return 25
s = Student()
print(s.name)
print(s.age)
# 返回函数也是可以的
class Student(object):
    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25

#只要调用的方式变为
s = Student()
s.age()

#注意，只要在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name,不会在__getarrt__中查找。
#此外，注意到任意调用如，s.abc 都会返回None,这是因为我们定义的__getattr__默认返回的就是None.要让class只响应特定的几个属性，我们就按照
#约定，抛出 AttributeError的错误
class Student(object):
    
    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

#5.__call__ 
print('----------__call__---------------')
#一个对象实例可以有自己的属性和方法，当我们调用实例方法的时候，我们用 instance.merthod()来调用。也可以用实例本身上进行调用
class Student(object):
    def __init__(self,name):
        self.name = name
    def __call__(self):
        print('my name is %s' % self.name)

s = Student('summer')
s()
#__call__() 还可以定义参数，对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把对象堪称函数。两者直接就没有根本的区别

#but 我们把对象看成函数，那么函数本身其实也可以在运行期间动态的创建出来，因为类的实例都是运行期创建出来的，这样，我们就模糊了对象和函数的界限。

#so 我们需要判断一个对象是否能被调用，能被调用的对象就是一个 Callable对象，比如函数和我们上面定义的带有 __call__() 的类的实例

print('callable:student--->',callable(Student('summer')))#True
print('callable:max--->',callable(max))#True
print('callable:[1,2,3]--->',callable([1,2,3]))#False
print('callable:None--->',callable(None))#False
print('callable:str--->',callable('str'))#False
#通过callable()函数，可以判断一个对象是否是‘可调用’对象

print('更多可被调用对象 doc 文档')
#https://docs.python.org/3/reference/datamodel.html#special-method-names

#总结：
#1，__str__(): 相当于 toString吧
#2，__iter__ 要于 __next__() 结合可进行 for... in循环
#3，__getitem__() 可以按照下标进行取出元素，还有切片的处理，但是不能完全 相当于list 比如说下标为负数，或者 没有对 step参数做处理
#4，__getattr__() 对未定义的属性 进行默认赋值
#5，__call__() 实例本身当作函数进行调用
#6，还有很多 https://docs.python.org/3/reference/datamodel.html#special-method-names 回头细看

print('-------------------分割线-------------------------------')

print('------------next--------------')


