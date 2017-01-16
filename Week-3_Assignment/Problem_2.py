#python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 23:53:46 2016

@author: pavantej
"""

n,W = input().split()
n,W = (int(n),int(W))

v = w = p = 0
#vw_list = []
wp_list = []
for i in range(n):
    v,w = input().split()
    v,w = (int(v),int(w))
    #vw_list.append((v , w))
    p = v / w
    wp_list.append((w , p))
    
wp_list.sort(key = lambda x: x[1], reverse = True)

v_total = 0
W_reduced = 0
while (W > 0) and (wp_list != []):
    if wp_list != []:
        W_reduced = min(W , wp_list[0][0])
        v_total += (wp_list[0][1]) * W_reduced
        W -= W_reduced
        wp_list.pop(0)
    
print ('{0:.4f}'.format(v_total))