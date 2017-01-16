#python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 2016

@author: pavantej
"""
n = int(input())
a = b = 0
ab_list = []
for i in range(n):
    a,b = input().split()
    a,b = (int(a),int(b))
    ab_list.append((a , b))
    
ab_list.sort(key = lambda x: x[1])

count = 0
ab_result = []
b_temp = 0
j = 1

while (ab_list != []):
    b_temp = ab_list[0][1]
    if len(ab_list) > 1:
        if ab_list[1][0] <= b_temp <= ab_list[1][1]:
            ab_list.pop(1)
        else:
            count += 1
            ab_result.append(b_temp)
            ab_list.pop(0)
    else:
        count += 1
        ab_result.append(b_temp)
        ab_list.pop(0)
        
print (count)
print (' '.join([str(k) for k in ab_result]))
        
    