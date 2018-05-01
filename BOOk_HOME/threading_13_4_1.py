#! usr/local/bin python3
#-*- coding:UTF-8 -*-
import threading
from time import sleep
from datetime import datetime
loops = [4,2]
date_time_format = '%y-%M-%d %H:%M:%S'
def date_time_str(date_time):
    return datetime.strftime(date_time,date_time_format)

def loop(n_loop,n_sec):
    print('thread',n_loop,'start time is',date_time_str(datetime.now()),'before sleep', n_sec,'second')
    sleep(n_sec)
    print('thread',n_loop,'sleep end, end time is',date_time_str(datetime.now()))

def main():
    print('all thread start , start time is',date_time_str(datetime.now()))
    threads = []
    n_loops = range(len(loops))

    for i in n_loops:
        t = threading.Thread(target=loop,args=(i, loops[i]))
        threads.append(t)
    
    for i in n_loops:
        threads[i].start()
    
    for i in n_loops:
        threads[i].join()
    
    print('all thread end ,end time is ', date_time_str(datetime.now()))

if __name__ == '__main__':
    main()
'''
all thread start , start time is 18-24-25 23:24:40
thread 0 start time is 18-24-25 23:24:40 before sleep 4 second
thread 1 start time is 18-24-25 23:24:40 before sleep 2 second
thread 1 sleep end, end time is 18-24-25 23:24:42
thread 0 sleep end, end time is 18-24-25 23:24:44
all thread end ,end time is  18-24-25 23:24:44
'''