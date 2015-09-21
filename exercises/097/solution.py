# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:25:08 2015

@author: A.KRUG
"""


def love_meet(bob, alice):
    love = []
    for i in set(bob):
        if i in alice:
            love.append(i)
    return sorted(love)


def affair_meet(bob, alice, silvester):
    affair = []
    for i in set(alice):
        if (i in silvester and i not in bob):
            affair.append(i)
    return sorted(affair)

"""
alice = ['II', 'IV', 'II', 'XIX', 'XV', 'IV', 'II']
bob = ['IV', 'III', 'II', 'XX', 'II', 'XX']

love = []
for i in set(bob):
    if i in alice:
        love.append(i)
print(love)
"""
"""
alice = ['II', 'IV', 'II', 'XIX', 'XV', 'IV', 'II']
bob = ['IV', 'III', 'II', 'XX', 'II', 'XX']
silvester = ['XVIII', 'XIX', 'III', 'I', 'III', 'XVIII']

affair = []
for i in set(alice):
    if (i in silvester and i not in bob):
        affair.append(i)
print(sorted(affair))
"""
