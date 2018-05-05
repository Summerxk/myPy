#! usr/local/bin python3
#-*-coding:UTF-8 -*-
import _thread
from time import sleep
from datetime import datetime

date_time_format = '%y-%M-%d %H:%M:%S'

def date_time_str(date_time):
    return datetime.strftime(date_time,date_time_format)
def loop_one():
    print('+++ thread one start:' ,date_time_str(datetime.now()))
    print('+++ thread one sleep 4 second')
    sleep(8)
    print('+++ thread one sleep stop, stop time is :', date_time_str(datetime.now()))
def loop_two():
    print('+++ thread two start:' ,date_time_str(datetime.now()))
    print('+++ thread two sleep 2 second')
    sleep(2)
    print('+++ thread two sleep stop, stop time is :', date_time_str(datetime.now()))

def main():
    print('--- all thread start time is',date_time_str(datetime.now()))
    _thread.start_new_thread(loop_one,())
    _thread.start_new_thread(loop_two,())
    sleep(6)
    print('--- all thread end time is', date_time_str(datetime.now()))

if __name__ == '__main__':
    main()

'''
--- all thread start time is 18-33-24 23:33:13
+++ thread one start: 18-33-24 23:33:13
+++ thread two start: 18-33-24 23:33:13
+++ thread one sleep 4 second
+++ thread two sleep 2 second
+++ thread two sleep stop, stop time is : 18-33-24 23:33:15
+++ thread one sleep stop, stop time is : 18-33-24 23:33:17
--- all thread end time is 18-33-24 23:33:19

'''

'''
将线程一的休眠时间改为 8 秒 主线程结束，子线程也结束 所以没有等待线程一进行结束
--- all thread start time is 18-38-24 23:38:58
+++ thread one start: 18-38-24 23:38:58
+++ thread two start: 18-38-24 23:38:58
+++ thread two sleep 2 second
+++ thread one sleep 8 second
+++ thread two sleep stop, stop time is : 18-39-24 23:39:00
--- all thread end time is 18-39-24 23:39:04
'''