#-*- coding:utf-8 -*-
import functools
#偏函数（parital function）
#举个栗子
#int() 函数可以把字符串转换为整数，当仅仅传入字符串时，int()函数默认按照十进制转换
print(int('12345'))#12345
#但是int()函数还提供额外的base参数，默认值为10，如果传入base参数，就可以做N进制的转换
print(int('12345',base = 8))#5349
print(int('12345',16))#74565

#假设哈，要转换大量的二进制字符串，每次都传入int(x,base = 2)非常麻烦，所以我们可以定义一个int2()的函数，默认把base = 2 传进去
def int2(x,base = 2):
    return int(x, base)
#这样就非常方便了
print(int2('1000000'))#64
print(int2('1000000',16))#16777216

#functools.partial 就是帮助我们创建一个偏函数，不需要我们自己定义int2(),可以直接使用下面的代码，创建一个新的函数 int2
int2 = functools.partial(int,base = 2)
print(int2('1000000'))#64
print(int2('1010101', base = 10))# 无法重新指定base的值

#所以，简单总结，functools.partial 的作用就是，把一个函数的某个参数给固定住（也就是设置默认值），返回一个新的函数，调用这个函数
#会更简单

#在创建偏函数的时候，实际上可以接受函数对象，*args, **kw 这三个参数
#int2 = functools.partial(int, base=2)
#实际上固定了int()函数的关键字参数base，也就是：
#int2('10010')
#相当于：
#kw = { 'base': 2 }
#int('10010', **kw)
#当传入：
#max2 = functools.partial(max, 10)
#实际上会把10作为*args的一部分自动加到左边，也就是：
#max2(5, 6, 7)
#相当于：
#args = (10, 5, 6, 7)
#max(*args)
#结果为10。