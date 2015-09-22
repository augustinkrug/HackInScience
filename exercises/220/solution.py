# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:33:07 2015

@author: A.KRUG
"""

from is_prime import is_prime

output = ""
for i in range(10000, 10050):
    if is_prime(i):
        output = output + str(i) + ", "

output = output[:-2]
print(output)
