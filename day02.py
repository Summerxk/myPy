# -*- coding:utf-8 -*-
#1.函数的参数（有点难度）
#函数的定义非常简单，但是灵活性也是非常大的。除了正常定一个的必选参数外，还可以使用默认的参数，可变参数和关键字参数。
#1.1 位置参数
def power(x):
    return x * x
print(power(2))
#对于power(x) 函数来说 参数x 就是一个位置参数
# 现在当我们调用power 时传入一个参数就可以，但是如果 计算多个x相乘就可以定一个power3
def power(x,n):
    s = 1
    while n > 0:
        n = n-1
        s = s * x
    return s
#对于修改后的power（x,n）可以计算任意n次方
print(power(4,3))
#print(power(2))
#1.2 默认参数
#但是对于 power来说 就失去了意义，因为增加了一个参数 导致旧的代码没办法调用
#print(power(4))#ypeError: power() missing 1 required positional argument: 'n'
#这个时候可以使用默认的参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5))
print(power(5,4))
#相同的函数名称的时候 调用的是哪个？？  依次调用相当于函数重新进行定义








