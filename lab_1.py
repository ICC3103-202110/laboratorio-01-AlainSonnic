#Laboratorio_1_Alain_Sonnic_leporati

import random
"""
from tabulate import tabulate

print("Bienvenido a MEMORIZE")

print("Con Cuantas cartas desea jugar?")

numero = int(input())
numero_pares = int(input())

"""
numero_pares = 10

l=[]

#crear matriz con los pares al azar

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
    return l

l_2=[]

#crea matriz de asteriscos
def matriz_asterisco(l_2):
    for i in range(2):
        l_2.append([])
        
    for i in l_2:
        for j in range(numero_pares):
            i.append("*")

matriz_asterisco(l_2)
matriz_cartas=matriz(numero_pares,l)

def print_matriz(matriz):
    g="-"
    g_2=' - '
    print(g*numero_pares*3)
    p=[]
    for i in range(numero_pares):
        p.append(i)
    print("    ",*p,sep="  ")
    print("   ",g_2*numero_pares)
    k=0
    for u in matriz:
        print(k,"|",*u, sep = "  ")
        k += 1
    
    
    print(g*numero_pares*3)
        

print_matriz(l_2)

flag = 0
punt_1 = 0
punt_2 = 0

#cuando flag cambie a 1, se termina el juego (gana alguien)
turno=0
'''
while flag!=1:
    #turno jugador 1:
    if turno == 0:
        print("Jugador 1: ")
        print_matriz(l_2)
        print("Indique coordenada de carta a elegir: ")
        print("Indique los numero separados por una coma.")
        inp = input()

    
    #turno jugador 2:
    if turno == 1:
    '''