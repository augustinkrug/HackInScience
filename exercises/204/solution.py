# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:33:07 2015

@author: A.KRUG
"""


def perfect_shuffle(deck):
    shuffle = []
    half = len(deck) // 2
    for i in range(0, half - 1):
        shuffle.append(deck[i])
        shuffle.append(deck[i + half])
    if len(deck) > 2:
        shuffle.append(deck[half-1])
        if len(deck) % 2 == 0:
            shuffle.append(deck[len(deck)-1])
    return shuffle

"""
deck = [1, 2, 3, 4]
print(perfect_shuffle(deck))
"""
