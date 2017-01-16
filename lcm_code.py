#python3
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
        return gcd(b,rem)
        
temp = list(map(int,input().split()))
A = temp[0]
B = temp[1]
GCD = gcd(A,B)
LCM = int(A * B / GCD)
print (LCM)