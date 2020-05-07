#Exercice 4
#1)

import random

def tri_compte1(tab,M):
    r_list = []
    compte = []
    for i in range(0,M+1):
        compte.append(0)
    
    for i,val in enumerate(tab):
            compte[val] = compte[val]+1
            
    for i, val in enumerate(compte):
        for j in range(0,val):
            r_list.append(i)
    
    return r_list
        
               
"""
2)
def tri_compte1(tab,M):
    r_list = []
    compte = []
    for i in range(0,M+1):#M+1
        compte.append(0)#1
    
    for i,val in enumerate(tab):#n
            compte[val] = compte[val]+1#1
            
    for i, val in enumerate(compte):#M+1
        for j in range(0,val):#O(M)
            r_list.append(i)#1
    
    return r_list

(M+1)*1+n*1+(M+1)O(M)*1 = M+1+n+M*O(M) = M(1+O(M))+n = O(n)
"""

#4)
def tri_compte2(tab,M):
    compte = []
    for i in range(0,M+1):
        compte.append(0)
    
    for i,val in enumerate(tab):
            compte[val] = compte[val]+1
            
    tab.clear()        
    for i, val in enumerate(compte):
        for j in range(0,val):
            tab.append(i)
            
#5)
def max(tab):
    max = 0
    for val in tab:
        if val > max:
            max = val
    return max

def tri_compte3(tab):
    compte = []
    for i in range(0,max(tab)+1):
        compte.append(0)
    
    for i,val in enumerate(tab):
            compte[val] = compte[val]+1
            
    tab.clear()        
    for i, val in enumerate(compte):
        for j in range(0,val):
            tab.append(i)