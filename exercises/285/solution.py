# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:33:07 2015

@author: A.KRUG
"""

from requests import get

try:
    r = get('http://mdk.fr/ip')
    text = r.text
    for i in range(len(r.text)):
        if text[i] == "\n":
            text = text[:i]
            print(text)
            break
except:
    print("No internet connectivity.")
