#函数的参数
#练习写一个计算x*x的程序
print('计算x * x的power(x)函数')
def power(x):
    return x * x
print('power(4) = ',power(4))
print('power(16) = ',power(16))
print('================================')
#定义传入两个参数  计算x的n次方的函数
print('power1(x,n)函数')
def power1(x,n):
    s = 1
    while n > 0:
         n = n - 1
         s = s * x
    return s
print('power(4,2) = ',power1(4,2))
print('power(16,3) = ',power1(16,3))
print('================================')
#默认参数
print('power1(x,n)默认参数函数')
def power1(x,n = 2):
    s = 1
    while n > 0:
         n = n - 1
         s = s * x
    return s
print('power(4,2) = ',power1(4))
print('power(16,3) = ',power1(16))
print('================================')
#注意
#从上面的例子可以看出，默认参数可以简化函数的调用。
#设置默认参数时，有几点要注意：
#一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
#二是如何设置默认参数。
#当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
#使用默认参数有什么好处？最大的好处是能降低调用函数的难度。
#例子
print('练习默认参数enroll(name,gender)')
def enroll(name,gender):
    print('name = ',name)
    print('gender = ',gender)
enroll('Monkey','A')
print('================================')

def enroll(name,gender,age = 6,city = 'GZ'):
    print('name = ',name)
    print('gender = ',gender)
    print('age = ',age)
    print('city = ',city)
enroll('Monkey','A')
#只有与默认参数不符的学生才需要提供额外的信息
enroll('pig','B',city = 'BJ')
#总结
#有多个默认参数时，调用的时候，既可以按顺序提供默认参数，
#比如调用enroll('Bob', 'M', 7)，意思是，
#除了name，gender这两个参数外，最后1个参数应用在参数age上，
#city参数由于没有提供，仍然使用默认值

#也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，
#需要把参数名写上。比如调用enroll('Adam', 'M', city='Tianjin')，
#意思是，city参数用传进去的值，其他默认参数继续使用默认值
print('================================')

#运用默认参数 注意
print('add_end(L=[])函数')
def add_end(L=[]):
    L.append('END')
    return L
print('add_end([1,2,3]) = ',add_end([1,2,3]))
print('add_end([\'x\',\'y\',\'z\']) = ',add_end(['x','y','z']))
print('add_end() = ',add_end())
print('add_end() = ',add_end())
#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
#因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
#如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
#所以，定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L = None):
    if L is None:
        L = []
    L.append('END')
    return L
print('add_end() = ',add_end())
print('add_end() = ',add_end()) 
print('================================')
print('可变参数========================')
#可变参数  顾名思义  参数是可变的 可以是1个 2个 3个  甚至更多。。。
def calc(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i * i
    return sum
#调用时先组装一个list与tuple
print('calc([1,2,3]) = ',calc([1,2,3]))
print('calc((3,4,5)) = ',calc((3,4,5)))
#利用可变参数，调用函数的方式可以简化成
def calc1(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i * i
    return sum
#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
#在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
#但是，调用该函数时，可以传入任意个参数，包括0个参数
print('calc1(1,2,3) = ',calc1(1,2,3))
print('calc1(1,3,5,7) = ',calc1(1,3,5,7))
nums = [1,2,3]
print('calc1(nums[0],nums[1],nums[2]) = ',calc1(nums[0],nums[1],nums[2]))
print('calc1(*nums) = ',calc1(*nums))
#*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见
print('================================')
print('关键字参数')
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
#而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name,age,**kw):
    print('name = ',name,'age = ',age,'other = ',kw)
person('Monkey','25')
person('Monkey','25',city = 'GZ')
person('Monkey','25',city = 'GZ',birthday = '19920610')
extra = {'city':'beijing','job':'engineer'}
person('Monkey',25,city = extra['city'],job = extra['job'])
person('Monkey',25,**extra)
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
#注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
print('================================')
print('命名关键字参数')

