#python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 15:02:11 2016

@author: pavantej
"""
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
N = int(input())
print (fibonacci(N))            