#生成器 generator 在python中，这种一边循环一边计算的机制，称为生成器，generator
#创建一个generator  只要把列表生成式的[]改成()，就创建一个generator
print("==========生成器=============")
G = (x * x for x in range(10))
for x in G:
    print (x,' ',end='')
print()
#列表生成器
print("==========列表生成式=============")
L = [x * x for x in range(20)]
print(L,end='')
#创建列表生成式与生成器区别仅在于最外层的[]和(),L是一个list