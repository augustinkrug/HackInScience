# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:33:07 2015

@author: A.KRUG
"""

text = open("words.txt")
result = {}
nb_letter = 0
for i in text.read():
    if i != "\n":
        nb_letter = nb_letter + 1
        if i in result:
            result[i] = result[i] + 1
        else:
            result[i] = 1

for j in result:
    print(j + ": " + str(round(result[j]/nb_letter, 2)))
