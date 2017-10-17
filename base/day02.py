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
#默认参数有一个坑：
def add_end(L = []):
    L.append("END")
    return L
#正常调用的时候是正常的
print(add_end([1,2,3])) 
print(add_end(['x','y','z']))

#但是当使用默认参数进行调用的时候 "end" 会进行添加
print(add_end())
print(add_end())
print(add_end())
print(add_end())
print('这是因为python函数在定义的参数，默认参数L 的值就被计算出来了，即[] 。因为L 也是一个变量，它执行对象[],每次调用函数的时候，如果改变了L的内容，默认参数的内同就变了，不再是函数定义时候的[]了')
print('所以默认参数必须指向不变的对象')
print('so,定义一个默认的参数，实际上就是给L指向了内存中的一块空间，为‘END’，当函数调用的时候，重新给L赋值，也就是说将L的指向改变为另一块内存空间，当在不给L赋值，调用默认的值的时候，‘end’，实际上是对end 后面拼接end字符')
#可以这样子进行定义：
def add_end (L=None):
    if L is None:
        L = []
    L.append('END')
    return L
#1.3可变参数
#定义传入的参数个数是可以进行改变的
def cals(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print('参数number接受到的是一个tuple')
print(cals(1,2))
print(cals(1,2,3))
num = [4,5,6]
print(cals(*num))
#1.4关键字参数
#可变参数允许你传入0个或者任意个参数，这些可变参数在函数调用的时候，自动组装成一个tuple，而关键字参数允许你传入0或者任意个含有参数名字的参数
#，而这些关键字在函数内部自动组装成一个dict
def person(name, age, **kw):
    print('name:',name,'age:',age, 'other:',kw)
person('Summer',18)
person('summer',19,sex='boy',like='girl')
extra = {'sex':'boy','like':'girl'}
person('Summer',20,**extra)
#1.5命名关键字参数
#关键字参数可以传入不受限制的关键字参数，如果要限制关键字参数的名字，就可以用命名关键字参数。
def person(name,age,*,city,job):
    print(name,age,city,job)
#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
person('Summer',20,city ='beijing',job = 'IT')
#如果函数中已经有一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分割符 * 了
def person(name,age,*args,city,job):
    print(name,age,args,city,job)
#命名关键字参数必须传入参数名子，这和位置参数不同，如果没有传入参数的话，嗲用将会报错
a = (1,2,3)
person('summer',21,a,city = 'beijing',job = 'IT')  
person('summer',21,city = 'beijing',job = 'IT')
#命名关键子可以有缺省，从而简化调用
def person(name,age,*,city = 'Beijing',job):
    print(name,age,city,job)
person('Summer',22,job ='It')
#person('Summer',22,city ='It')#error 缺少job
#使用命名关键字参数时候，要特别注意，如果没有可变参数，就必须加一个 * 作为分割符号，如果缺少 * ，解释器将无法识别位置参数和关键字参数
def person(name,age,city,job):
    #缺少 * city 和 job 被视为位置参数
    pass
#1.6 参数组合
#5种参数都可以组合使用，但是参数的定义顺序必须是：必选参数，默认参数，可变参数，命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
f1(1,2)   
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
#So 对于任意函数，都可以通过func(*args,**kw) 的形式调用它，无论它的参数是如何定义的

#小结一下：
#1.必选参数，默认参数，可变参数（list，tuple），命名关键字参数（dict），关键字参数(dict 的指定key的名字)
#2.默认参数一定要用不可变的对象，如果是可变的参数，程序运行的时候，会出现逻辑错误
#3.*args是可变参数接受的是一个tuple;
#4.**kw 是关键字参数，kw接受的是一个dict
#5.可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#6.关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
#7.使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
#8.命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
#9.定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
def hello(greeting, *args):
    if (len(args)==0):
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ', '.join(args)))

hello('Hi') # => greeting='Hi', args=()
hello('Hi', 'Sarah') # => greeting='Hi', args=('Sarah')
hello('Hello', 'Michael', 'Bob', 'Adam') # => greeting='Hello', args=('Michael', 'Bob', 'Adam')

names = ('Bart', 'Lisa')
hello('Hello', *names) # => greeting='Hello', args=('Bart', 'Lisa')

print('*****************************************************************')
def print_scores(**kw):
    print('      Name  Score')
    print('------------------')
    for name, score in kw.items():
        print('%10s  %d' % (name, score))
    print()

print_scores(Adam=99, Lisa=88, Bart=77)

data = {
    'Adam Lee': 99,
    'Lisa S': 88,
    'F.Bart': 77
}

print_scores(**data)

def print_info(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('---------------')
    print('   Name: %s' % name)
    print(' Gender: %s' % gender)
    print('   City: %s' % city)
    print('    Age: %s' % age)
    print()

print_info('Bob', gender='male', age=20)
print_info('Lisa', gender='female', city='Shanghai', age=18)