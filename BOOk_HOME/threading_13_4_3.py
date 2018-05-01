#! usr/local/bin python3
#-*- coding:UTF-8 -*-
import threading
from time import sleep
from datetime import datetime

loops = [4,2]
date_time_format = '%y-%M-%d %H:%M:%S'
def date_time_str(date_time):
    return datetime.strftime(date_time,date_time_format)

class MyThread(threading.Thread):
    def __init__(self, func, args, name = ''):
        threading.Thread.__init__(self)
        self.name = name
        self.args = args
        self.func = func
    
    def getResult(self):
        return self.res

    def run(self):
        print('starting',self.name,'at:',date_time_str(datetime.now()))
        self.res = self.func(*self.args)
        print(self.name, 'finnish at:', date_time_str(datetime.now()))

def loop(n_loop,n_sec):
    print('thread',n_loop,'start ,start time is',date_time_str(datetime.now()),'befort sleep ',n_sec,'second')
    sleep(n_sec)
    print('thread',n_loop,'sleep end, end time is',date_time_str(datetime.now()))

def main():
    print('all thread start ,start time is',date_time_str(datetime.now()))
    threads =[]
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop, (i,loops[i]), loop.__name__)
        threads.append(t)
    
    for i in nloops:
        threads[i].start()
    
    for i in nloops:
        threads[i].join()
    
    print('all thread end, end time is',date_time_str(datetime.now()))

if __name__ == '__main__':
    main()
'''
all thread start ,start time is 18-44-26 00:44:04

starting loop at: 18-44-26 00:44:04
thread 0 start ,start time is 18-44-26 00:44:04 befort sleep  4 second

starting loop at: 18-44-26 00:44:04
thread 1 start ,start time is 18-44-26 00:44:04 befort sleep  2 second
thread 1 sleep end, end time is 18-44-26 00:44:06
loop finnish at: 18-44-26 00:44:06

thread 0 sleep end, end time is 18-44-26 00:44:08
loop finnish at: 18-44-26 00:44:08

all thread end, end time is 18-44-26 00:44:08
'''