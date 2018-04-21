#! /usr/local/bin/python3
# -*- coding:UTF-8 -*-
class Studeng(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name
s = Studeng('Summer')
print(s)