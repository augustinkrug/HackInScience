# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:25:08 2015

@author: A.KRUG
"""

import sys

if len(sys.argv) > 2:
    result = int(sys.argv[1])-int(sys.argv[2])
    print(result)
else:
    print("usage: python3 solution.py OP1 OP2")
