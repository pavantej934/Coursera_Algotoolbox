# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 15:32:39 2016

@author: pavantej
"""

#efficient code for gcd - Euclidean theorem

def gcd(a,b):
    if b == 0:
        return a
    else:
        rem = a % b
        print (b,rem)
        return gcd(b,rem)
        
#print (gcd(357,234))