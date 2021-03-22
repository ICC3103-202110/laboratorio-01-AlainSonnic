#Laboratorio_1_Alain_Sonnic_leporati

import random
"""
print("Bienvenido a MEMORIZE")

print("Con Cuantas cartas desea jugar?")

numero = int(input())

"""
numero_pares = 10

l=[]

#crear matriz

def matriz(m,l):
    for i in range(2):
        l.append([])
        
    for i in l:
        for j in range(m):
            i.append(0)
    
    j=0
    lis=[]
    
    while j<2*m:
        
        k=random.randrange(2)
        n=random.randrange(m)
        
        if (k,n) not in lis:
                lis.append((k,n))
                j+=1
    o=0
    for i in range(2):
        for k in range(1,m+1):
            pos1,pos2=lis[o]
            l[pos1][pos2]=k
            o+=1
            
         
    print(lis)
    
    return l

i=matriz(numero_pares,l)

print (i)
        