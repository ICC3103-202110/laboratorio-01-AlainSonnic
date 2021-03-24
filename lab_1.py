#Laboratorio_1_Alain_Sonnic_leporati

import random

#crear matriz con los pares al azar

def matriz(m):
    l=[]
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

#crea matriz de asteriscos
def matriz_asterisco():
    l_2=[]
    for i in range(2):
        l_2.append([])
        
    for i in l_2:
        for j in range(numero_pares):
            i.append("*")
    return l_2


def print_matriz(matriz):
    g="-"
    g_2=' - '
    print(g*numero_pares*3)
    p=[]
    for i in range(numero_pares):
        p.append(i)
    print("    ",*p,sep="  ")
    print("    ",g_2*numero_pares)
    k=0
    for u in matriz:
        print(k,"|",*u, sep = "  ")
        k += 1
    
    print("    ",g_2*numero_pares)
    
    print(g*numero_pares*3)

#MAIN:

print("Bienvenido a MEMORIZE")
print("La primera coordenada corresponde al eje vertical y la segunda al eje horizontal.")
print("Con Cuantas cartas desea jugar?")


numero_pares = int(input())

#numero_pares = 8
matriz_aster=matriz_asterisco()
matriz_cartas=matriz(numero_pares)
flag = 0
punt_1 = 0
punt_2 = 0

#cuando flag cambie a 1, se termina el juego (gana alguien)
turno = 0
primer_num = 0

while flag!=1:
    #turno jugador 1:
    if turno == 0:
        print("Jugador 1: ")
        print_matriz(matriz_aster)
        print("Indique coordenada de carta a elegir: ")
        print("Indique los numero separados por una coma.")
        inp = input()

        i = inp.strip().split(",")
        pos = []
        for k in i:
            pos.append(int(k))

        pos1,pos2 = pos
        matriz_aster[pos1][pos2] = matriz_cartas[pos1][pos2]
        num1 = matriz_cartas[pos1][pos2]
        print_matriz(matriz_aster)
        print("Indique las coordenadas del segundo numero: ")
        inp = input()
        i = inp.strip().split(",")
        pos = []
        for k in i:
            pos.append(int(k))

        pos1,pos2 = pos
        matriz_aster[pos1][pos2] = matriz_cartas[pos1][pos2]
        
        num2 = matriz_cartas[pos1][pos2]
        print_matriz(matriz_aster)

        if num1==num2:
            print("Ganaste 1 punto!")






        turno = 1

    
    #turno jugador 2:
    if turno == 1:
        print("Jugador 2: ")
        print_matriz(matriz_aster)
        print("Indique coordenada de carta a elegir: ")
        print("Indique los numero separados por una coma.")
        inp = input()
        turno = 0