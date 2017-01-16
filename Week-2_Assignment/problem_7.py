#python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 15:02:11 2016

@author: pavantej
"""
#efficient algo for finding last digit in sum of two random nos in fibonacci series
temp = list(map(int,input().split()))
a = temp[0]
b = temp[1]
sum_ab = 0
fib_series = [0,1]

def fibonacci(n):
    if n <= 1:
        return True
    else:
        for i in range(2,n+1):
            fib = fib_series[i-1] + fib_series[i-2]
            fib_series.append(fib % 10)
        return True

fibonacci(b)
for j in range(a, b+1):
    sum_ab += fib_series[j] % 10

print (sum_ab % 10)

