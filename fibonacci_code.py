# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 15:02:11 2016

@author: pavantej
"""

#naive way to find the fibonacci series
def fibonacci_naive(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_naive(n-1) + fibonacci_naive(n-2)
        
#print (fibonacci_naive(50))

#%%

#efficient algo for fibonacci series

def fibonacci(n):
    fib_series = [0,1]
    if n == 0 or n == 1:
        return n
    else:
        for i in range(2,n+1):
            fib = fib_series[i-1] + fib_series[i-2]
            fib_series.append(fib)
        return fib_series[n]

#print (fibonacci(50))
            