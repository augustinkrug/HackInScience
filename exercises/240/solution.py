# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:33:07 2015

@author: A.KRUG
"""

output = "1, 2, "
i = 2
nb1 = 1
nb2 = 2
while i < 10:
    nb = nb1 + nb2
    output = output + str(nb) + ", "
    i = i + 1
    nb1 = nb2
    nb2 = nb
output = output[:-2] + "."
print(output)
