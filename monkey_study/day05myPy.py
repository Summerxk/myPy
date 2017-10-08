#python对象
#三个特性 身份 类型 值
#身份 每个对象都有一个唯一的身份标识自己，可以理解为是该对象的内存地址
#类型 对象的类型决定了该对象可以保存什么类型的值，可以进行什么样的操作，以及遵循什么样的规则
#值 对象表示的数据项
#标准类型
#Integer 整形 Boolean 布尔类型 Long integer 长整形 Floating point real number 浮点儿型
#Complex number 复数类型 String 字符串 List 列表 Tuple 元组 Dictionary 字典

print('===========标准类型对象身份比较操作符')
x = 1
print ('x的内存地址为 = ',id(x))
b = 1
print ('b的内存地址为 = ',id(b))
c = x is b
print('x is b 的结果为 = ',c)
d = 2
print ('d的内存地址为 = ',id(d))
y = x is not d
print('x is not d 的结果为 = ',y)
print('==============================================')

print('===========标准类型布尔操作符')
x , y = 3.14,-1024
a = x < 5.0
print('x < 5.0的布尔值 = ', a)
a = not (x < 5.0)
print('not (x < 5.0)的布尔值 = ', a)
a = (x < 5.0) or (y > 2.17)
print('(x < 5.0) or (y > 2.17)的布尔值 = ', a)
a = (x < 5.0) and (y > 2.17)
print('(x < 5.0) and (y > 2.17)的布尔值 = ', a)
a = not (x is y)
print('not (x is y)的布尔值 = ', a)
print('==============================================')

print('标准类型内建函数')
#type(object) 得到一个对象的类型，并反悔相应的type对象
print('type(4)是 = ',type(4))
#cmp() 比较obj1与obj2，根据比较结果返回整型 i：
# i < 0 if obj1 < obj2
# i = 0 if obj1 == obj2
# i > 0 if obj1 > obj2
# 类似与C语言中的strcmp()
#python3中operator 代替了cmp函数
#lt(a,b) 相当于 a<b     从第一个数字或字母（ASCII）比大小 
#le(a,b)相当于a<=b
#eq(a,b)相当于a==b     字母完全一样，返回True,
#ne(a,b)相当于a!=b
#gt(a,b)相当于a>b
#ge(a,b)相当于 a>=b
import operator
print (operator.eq(80,200))
print('==============================================')

print('学习廖雪峰的python3开始')
#学习set
#set与dict类似  保存key的一个集合，但是不保存value值，由于key不重复，所以set集合中没有重复的key
s = set([1,2,3])
print('set的集合为 = ',s)
#set集合与java中类似  有重复的元素它将自动过滤掉重复的元素
s = set([1,1,2,2,3,4,5])
print('set去重后的的集合为 = ',s)
#可以通过add(key)向set集合中添加元素
s.add(6)
print('set添加新元素后的的集合为 = ',s)
#可以通过remove(key)删除set集合中的元素
s.remove(4)
print('set删除数字4元素后的的集合为 = ',s)
#set可以看成数学意义上无序和无重复的元素集合，可以利用两个set集合获取集合交集、并集操作
a = set([1,2,3])
b = set([2,4,5])
print('a & b = ',a & b)
print('a | b = ',a | b)

#set与dict唯一的区别在于有无保存value值，其两个的原理都是一样的，同样不可以放入可变对象，因为无法判断两个可变对象是否相等
#也就无法保证set内部不会有重复元素
#str是不可变对象
#list则是可变对象
#对于可变对象，比如list，对list进行操作，list内部的内容是会变化的
a = ['c','b','a']
a.sort()
print('a.sort = ',a)
#对于不可变对象，比如str，对str的操作
s = 'abc'
print('s = ',s)
print('s.replace(\'a\',\'A\') = ',s.replace('a','A'))
print('s = ',s)
#a是变量，而'abc'才是字符串对象！有些时候，我们经常说，对象a的内容是'abc'，但其实是指，a本身是一个变量，它指向的对象的内容才是'abc'
#当我们调用a.replace('a', 'A')时，实际上调用方法replace是作用在字符串对象'abc'上的，而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。
#相反，replace方法创建了一个新字符串'Abc'并返回，如果我们用变量b指向该新字符串，就容易理解了，变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了
#对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的

#小结
#使用key-value存储结构的dict在Python中非常有用，选择不可变对象作为key很重要，最常用的key是字符串

print('=============================================')
print('python函数')
def mianji(r):
    Pi = 3.14
    mianji = Pi * r * r
    return mianji
for r in [12.34,9.08,73.1]:
    r=r+1
    print('圆的的面积为 = ',mianji(r))
print('=============================================')
print('练习hex()函数')
n1 = 255
n2 = 1000
print('n1 = 255 的十六进制形式表示 = ', hex(n1))
print('n1 = 1000 的十六进制形式表示 = ', hex(n2))
print('=============================================')
print('定义python函数')
#在Python中，定义一个函数要使用def语句，
#依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回
#请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。
#因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。
#如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。
#return None可以简写为return
def my_firstFunction_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x > 0 :
        return x
    else :
        return -x

print('调用my_firstFunction_abs函数 = ',my_firstFunction_abs(2))
print('=============================================')
print('返回多个值')
import math
def my_returnmore(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = my_returnmore(100, 100, 60, math.pi / 6)
print(x, y)
#小结
#定义函数时，需要确定函数名和参数个数；
#如果有必要，可以先对参数的数据类型做检查；
#函数体内部可以用return随时返回函数结果；
#函数执行完毕也没有return语句时，自动return None。
#数可以同时返回多个值，但其实就是一个tuple。

print('计算一元二次方程组 a*x*x+b*x+c=0')

def quadratic(a,b,c):
    if not isinstance(a, (int, float)):
        raise TypeError('input isinstance error')
    if not isinstance(b, (int, float)):
        raise TypeError('input isinstance error')
    if not isinstance(c, (int, float)):
        raise TypeError('input isinstance error')
    if a == 0:
        return -c / b
    z = b*b - 4*a*c
    if z < 0:
        print('无解')
    elif z >= 0:
       x1=(-b+math.sqrt(z)) / (2*a)
       x2=(-b-math.sqrt(z)) / (2*a)
       return x1,x2
print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))