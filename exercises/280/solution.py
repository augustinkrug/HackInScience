# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:33:07 2015

@author: A.KRUG
"""

from sys import argv

try:
    print(argv[1])
except:
    print("Not enough parameters.")
