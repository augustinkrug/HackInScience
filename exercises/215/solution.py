# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:33:07 2015

@author: A.KRUG
"""

from is_prime import is_prime

somme = 0

for i in range(222281, 222381):
    bin_num = bin(i)[2:]
#    print('bin_num = ' + bin_num)
    somme_bin = 0

    for j in range(0, len(bin_num)):
        #   print("j = " + str(bin_num))
        somme_bin = somme_bin + int(bin_num[j])
#    print('somme_bin = ' + str(somme_bin))
    if is_prime(somme_bin):
        print(i)
