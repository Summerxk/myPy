#! usr/local/bin python3
#-*-coding:UTF-8 -*-
import _thread
from time import sleep
from datetime import datetime

loops = [4,2]
date_time_format = '%y-%M-%d %H:%M:%S'

def date_time_str(date_time):
    return datetime.strftime(date_time,date_time_format)
def loop(n_loop,n_sec,lock):
    print('+++ thread', n_loop ,'start:' ,date_time_str(datetime.now()),'and just sleep times is',n_sec)
    sleep(n_sec)
    print('+++ thread', n_loop ,'sleep stop, stop time is :', date_time_str(datetime.now()))
    lock.release()

def main():
    print('--- all thread start time is',date_time_str(datetime.now()))
    locks = []
    n_loops = range(len(loops))

    for i in n_loops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in n_loops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in n_loops:
        while locks[i].locked():
            pass
    print('--- all thread end time is', date_time_str(datetime.now()))

if __name__ == '__main__':
    main()
