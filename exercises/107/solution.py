# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:25:08 2015

@author: A.KRUG
"""
from operator import itemgetter


def select_student(my_class, mark):
    accepted = []
    rejected = []
    for i in range(0, len(my_class)):
        if my_class[i][1] >= mark:
            accepted.append(my_class[i])
        else:
            rejected.append(my_class[i])
    return {'Accepted': sorted(accepted, reverse=True, key=itemgetter(1)),
            'Refused': sorted(rejected, key=itemgetter(1))}

"""
my_class = [['Kermit Wade', 27], ['Hattie Schleusner', 67],
            ['Ben Ball', 5], ['William Lee', 2]]
print(select_student(my_class, 20))
print(select_student(my_class, 50))
"""
