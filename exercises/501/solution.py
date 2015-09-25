# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:33:07 2015

@author: A.KRUG
"""


def changes2(amount, coins_rv):
    count = 0
    while coins_rv[0] > amount:
        del coins_rv[0]
    maxi = amount // coins_rv[0]
    for i in reversed(range(0, maxi + 1)):
        rest = amount - i * coins_rv[0]
        if rest == 0:
            count = count + 1
        else:
            if len(coins_rv) > 1:
                count = count + changes2(rest, coins_rv[1:])
    return count


def changes(amount, coins):
    coins_rv = sorted(coins, reverse=True)
    return changes2(amount, coins_rv)
