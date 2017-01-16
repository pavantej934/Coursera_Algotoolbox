#python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 21:38:37 2016

@author: pavantej
"""
_ = int(input())

input_set = list(map(int,input().split()))

input_set.sort()

print (input_set[-1] * input_set[-2])
