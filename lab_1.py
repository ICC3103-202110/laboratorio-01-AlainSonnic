#Laboratorio_1_Alain_Sonnic_leporati

import random
import time

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
        for j in range(n_pair):
            i.append("*")
    return l_2


#imprime matriz en pantalla
def print_matriz(matriz):        
    g="-"
    g_2=' - '
    print(g*n_pair*3)
    p=[]
    for i in range(n_pair):
        p.append(i)
    print("    ",*p,sep="  ")
    print("    ",g_2*n_pair)
    k=0
    for u in matriz:
        print(k,"|",*u, sep = "  ")
        k += 1
    
    print("    ",g_2*n_pair)
    
    print(g*n_pair*3)

print("Bienvenido a MEMORIZE")
print("La primera coordenada corresponde al eje vertical y la segunda al eje horizontal.")
print("Con Cuantas cartas desea jugar?")


n_pair = int(input())

matriz_aster=matriz_asterisco()
m_card=matriz(n_pair)

punt_1 = 0
punt_2 = 0

turn = 0
first_num = 0
card_disc = 0

#Empieza el ciclo del juego, el jugador 1 comienza hasta que falle.
while card_disc<n_pair*2:
    #turno jugador 1:
    if turn == 0:
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
        matriz_aster[pos1][pos2] = m_card[pos1][pos2]
        num1 = m_card[pos1][pos2]
        print_matriz(matriz_aster)

        print("Indique las coordenadas del segundo numero: ")
        inp = input()
        i = inp.strip().split(",")
        pos_2 = []
        for k in i:
            pos_2.append(int(k))

        pos3,pos4 = pos_2
        matriz_aster[pos3][pos4] = m_card[pos3][pos4]
        
        num2 = m_card[pos3][pos4]
        print_matriz(matriz_aster)
        time.sleep(2)             #Se usa para darle aire al juego y que el jugador no se pierda en la velocidad de los prints.

        if num1==num2:
            print("Ganaste 1 punto!")
            punt_1+=1           #puntaje se le agrega 1 punto.
            card_disc += 2    #numero de cartas que se han dado vuelta.

            matriz_aster[pos1][pos2] = ' '
            m_card[pos1][pos2] = ' '
            matriz_aster[pos3][pos4] = ' '
            m_card[pos3][pos4] = ' '

            time.sleep(1)

        else:
            print("No coinciden :(")
            matriz_aster[pos1][pos2] = '*'
            matriz_aster[pos3][pos4] = '*'
            turn = 1             #si turn ==1, le toca al jugador 2.

    
    #turno jugador 2:
    if turn == 1:
        print("Jugador 2: ")
        print_matriz(matriz_aster)
        print("Indique coordenada de carta a elegir: ")
        print("Indique los numero separados por una coma.")
        inp = input()

        i = inp.strip().split(",")
        pos = []
        for k in i:
            pos.append(int(k))

        pos1,pos2 = pos
        matriz_aster[pos1][pos2] = m_card[pos1][pos2]
        num1 = m_card[pos1][pos2]
        print_matriz(matriz_aster)

        print("Indique las coordenadas del segundo numero: ")
        inp = input()
        i = inp.strip().split(",")
        pos_2 = []
        for k in i:
            pos_2.append(int(k))

        pos3,pos4 = pos_2
        matriz_aster[pos3][pos4] = m_card[pos3][pos4]
        
        num2 = m_card[pos3][pos4]
        print_matriz(matriz_aster)
        time.sleep(1)

        if num1==num2:
            print("Ganaste 1 punto!")
            punt_2+=1
            card_disc += 2

            matriz_aster[pos1][pos2] = ' '
            m_card[pos1][pos2] = ' '
            matriz_aster[pos3][pos4] = ' '
            m_card[pos3][pos4] = ' '

            time.sleep(2)            #para que el jugador no se pierda

        else:
            print("No coinciden :(")
            matriz_aster[pos1][pos2] = '*'
            matriz_aster[pos3][pos4] = '*'
            turn = 0

if punt_1 >= punt_2:
    print("Gano Jugador 1! Con",punt_1," puntos.")
else:
    print("Gano Jugador 2! Con",punt_2," puntos.")