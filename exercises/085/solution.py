# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:25:08 2015

@author: A.KRUG
"""

from operator import itemgetter


def sort_a_list(l):
    return sorted(l, reverse=True)


def sort_by_mark(my_class):
    return sorted(my_class, key=itemgetter(0), reverse=True)


def sort_by_name(my_class):
    return sorted(my_class, key=itemgetter(1))

"""
my_class = [[6, 'Joshua Tran'], [37, 'Jeanette Wafer'], [85, 'Susan Maddox'],
            [84, 'Joseph Pedersen'], [12, 'Bonnie Torres'],
            [36, 'John Freeman'], [27, 'Betty Askins'], [37, 'Melanie Noe'],
            [22, 'Mark Osbourne'], [42, 'Lidia Robel']]


print(sorted(my_class, key=itemgetter(0), reverse=True))
"""
