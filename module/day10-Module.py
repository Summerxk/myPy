#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#为了编写可维护的代码，我们把很多函数分组，分别放在不同的文件里面，这样每个文件包含的代码就相对较少，很多编程语言都采用
#这种组织代码的方式。在python中，一个.py文件就称为一个模块(module)

#python的内值函数 https://docs.python.org/3/library/functions.html

#为了避免模块名的冲突，python 又引进了package包的概念

#每个包目录下面都会有一个__int__.py的文件，这个文件时必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。
#__init__.py 可以是空文件，也可以有Python代码，因为__init__.py 本身就是一个模块

#1.使用模块 以内建的sys模块为栗子，编写一个hello的模块

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()
#!/usr/bin/env python3 可以让 .py 文件直接在unix/linux/mac 上运行，
#-*- coding: utf-8 -*- 表示文本使用标准的UTF-8编码
#使用__author__ 变量把作者写进去

#sys 模块有一个 argv 变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该 .py 的名称.

#当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello
#模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
# $ python3 day10-Module.py summer ---> Hello, summer!

#2.作用域
#2.1在一个模块中，我们可能会定义很多函数和变量，但是用的函数和变量我们希望我们希望给别人使用，有的函数和变量我们希望在模块的
#内部使用，在python 中是通过 _ 前缀来进行实现

#2.2正常的函数河边两名是公开的public 可以直接进行引用，比如：abs, x123, PI

#2.3类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊的运用，比如上面 __author__,__name__ 就是特殊变量，hello
#模块定一个的文档注释也可以用特殊变量 __doc__ 访问，我们自己的变量一般不要用这种变量名；

#2.4类似__xxx 和_x这样的函数或者变量就是非公开的（private）,不应该直接被引用，比如_abx, __abc
#之所以private用不因该，而不是 不能被直接引用，是因为python并没有一种方法可以完全限制访问private函数或者变量。但是，从编成习惯上
#不应该引用private函数或者变量


def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
#我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，这样，调用greeting()函数不用关心内部的private函数
#细节，这也是一种非常有用的代码封装和抽象的方法，即：外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。

#安装第三方模块

#在python中，安装第三方模块，是通过包管理工具pip完成的。



