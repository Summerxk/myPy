#-*- coding:utf-8 -*-
#sorted 排序算法
#python 内置的sorted()函数就可以对list进行排序
print(sorted([36,2,-15,9,-21]))
#此外，sorted()函数也是一个高阶函数，他可以接受一个key函数来实现自定义的排序，例如按照绝对值大小排序
print(sorted([36,2,-15,9,-21],key=abs))
#key指定的函数将作用于list的每一个元素上面，并根据key函数返回的结果进行排序。

#字符串的排序
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
#默认情况下，对字符串的排序，是按照ASCII的大小进行比较的。
#如果现在忽略大小写
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key = str.lower))

#要进行反向的排序，不必改动key函数，可以传入第三个参数 reverse = true
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key = str.lower, reverse = True))

#按照名字和成绩进行排序
def by_name(t):
    return t[0]

def by_score(t):
    return t[1]

L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
L2 = sorted(L,key=by_name)
L3 = sorted(L,key=by_score,reverse=True)
print(L2)
print(L3)