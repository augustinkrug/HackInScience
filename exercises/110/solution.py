# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:25:08 2015

@author: A.KRUG
"""
from sys import argv


try:
    if len(argv) < 4:
        print("usage: ./solution.py a_number (an_operator +-*/%^) a_number")
    elif (argv(1) is int and argv(3) is int):
        if argv(2) == "+":
            print(argv(1) + argv(3))
        elif argv(2) == "-":
            print(argv(1) - argv(3))
        elif argv(2) == "-":
            print(argv(1) - argv(3))
        elif argv(2) == "*":
            print(argv(1) * argv(3))
        elif argv(2) == "/":
            print(argv(1) / argv(3))
        elif argv(2) == "%":
            print(argv(1) % argv(3))
        elif argv(2) == "^":
            print(argv(1) ^ argv(3))
        else:
            print("input error")
    else:
        print("input error")
except:
    print("input error")
