#input函数 只能输入字符串
#user = input('Enter login name :')
#print('Your login name is :',user)
#将字符串转为整型
#num = input('Now enter a number: ')
#print ('Doubling your number is : ', (int(num)*2)) 

#学习Python   需要得到一个生疏函数的帮助
#只需要对它调用内建函数 help()，通过用函数名作为help()的参数就能得到相应的的帮助信息 如下
#help(input)

#操作符 
# + - * / // % **
# **  3**2 表示两个3相乘
#两种除法
#一种除法 /
a = 10/3;
print("一种除法 / --> 10 / 3 =", a);
a = 9 / 3;
print("一种除法 / --> 9 / 3 =", a);
#另一种除法  整数除整数得整数   如java中的/  python中是//
a = 10//3;
print("另一种除法  整数除整数得整数  / --> 10 / 3 =",a);
print(4 ** 2)
print (-2 * 4 + 3 ** 2) 

#  < <= > >= == != <>  and or not

#变量赋值
counter = 0
miles = 1000.0
name = 'monkey'
counter = counter +1
kilometers = 1.609 * miles
print( miles,'miles is the same as',kilometers,'km')

#字符串
pystr = 'Python'
iscool = 'is cool'
print(pystr[0],' ',pystr[2:5])
print(iscool[:2],' ',iscool[3:])
print(iscool[-1],' ',pystr+iscool)
print(pystr+' '+iscool,' ',pystr * 2,' ','-' * 20)
#小结
#Python支持使用成对的单引号或双引号，三引号（三个连续的单引号或者双引号）可以用来包含特殊字符
#使用索引操作符[]
#切片操作符[:]
#可以得到子字符串
#字符串有其特有的索引规则：第一个字符的索引是0，最后一个字符的索引是-1， +加号连接符  *用于字符串重复

#列表和元组
aList = [1,2,3,4,5]
print(aList)
print(aList[0])
print(aList[2:])
print(aList[:3])
aList[1] = 5
print(aList)

aTuple = ('monkey',77,99,'try')
print(aTuple)
print(aTuple[:3])
#aTuple[1] = 5
#print(aTuple)
#小结
#列表与元组  理解为同java一样的数组，不同的是它能保存人无疑数量任意类型的python对象
#列表与元组有几处重要的区别
#列表是用[]包裹，元素的个数及元素的值可以改变
#元组使用()包裹，不可以改变更改（尽管他们的内容可以），元组可以看成是只读的列表，通过切片运算可以得到子集

#字典
aDict = {'monkey':'jwj'}
aDict['port'] = 80
print(aDict)
print(aDict.keys())
print(aDict['monkey'])
for key in aDict:
    print(key,aDict[key])
#类似于java中map  键值对(key-value)
#工作原理类似perl中的关联数组或哈希表
#几乎所有的类型的python对象都可以用作键，不过一般还是以数字或者字符串最为常用

#if语句
x = 1
if x < 0:
    print('false')

if x>0:
    print('true')
else: 
    print('false')

if  x > 0:
    print('false')
elif x == 0:
    print('false')
else:
    print('false')

#while 循环
counter1 = 0
while counter1 < 3:
    print('loop ',counter1)
    counter1 += 1

#for循环和range()内建函数
item = ['e-mail','net-surfing','homework','chat']
for i in item:
    print(i,)
#注意 python中的for循环与传统的for循环(计数器循环)不太一样，它更像shell脚本里的foreach迭代
#python 中的for接受可迭代对象（列如序列或迭代器）作为其参数，每次迭代其中一个元素

#读取文件
fileobj = open('D:/python/test.txt','r')
for eachLine in fileobj:
    print(eachLine)
fileobj.close()

#如何打开文件
#handle = open(file_name,access_model = 'r')
# r 表示读取  w 表示写入 a 表示添加


#定义函数
#def function_name([args]):
#   "optional documentation string"
#   function_suite
#注解：
    #定义一个函数语法由def关键字及紧随其后的函数名，类似于java函数，区别在于()后以:结束，与if for whlie语法一样
    #之后是函数体
    #有return  则返回值
    #无return 则返回None
    #Python是通过易用调用的，这就意味着函数内对参数的改变会影响到原始对象
#列如
def test(x):
    print('test function ')
    return (x+x)
print(test('monkey'))
print(test(1))









