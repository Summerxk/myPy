#! usr/local/bin python3
#-*- coding:UTF-8 -*-
import threading
from time import sleep
from datetime import datetime

loops = [4,2]
date_time_format = '%y-%M-%d %H:%M:%S'
def date_time_str(date_time):
    return datetime.strftime(date_time,date_time_format)

class ThreadFunc(object):
    def __init__(self,func,args,name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)

def loop(n_loop,n_sec):
    print('thread',n_loop,'start ,start time is',date_time_str(datetime.now()),'befort sleep ',n_sec,'second')
    sleep(n_sec)
    print('thread',n_loop,'sleep end, end time is',date_time_str(datetime.now()))

def main():
    print('all thread start ,start time is',date_time_str(datetime.now()))
    threads =[]
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop, (i,loops[i]) ,loop.__name__))
        threads.append(t)
    
    for i in nloops:
        threads[i].start()
    
    for i in nloops:
        threads[i].join()
    
    print('all thread end, end time is',date_time_str(datetime.now()))

if __name__ == '__main__':
    main()



'''
all thread start ,start time is 18-12-26 00:12:10
thread 0 start ,start time is 18-12-26 00:12:10 befort sleep  4 second
thread 1 start ,start time is 18-12-26 00:12:10 befort sleep  2 second
thread 1 sleep end, end time is 18-12-26 00:12:12
thread 0 sleep end, end time is 18-12-26 00:12:14
all thread end, end time is 18-12-26 00:12:14
'''