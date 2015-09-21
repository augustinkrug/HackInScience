# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:25:08 2015

@author: A.KRUG
"""

import datetime

jour = datetime.date.today()
heure = datetime.datetime.today().time().strftime('%H:%M:%S')

print("Today is", jour, "and it is", heure)
