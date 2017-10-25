#Author:Summer
#!/usr/lib/env python3
# -*- coding:utf-8 -*-

import os

cmd_res = os.system('dir')#执行命令，不保存结果
print('-->',cmd_res)#0
#0 代表成功 不会保存到变量里面

cmd_res = os.popen('dir')
print('-->',cmd_res)#<os._wrap_close object at 0x0000000001165160> 打印的内存地址
cmd_res = os.popen('dir').read()
print(cmd_res)#这样就存下来了

#创建一个目录
cmd_res = os.makedirs('test_file').read()#AttributeError: 'NoneType' object has no attribute 'read'

print('rd name -->',cmd_res)#None  不会返回结果 输入read 会报NoneType 而且文件中有重名的文件夹不会创建成功
#cmd 下删除文件是 del name 删除文件夹 是rd name


#编译型，解释型
# .pyc 文件，c 为 compiled 编译，
#编译型语言是在程序执行之前，会通过编译器对程序执行一个编译的过程，把程序转变成机器语言，运行的时候就不需要翻译，而直接执行局就可以了，
#最典型的就是C语言。
#解释型语言就是没有这个编译过程，而是在程序运行的时候，通过解释器对程序逐行做出解释，然后进行执行。
#对于java而言，java首先通过编译器编译成字节码文件，然后在运行时候通过解释器给解释成机器文件。所以java是一种先编译后解释的语言

#python 和java相同，也是一门基于虚拟机的语言
#python 在命令行输入 python hello.py 的时候，执行的第一项工作就是先进行编译，所以python也是一门先编译后解释的语言。
#当python程序运行的时候，编译的结果则是保存在位于内存中的PyCodeObject中，当Python程序运行结束时，Python解释器则将PyCodeobject 写回到.pyc文件中。
#当python程序第二次运行时候，首先程序会在硬盘中寻找.pyc 文件 如果找到，则直接载入，否则就重复上面的过程。
#所以我们应该这样定位PyCodeObject和pyc文件，我们说pyc文件其实是PyCodeObject的一种持久化保存方式
