# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:25:08 2015

@author: A.KRUG
"""
from sys import argv


def calc(a, op, b):
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a / b)
    elif op == "%":
        print(a % b)
    elif op == "^":
        print(pow(a, b))

if len(argv) < 4:
    print("usage: ./solution.py a_number (an_operator +-*/%^) a_number")
elif argv[2] not in ["+", "-", "*", "/", "%", "^"]:
    print("input error")
else:
    try:
        a = int(argv[1])
        op = argv[2]
        b = int(argv[3])
        calc(a, op, b)
    except:
        print("input error")
