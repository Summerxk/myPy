#!/usr/lib/env python
#-*- coding: utf-8 -*-

#python的pdb可以让我们以单步的方式执行代码。

#1.错误处理
#try
try:
    print('try...')
    r = 10/0
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally....')
print('end')
#如果出错将会执行 except 模块，如果有finally 语句块，则执行 finally语句块，至此，执行完毕
'''
try...
except: division by zero
finally....
end
'''
#还有一种异常 例如 ValueError

#此外，如果没有异常发生，可以在except语句块后面加一个 else ,当没有错误发生的时候，会自动执行 else语句
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

#Python的错误其实也是 class,所有的错误类型都继承自 BaseException，所以在使用 except时候，要注意的是
#baseException 可以捕获所有的异常
def foo():
    pass
try:
    foo()
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')
#像上面这个try 因为 UnicodeError是ValueError 的子类，所以永远不会捕获到 Unicoderror的错误

#常见的错误类型：
#https://docs.python.org/3/library/exceptions.html#exception-hierarchy
'''
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
           +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
'''
#调用堆栈
print('-------------调用堆栈-----------------')
#如果错误没有被捕获，它就会一直往上抛，最后被Python解释器，打印一个错误信息，然后程序退出。来瞅瞅err.py

#err.py:
def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s) * 2
def main():
    bar('0')
main()
'''
Traceback (most recent call last):
  File "day14-debug.py", line 133, in <module>
    main()
  File "day14-debug.py", line 132, in main
    bar('0')
  File "day14-debug.py", line 130, in bar
    return foo(s) * 2
  File "day14-debug.py", line 127, in foo
    return 10/int(s)
ZeroDivisionError: division by zero
'''

#从上往下看：
#错误信息的第一行： Traceback (most recent call last): 这是错误的跟踪信息
# 2-3行 
'''  
File "err.py", line 11, in <module>
    main()
'''
#调用main出错，在代码文件day14-debug.py 的第133行，但是原因在第132行；
#调用bar('0')出错了，在代码文件day14-debug.py 的第130行代码，但原因是127行：
#原因是return foo(s) * 2这个语句出错了，但这还不是最终原因，继续往下看：
#原因是return 10 / int(s)这个语句出错了，这是错误产生的源头，因为下面打印了：

#记录错误
print('-------------记录错误------------')
#如果不捕获异常，自然可以让python解释器来打印出错误的堆栈，但是程序也被结束了。 记录一下错误 继续执行：
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')
'''
ERROR:root:division by zero
Traceback (most recent call last):
  File "err_logging.py", line 13, in main
    bar('0')
  File "err_logging.py", line 9, in bar
    return foo(s) * 2
  File "err_logging.py", line 6, in foo
    return 10 / int(s)
ZeroDivisionError: division by zero
END
'''

#抛出错误
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')
#只有在需要的时候才会钉子我们自己的错误类型。如果可以选择python已有的内值的错误类型（比如 ValueError,TypeError）,尽量使用python的内置错误

def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()

#bar()函数中，我们已经成功的捕获了一个 异常，打印了 ValueError！ 后又抛出了异常，。捕获错误的目的在于记录，往上抛，让父类进行处理。
#raise语句如果不带参数，就会把当前错误原样抛出，除此之外 在except中raise一个Error,还可以把一种类型的错误转化为另一种类型：

try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')
#小结：
#Python内置的try...except...finally用来处理错误十分方便。出错时，会分析错误信息并定位错误发生的代码位置才是最关键的。

#程序也可以主动抛出错误，让调用者来处理相应的错误。但是，应该在文档中写清楚可能会抛出哪些错误，以及错误产生的原因。