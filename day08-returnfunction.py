#-*- coding:utf-8 -*-
#函数作为返回值
#高阶函数除了可以接受函数作为参数外，还可以吧函数作为结果值返回
#1.我们实现一个求和的函数
def calc_sum(*args):
    ac = 0
    for n in args:
        ac = ac + n
    return ac
#2，但是我们如果不需要立即求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数
def lazy_sum(*args):
    def sum():
        ac = 0
        for n in args:
            ac = ac + n
        return ac
    return sum

f = lazy_sum(1,3,5,7,9)
print(f)#<function lazy_sum.<locals>.sum at 0x7fc6e3a6d158>
print(f())#25
#在这个例子中，我们在函数lazy_sum 中又定义了函数，sum 并且，内部函数sum 可以引用外部函数 lazy_sum 的参数和局部变量
#当lazy_sum 返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为‘闭包（closure）’
f1 = lazy_sum(1,3)
f2 = lazy_sum(1,3)
print(f1)#<function lazy_sum.<locals>.sum at 0x7fe48bba5268>
print(f2)#<function lazy_sum.<locals>.sum at 0x7fe48bba52f0>
print(f1 == f2)#False
#要注意，当我们调用lazy_sum()时候，每次调用都会返回一个新的函数，即使传入相同的参数
#f1()和f2()的调用结果互不影响

###闭包
#需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行，看个栗子
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print(f1())#9
print(f2())#9
print(f3())#9
#结果全部都是9 原因在于返回的函数引用了变量i，但是它并不是立刻执行的，等到三个函数都返回的时候，他们所引用的i 已经都变成了3，因此最终变成了9
#返回闭包时候要牢记一点就是：返回函数不要引用任何的循化年变量，或者后续会发生变化的变量
#如果一定要引用循环变量，方法时再创建一个函数，用妨碍函数的参数绑定循环变量当前的值，so，。无论该循环变量后续如何更改改，已经绑定到函数参数的值不会变
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count()
print(f1())#1
print(f2())#4
print(f3())#9
#返回一个函数时候，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量


