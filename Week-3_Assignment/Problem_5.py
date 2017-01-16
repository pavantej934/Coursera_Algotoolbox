#python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 14:16:31 2016

@author: pavantej
"""
N = int(input())

n = N
result = []
i = 1

while (n > 0):
    if (n - i) >= (i + 1):
        result.append(i)
        n -= i
        i += 1
    else:
        result.append(N - sum(result))
        n = 0
        
print (len(result))
print (' '.join([str(k) for k in result]))