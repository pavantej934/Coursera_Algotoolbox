#python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 22:14:24 2016

@author: pavantej
"""

m = int(input())
no_10 = no_5 = no_1 = 0

no_10 = m // 10
m = m - (10 * no_10)

no_5 = m // 5
m = m - (5 * no_5)

no_1 = m

print (no_10 + no_5 + no_1)
    