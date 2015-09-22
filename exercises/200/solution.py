# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:25:08 2015

@author: A.KRUG
"""


def is_prime(num):
    if num < 1:
        return False
    else:
        for i in range(3, num):
            if num % i == 0:
                return False
    return True
