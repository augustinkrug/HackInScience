# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:33:07 2015

@author: A.KRUG
"""

from is_prime import is_prime

somme = 0

for i in range(1, 1000):
    if is_prime(i):
        somme = somme + i

print(somme)
