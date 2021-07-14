# 
import numpy as np

# matriz = [
#     [21, 22, 23],
#     [34, 35, 36],
#     [47, 48, 49]
# ]

#matriz_np = np.array(matriz)
# print(matriz_np)

# i = 1
# columna = matriz_np[:, i]
# print(columna)

a = np.array([
            [1, 2, 3], 
            [4, 5, 6]
            ])

b = np.array([
            [1, 1, 1], 
            [2, 2, 2]
            ])

c = np.array([
            [1, 2, 3]
            ])
# print(a[1, 0])
# print(a[1][0])
# print(a[:, 0:2]) # : Fila , Columna # : todas las fila y 0:2 las dos primeras columnas

# print(a[1, 1])
# print(a[:, 2])
# print(a[0, :])
# print(a[0, ::-1])

# print(a.sum())
# print(a[0, :].sum()) # En la fila 0, sumar todos los elementos de la columna por medio de la función sum()
# print(a.flatten())
# # parametros flatten ('C', 'F', 'A', 'K')

# Operaciones. Se debe considerar de la misma dimensión
# print(a + b)
# print(a / b)
# print(a ** 2)

print(a * c)
print(a + c)