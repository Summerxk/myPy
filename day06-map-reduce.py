# -*- coding:utf-8 -*-
from functools import reduce
#discription:函数式编成
#一，高阶函数
#高阶函数英文名：Higher-order function 
#1.变量可以指向函数
print(abs(-10))
print(abs)#<built-in function abs>

#可见 abs(-10) 是函数的调用，而abs是函数本身
f = abs
print(f)
print(f(-20))
#结论：函数本身也可以赋值给变量 即：变量可以指向函数

#2.函数名也是变量
#函数名其实就是执行函数的变量！对于abs() 这个函数，未能全可以吧函数名abs 看成变量，他指向一个可以计算绝对值的函数
#abs = 10
#abs(-10)
#把abs指向10后，就无法通过abs(-10)调用该函数了！因为abs这个变量已经不指向求绝对值函数而是指向一个整数10
#由于abs函数实际上是定义在import builtins模块中的，所以要让修改abs变量的指向在其它模块也生效，要用import builtins; builtins.abs = 10。

#3.传入函数
#既然变量可以指向函数，函数的参数能沟接受变量，那么一个函数就可以接受另一个函数作为参数，这种函数就称之为高阶函数
def add (x,y,f):
    return f(x) + f(y)
print(add(-5,6,abs))
#编写高阶函数，就是让函数的参数能够接收别的函数

#4.map/reduce
#python中内建了map()和reduce()函数。
#4.1map():函数接受来两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每一个元素，并把结果作为一个新的iterator返回
def f(x):
    return x * x
r = map(f,[1,2,3,4,5,6,7,8,9])
print(r)#<map object at 0x7f6dab1aa2b0>
print(list(r))#[1, 4, 9, 16, 25, 36, 49, 64, 81]
#map()作为一个高阶函数，事实上它把运算规则抽象了，因此我们不但可以计算f(x) = x^2 ,还可以任意复杂的函数，比如把这个list所有的数据转化为字符串
print(list(map(str,[1,2,3,4,5,6,7])))

#4.2reduct的用法
#reduce把一个函数作用在一个序列[x1,x2,x3,x4......]上，这个函数必须接受两个参数，reduce把结果继续和序列的下一个元素做累积计算
#reduce(f,[x1,x2,x3]) = f(f(f(x1),x2),x3)
#比如说用reduce实现一个序列的求和
def add (x,y):
    return x + y
#map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list
print(reduce(add,[1,2,3,4,5]))
print(sum([1,2,3]))#当然求和可以直接用sum()，没有必要用reduce

def fn(x, y):
    return x * 10 + y
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print(reduce(fn, map(char2num, '13579')))#13579

#整理成srt2int(s) 函数就是
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))
print(str2int('13579'))#13579

#还可以用lambda函数进一步简化
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
print(str2int('13579'))#13579
#练习
#1.利用map()函数，把用户输入的不规范的英文名字，变成首字母大写，其他小写的规范名字
def normalize(name):
    return name.capitalize()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
#2.求积
def prod(L):
    def mult(x, y):
        return x * y
    return reduce(mult,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

#3.利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def str2float(s):
    if not isinstance(s, str):
        raise TypeError('Parameter must be str')
    if '.' not in s:
        return int(s)
    int_str, float_str = s.split('.')
    return reduce(lambda x, y: x * 10 + y, map(char2num, int_str + float_str)) / (10 ** len(float_str))


print('str2float(\'123.456\') =', str2float('123.456'))










