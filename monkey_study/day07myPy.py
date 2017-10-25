#切片
#区分元组 与 列表
#list 是python内置的一个数据类型，列表，是一种有序的集合，可以随时添加和删除
#其中的元素 类似java中的list集合
#另一种有序列表叫元组，tuple与list很相似，但是tuple一旦初始化就不能修改
#获取元素的方法和list是一样的，但不能赋值成另外的元素
#因为tuple不可变，所以代码更安全，如果可能，能用tuple代替list就尽量使用tuple
L = ['Monkey','Summer','KK','MH']
print('遍历集合L===================')
print(L[0:4])
print('遍历集合L从第一个元素开始遍历===================')
print(L[1:3])
print('倒着遍历集合L=====================')
print(L[-4:])
print('遍历另一中方式L[:]=================')
print(L[:])

#迭代
#如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（iteration）
#python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。
print('迭代======================================')
print('迭代dict输出==============================')
d = {'a':1,'b':2,'c':3}
for key in d:
    print(key)
#dict迭代的是key，如果要迭代value，可以用for value in d.values()，如果同时迭代key和calue，
#可以用for k，v in d.items()
print('迭代字符串================================')
for ch in 'ABCD':
    print(ch)
#如果实现类似java那样的下标循环，python内置的enumerate函数可以把一个list变成索引-元素对
#这样就可以在for循环中同时迭代索引和元素本身：
for i,value in enumerate(['A','B','C']):
    print(i,value)
#迭代也可以同时应用两个变量，在python里是很常见的
for x,y in [(1,1),(2,2),(3,3)]:
    print(x,y)

#列表生成式
print('列表生成式================================')
#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式
#列子 要生成list[1，2，3，4，5，6，7，8，9，10]可以用 list(range(1,11))
A = list(range(1,21))
print(A)
for a in A:
    print(a)
#如果要生成[1*1,2*2,3*3,...,10*10]
B = []
for b in range(1,11):
    B.append(b*b)
print(B)
#利用列表生成式生成上边的list
D=[a*a for a in range(1,11)]
print(D)
#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
D = [a*a for a in range(1,11) if a % 2 == 0]
print(D)
#还可以使用两层循环，生成全排列
D = [m+n for m in 'abc' for n in '123']
print(D)
#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
d = {'x':'A','y':'B','z':'C'}
for k,v in d.items():
    print(k, '=', v )
#最后一个把list中所有的字符串变成小写
L = ['KK','Monkey','Semmer']
l = [s.lower() for s in L]
print(l)

#练习
L = ['Hello','World',18,'Apple',None]
x = [l.lower() for l in L if isinstance(l,str)]
print(x)