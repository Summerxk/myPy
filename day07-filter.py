#-*- coding:utf-8 -*-
#python内建的filter()函数用于过滤序列。

#和map()函数类似，filter()也接受一个函数和一个序列。和map（）不同的是，filter()把传入的函数依次作用于每一个元素，然后根据返回指是True还是false决定保留还是丢弃该元素
def is_odd(n):
    return n % 2 == 1

L1 = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(L1)#[1, 5, 9, 15]
#把一个序列中的空字符串删掉，可以这么写：
def not_empty(s):
    return s and s.strip()

L1=list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(L1)#['A', 'B', 'C']
#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

#用filter求素数
#先构造一个从3开始的奇数序列，注意这是一个生成器，并且是一个无限序列。
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
#然后定义一个筛选函数：
def _not_divisible(n):
    return lambda x: x % n > 0
#最后，定义一个生成器，不断返回下一个素数：
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
#这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。
# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
