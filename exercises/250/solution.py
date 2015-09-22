# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:33:07 2015

@author: A.KRUG
"""


def draw_n_squares(n):
    line1 = n * "+---" + "+"
    line2 = n * "|   " + "|"
    squares = ""
    for i in range(1, n + 1):
        squares = squares + line1 + "\n" + line2 + "\n"
    return squares + line1
"""
print(draw_n_squares(5))
"""
