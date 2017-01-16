#python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 15:02:11 2016

@author: pavantej
"""
#efficient algo for finding last digit in fibonacci series

'''
n = int(input())

a = 0
b = 1
c = 1
if n == 0 or n == 1:
    print (n)
else:
    for i in range(n - 1):
        a, b = b, a + b
        c += b
    print (c % 10) 
            '''
            
#alternative solution
import functools

N = int(input())

@functools.lru_cache(None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
    
f_n2 = fib(N+2)
print ((f_n2 - 1) % 10)