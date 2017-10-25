#!/usr/lib/env python
#-*- coding: utf-8 -*-
#多重继承
class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass
#Python自带的很多库也使用了MixIn。举个例子，Python自带了TCPServer和UDPServer这两类网络服务，
#而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由ForkingMixIn和ThreadingMixIn提供。
#通过组合，我们就可以创造出合适的服务来。
#比如，编写一个多进程模式的TCP服务
class MyTCPServer(TCPServer, ForkingMixIn):
    pass
#编写一个多线程模式的UDP服务
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass

#小结：
#由于python 允许使用多继承，因此，MixIn就是一种常见的设计。
