import triCompte
import random

#3)
t1 = []
for i in range(0,10000+1):
    t1.append(random.randint(0,100))
     
t2 = t1
     
print(tri_compte1(t1,max(t1))) #on pourrait donner 100 en argument mais on va se permettre une optimisation ici

#4)
tri_compte2(t1, max(t1))
print(t1)

#5)
tri_compte3(t2)
print(t2)