# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:33:07 2015

@author: A.KRUG
"""

from is_prime import is_prime

i = 100000000
while is_prime(i) is False:
    i = i + 1
else:
    print(i)
