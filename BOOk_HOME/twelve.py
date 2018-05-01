#! usr/local/bin python3
#-*- coding:UTF-8 -*-
# import fileinput
# with open('/Users/summer/workspace/myPy/test_file/aa.txt') as f:
#     print(f.read())

#with open('/Users/summer/workspace/myPy/test_file/bb.txt','w') as f:
#print(f.write('heiheihei'))
# for line in fileinput.input('/Users/summer/workspace/myPy/test_file/aa.txt'):
#     print(line)
import pickle
# d = dict(name = 'Summer',age = '25')
# # print(pickle.dumps(d))
# with open('/Users/summer/workspace/myPy/test_file/pickle.txt','wb') as f:
#     pickle.dump(d,f)
with open('/Users/summer/workspace/myPy/test_file/pickle.txt','rb') as f:
    print(pickle.load(f))