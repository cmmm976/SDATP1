#Exercice 1

import random
import sys

#1)
def double_tab(t):
    r_tab = []

    for i, val in enumerate(t):
        r_tab.insert(i,2*val)

    return r_tab

#2)

def permutation(a,b): #renvoie une permutation aleatoire de {a,...,b}
    r_tab = []
    base_tab = list(range(a,b+1))
    i = 0
    while len(base_tab) > 0:
        l = len(base_tab)
        t = base_tab[random.randint(a,l-1)]
        while not (t in base_tab):
            t = random.randint(a, l-1)
        r_tab.insert(i,t)
        base_tab.pop(base_tab.index(t))
        i = i+1

    return r_tab

#Exercice 2
#1)
def max(tab):
    max = 0
    for val in tab:
        if val > max:
            max = val
    return max

def min(tab):
    min = sys.maxsize
    for val in tab:
        if val < min:
            min = val
    return min

#2) Les fonctions max et min effectuent n comparaisons

"""3)
        
def min_max(tab):
    return (min(tab),max(tab))
elle effectue 2n comparaisons"""

#4)

def min_max(tab):
    min = sys.maxsize
    max = 0
    l = len(tab)
    if l % 2 == 1:
        for i in range(0,round(l/2)+1):
            for j in range(round(l/2)-1,l):
                if tab[i] < tab[j]:
                    if tab[i] < min:
                        min = tab[i]
                    if tab[j] > max:
                        max = tab[j]
                else:
                    if tab[i] > max:
                        max = tab[i]
                    if tab[j] < min:
                        min = tab[j]
    else:
        for i in range(0,round(l/2)):
            for j in range(round(l/2),l):
                if tab[i] < tab[j]:
                    if tab[i] < min:
                        min = tab[i]
                    if tab[j] > max:
                        max = tab[j]
                else:
                    if tab[i] > max:
                        max = tab[i]
                    if tab[j] < min:
                        min = tab[j]
                        
    return (min, max)           
            
            
#Exercice 3
#1)

alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
     
#2)

def ordre_alphabetique(c1,c2):
    a = c1.lower()
    b = c2.lower()
    if a<b:
        return 1
    if a>b:
        return 2
    if a==b:
        return 0

#3)

def ordre_lexico(m1,m2):
    if len(m1) > len(m2):
        for i,val in enumerate(m2):
            if ordre_alphabetique(val,m1[i]) == 2:
                return 1
            if ordre_alphabetique(val,m1[i]) == 1:
                return 2
        return 2
    if len(m2) > len(m1):
        for i,val in enumerate(m1):
            if ordre_alphabetique(val,m2[i]) == 2:
                return 2
            if ordre_alphabetique(val,m2[i]) == 1:
                return 1
        return 1
    if len(m2) == len(m1):
        for i,val in enumerate(m1):
            if ordre_alphabetique(val,m2[i]) == 2:
                return 2
            if ordre_alphabetique(val,m2[i]) == 1:
                return 1
        return 0
    
#4)
        
def tri_lexico(tab):
    x = 0
    j = 0
    for i in range(1, len(tab)):
        # mémoriser T[i] dans x
        x = tab[i]
        # décaler vers la droite les éléments de T[0]..T[i-1] qui sont plus grands que x en partant de T[i-1]
        j = i                               
        while j > 0 and ordre_lexico(tab[j-1],x) == 2:
            tab[j] = tab[j - 1]
            j = j - 1
        # placer x dans le "trou" laissé par le décalage
        tab[j] = x  
        
    return tab
    
#Exercice 4
#1)
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

#3)
t_tab = []
for i in range(0,10000+1):
    t_tab.append(random.randint(0,100))

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