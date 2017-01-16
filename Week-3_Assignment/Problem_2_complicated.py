# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 23:53:46 2016

@author: pavantej
"""

n,W = input().split()
n,W = (int(n),int(W))

v = w = p = 0
vw_list = []
wp_list = []
for i in range(n):
    v,w = input().split()
    v,w = (int(v),int(w))
    vw_list.append((v , w))
    p = v / w
    wp_list.append((w , p))
    
wp_list.sort(key = lambda x: x[1], reverse = True)

v_total = 0
while (W > 0):
    if wp_list != []:
        v_total += (max(wp_list, key = lambda y: y[1])[1]) * min(W , (max(wp_list, key = lambda z: z[1])[0]))
        W -= min(W , (max(wp_list, key = lambda a: a[1])[0]))
        wp_list.pop(0)
    
print ('{0:.4f}'.format(v_total))