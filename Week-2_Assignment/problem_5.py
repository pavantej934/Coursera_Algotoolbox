#python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 20:05:21 2016

@author: pavantej
"""
#pisano period - when the fibonacci series is mod by n, the remainder is periodic
#if F(n) mod by 2 = series repeats - 0,1,1,0,1,1,0,1,1 so on..
# periodicity = k, series = s

temp = list(map(int,input().split()))
n = temp[1]
f = temp[0]

#to find periodicity
a = 0
b = 1
c = a + b
for i in range(0 , n * n):
    c = (a + b) % n
    a = b
    b = c
    if (a == 0) and (b == 1):
        k = i + 1
        break
        
#to find the whole period
s = []
d = 0
e = 1
for j in range(0 , k):
    s += [d % n]
    d, e = e, d + e

rem = f % k
print (s[rem])