# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:25:08 2015

@author: A.KRUG
"""

total = 0

for n in range(1, 101):
    if n % 2 == 0:
        total = total + n
print(total)
