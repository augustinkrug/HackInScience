# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:25:08 2015

@author: A.KRUG
"""

total = 0

for n in range(1, 1000):
    if n % 3 == 0:
        total = total + n
    elif n % 5 == 0:
        total = total + n

print(total)
