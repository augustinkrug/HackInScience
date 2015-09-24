# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:33:07 2015

@author: A.KRUG
"""

import json


def load_json(path):
    x = open(path)
    return json.load(x)
"""
print(load_json('example.json'))
"""
