#Escribe un programa que permita leer un arreglo de n datos enteros, luego imprime de manera invertida. Guarde el archivo como Arreglo.py
import random
import numpy as np

# a = np.array([
#             [1, 2, 3], 
#             [4, 5, 6]
#             ])

# b = np.array([
#             [0, 0, 0], 
#             [0, 0, 0]
#             ])


# # Recorrer filas
# for i in range(len(a)):
#     # Recorrer columnas
#     for j in range(len(a[0])):
#         b[i][j] = a[i][j]

# for z in b:
#     print(z)

matriz=[]

def iniciar_matriz(a, b):
    for fila in range(a):
        matriz.append([0]*b)

    for i in range(a):
        for j in range(b):
            matriz[i][j]=random.randint(1,20)

def mostrar_matriz():
    print("La matriz resultantes es: ")
    for i in matriz:
        print(i)

#region Main
filas = int(input("Escriba el numero de filas: "))
columnas = int(input("Escriba el numero de columnas: "))

iniciar_matriz(filas, columnas)
mostrar_matriz()

#endregion Main