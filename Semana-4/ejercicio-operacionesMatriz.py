import random
import numpy as np

matriz_a=[]
matriz_b=[]

def iniciar_matriz(a, b):
    for fila in range(a):
        matriz_a.append([0]*b)

    for i in range(a):
        for j in range(b):
            matriz_a[i][j]=random.randint(1,20)

def mostrar_matriz():
    print("La matriz resultantes es: ")
    for i in matriz_a:
        print(i)

#region Main
filas = int(input("Escriba el numero de filas: "))
columnas = int(input("Escriba el numero de columnas: "))

iniciar_matriz(filas, columnas)
mostrar_matriz()

#endregion Main