#python基础
#多重赋值
x = y = z =1
print('多重赋值')
print('x = ',x)
print('y = ',y)
print('z = ',z)
print('=============================================')
#'多元'赋值
#x,y,z = 1,2,'String'
#通常元组需要用圆括号(小括号)括起来，建议加上括号
(x,y,z) = (3,2,'string')
print('多元赋值')
print('x = ',x)
print('y = ',y)
print('z = ',z)
print('=============================================')
#python 实现两个数交换
x,y = 1,2
print('交换前')
print('x = ',x)
print('y = ',y)
print('=============================================')
x,y = y,x
print('交换后')
print('x = ',x)
print('y = ',y)
print('=============================================')
#python关键字
print('python 部分关键字')
print('and  break  class  continue  def  del  elif  else  except')
print('exce  finally  for  from  global  if  import  in  is  lambda')
print('not  or  pass  print  raise  return  try  while  ')
print('=============================================')

#第一个python程序
import os
ls = os.linesep
#get name
while True:
    fname = input()
    if os.path.exists(fname):
        print('ERROR:',fname,'already exits')
    else :
        break
#get file content （text） lines
all = []
print ("\nEnter lines ('.' by itself to quit).\n")
while True :
    entry = input('> ')
    if entry == '.':
        break
    else :
        all.append(entry)
#write lines to file with proper line-ending
fobj = open(fname,'w')
fobj.writelines(['%s%s' % (x,ls) for x in all])
fobj.close()
print('DONE!')

#读文件小程序
#get filename
fname = input('Enter filename: ')
print
try :
    fobj = open(fname,'r')
except IOError(e):
    print ('*** file open error:',e)
else :
    #display contents to the screen
    for eachLine in fobj :
        print (eachLine)
    fobj.close() 
