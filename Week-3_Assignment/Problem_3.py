#python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 2016

@author: pavantej
"""
n = int(input())
a = input().split()
b = input().split()
for i in range(n):
    a[i] = int(a[i])
    b[i] = int(b[i])

a.sort(reverse = True)
b.sort(reverse = True)
    
max_revenue = 0
while (a != [] and b != []):
    max_revenue += a[0] * b[0]
    a.pop(0)
    b.pop(0)
    
print (max_revenue)
