# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:33:07 2015

@author: A.KRUG
"""

import numpy as np
import math


def euclidean(a, b):
    x = 0
    for i in range(0, len(a)):
        x = x + (b[i]-a[i])**2
    return x**(.5)


def opt_euclidean(a, b):
    x = 0
    for i in range(0, len(a)):
        x = x + math.pow(b[i]-a[i], 2)
    return math.sqrt(x)


def np_euclidean(a, b):
    x = 0
    for i in range(0, len(a)):
        x = x + np.power(np.subtract(b[i], a[i]), 2)
    return np.power(x, .5)


"""
a = [2,3,7,3,4,0,8,2,1]
b = [5,3,0,7,8,6,9,4,5]
print(euclidean(a, b))
print(opt_euclidean(a, b))
print(np_euclidean(a, b))
print(euclidean(a, b) == opt_euclidean(a, b) == np_euclidean(a, b))
"""
