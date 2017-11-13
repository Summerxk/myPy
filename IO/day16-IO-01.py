#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#1.同步IO
#2.异步IO
#一，文件读写
#1.读文件
#以读文件的模式打开一个文件对象，使用python内置的open()函数，传入文件名和标示符
f = open('/home/summer/aa.sql','r')
#r 表示读，这样就打开了一个文件
#如果文件不存在，open()函数就会抛出一个 IOError的错误，并且给出错误码和详细的信息

'''
>>> f=open('/Users/michael/notfound.txt', 'r')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '/Users/michael/notfound.txt'

'''
#如果文件打开成功，接下来调用read()方法可以一次读取文件的内容，pyhon把内容读到内存，用str表示
print('sql fro IO:%s' %f.read())
#最后一步是调用close()方法， 关闭文件，文件使用完毕后，必须关闭，因为文件对象会占用操作系统的资源，操作系统
#在同一个时间内打开文件的数量也是有限的
f.close()

#由于文件读写的时候，都有可能产生IOError，所以，为了保证正确的关闭文件，要使用try----finally 来实现

try:
    f = open('/home/summer/bb.sql','r')
    print('bb.sql:%s' %f.read())
finally:
    if f:
        f.close()

#由于操作复杂，python引入 with 语句调用close()方法：

with open('/home/summer/aa.sql','r') as f:
    print(f.read())



