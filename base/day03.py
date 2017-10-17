#-*- coding:utf-8 -*-
#1 递归函数
# fact(n) = n! = 1 * 2 * 3 * ....* (n-1) * n 
#所以fact(n) 可以表示为 n * fact（n - 1）,只有n = 1的时候需要处理
#于是fact(n) 用递归的方法写出来就是：
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
#使用递归函数需要防止栈的益处，函数调用一次，栈就增加一层，返回一次栈就减少一层，如果递归的次数过多，会造成栈的益处
#解决递归调用的方法是通过尾递归进行优化
#尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
#Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。

# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')