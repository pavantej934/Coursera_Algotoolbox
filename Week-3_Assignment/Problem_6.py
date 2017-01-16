#python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 14:16:31 2016

@author: pavantej
"""
n = int(input().strip())
numbers = list(map(int,input().split()))
answer = []

def numbercompare (x,y):
    x , y = str(x) , str(y)
    xy , yx = x + y , y + x
    if xy > yx :
        return True
    else:
        return False
    
while numbers != [] :
    maxdigit = 0
    for i in range(len(numbers)) :
        if numbercompare (numbers[i] , maxdigit):
            maxdigit = numbers[i]
    answer.append(maxdigit)
    if maxdigit in numbers:
        numbers.remove(maxdigit)

print (''.join(str(k) for k in answer))
