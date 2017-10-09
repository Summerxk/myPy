# -*- coding:utf-8 -*-
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

