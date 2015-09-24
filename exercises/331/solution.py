# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:33:07 2015

@author: A.KRUG
"""

import json

"""
stations = [{"number": 31705,
             "name": "31705 - CHAMPEAUX (BAGNOLET)",
             "longitude": 2.416170724425901,
             "address":
             "RUE DES CHAMPEAUX (PRES DE LA GARE ROUTIERE) - 93170 BAGNOLET",
             "latitude": 48.8645278209514}]
"""
stations = json.load(open('velib.json'))

for n in stations:
    n['name'] = n['name'][8:]
    for i in range(2, len(n['address'])):
        if n['address'][i-2:i+1] == " - ":
            n['zip_code'] = n['address'][i+1:i+6]
            n['city'] = n['address'][i+7:]
            n['address'] = n['address'][:i-2]
            break

soluce = open('solution.json', 'w')
soluce.write(str(stations))
soluce.close()
