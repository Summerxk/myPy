# -*- coding: utf-8 -*-
from collections import Iterable, Iterator
#高级特性：
#1.切片
#取出list的前几个元素
L=[0,1,2,3,4,5,6,7,8,9]
print(L[0:3])#表示从索引0开始 直接取到3为止，但是不包括索引3
#如果第一个索引是0，还可以这么写
print(L[:4])
#也可以取负数，最后一个值的索引为-1
print(L[-2:])
#1.1定一个L 0-99的数列
L = list(range(100))
print(L)
#1.2取出前10个
print(L[:10])
#1.3取出后10个
print(L[-10:])
#1.4取出11-20个
print(L[10:20])
#1.5前10个数，没隔两个取一个
print(L[:10:2])
#1.6所有的数字没隔着5个取出一个
print(L[::5])
#1.7tuple
print((0, 1, 2, 3, 4, 5)[:3])
#1.8字符串
print('ABCDEFG'[:3])
print('ABCDEFG'[::4])

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print('L[0:3] =', L[0:3])
print('L[:3] =', L[:3])
print('L[1:3] =', L[1:3])
print('L[-2:] =', L[-2:])

R = list(range(100))
print('R[:10] =', R[:10])
print('R[-10:] =', R[-10:])
print('R[10:20] =', R[10:20])
print('R[:10:2] =', R[:10:2])
print('R[::5] =', R[::5])

#2.迭代
#如果给定的一个list或者tuple 我们可以通过for循环来遍历这个list获者tuple，成这种遍历为迭代

#我们使用for循环的时候只要作用于一个可以进行迭代的对象，for循环就可以进行应用，不用关心该对象是list还是其他的数据类型
#2.1 判断一个对象是不是可以进行迭代的方法，就是通过collections模块的Iterable 类型进行判断
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))
#2.2如果要对list实现下标循环 用函数 enumerate 函数可以把一个list变成一个索引-元素对
for i,value in enumerate([1,2,3]):
    print(i,value)

print('*********************** test *******************')


def g():
    yield 1
    yield 2
    yield 3

print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
print('Iterable? \'abc\':', isinstance('abc', Iterable))
print('Iterable? 123:', isinstance(123, Iterable))
print('Iterable? g():', isinstance(g(), Iterable))

# iter list:
print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
    print(x)

print('for x in iter([1, 2, 3, 4, 5]):')
for x in iter([1, 2, 3, 4, 5]):
    print(x)

print('next():')
it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


d = {'a': 1, 'b': 2, 'c': 3}

# iter each key:
print('iter key:', d)
for k in d.keys():
    print('key:', k)

# iter each value:
print('iter value:', d)
for v in d.values():
    print('value:', v)

# iter both key and value:
print('iter item:', d)
for k, v in d.items():
    print('item:', k, v)

# iter complex list:   ????
print('iter [(1, 1), (2, 4), (3, 9)]:')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
