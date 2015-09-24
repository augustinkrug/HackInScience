# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:33:07 2015

@author: A.KRUG
"""

text = open("words.txt")
count = 0
for i in text.read():
    if i == "e":
        count = count + 1
print(count)
