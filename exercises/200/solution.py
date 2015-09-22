# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:25:08 2015

@author: A.KRUG
"""


def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True

print(is_prime(2))
