import fonctions
import random
import sys

#Exercice 1 :

#2) 

t1 = list(range(0,100))
t2 = sorted(t1,reverse=True)
t3 = permutation(0,99)

#1)
print(double_tab(t1))#renvoie un très grand tableau

#Exercice 2 :
#1)

print(max(t2))#renvoie 99
print(min(t3))#renvoie 0

#2) Elles effectuent n comparaisons

"""3) enlever les commentaires dans fonctions.py et ici pour tester 
print(max(t1))
"""

#4)
print(min_max(t3))#renvoie (0,99)

#Exercice 3:
#1)

alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

#2) 
print(ordre_alphabetique('a','z')) #renvoie 1
print(ordre_alphabetique('Z', 'a')) #renvoie 2
print(ordre_alphabetique('t','t')) #renvoie 0

#3)
m1 = "ballon"
m2 = "ballo"
m3 = "exercice"
print(ordre_lexico(m1,m2)) #renvoie 2
print(ordre_lexico(m2,m3)) #renvoie 1
print(ordre_lexico(m3,m1))#renvoie 2
print(ordre_lexico(m1,m3))#renvoie 1
print(ordre_lexico(m1,m1)) #renvoie 0

#4)
T = [m3,m1,m2]
print(tri_lexico(T))#renvoie ['ballo', 'ballon', 'exercice']    