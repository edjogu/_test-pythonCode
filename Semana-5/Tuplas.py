# a = ()
# print(type(a))

# # Tupla con elementos de distinto tipos:
# a = (1, "dos", 3)
# print(a)
# #vector
# b = (1, 2, 3)
# matriz = (1, 2, 3), (4, 5, 6)
# print(b)
# print(matriz)

#Creacion de tuplas con al función tuple()
# print(tuple())
# print(tuple([1, 2, 3]))
# print(tuple("Python"))
# print(tuple((1,2,3)))

# Operaciones con tuplas
# a = (1, 2, 3)
# print(a)
# print(a[1])
# print(len(a))
# print(a.index(3))
# print(0 in a)
# matriz = (1, 2, 3), (4, 5, 6)
# print(matriz[1])
# print(matriz[1][2])

# Crear una tupla de un solo elemento
# t1 = ("a", )
# print(type(t1))

# # Creau tupla usando la función tuple()
# t = tuple()
# print(t)

# t2 = tuple("hola")
# print(t2)

# t3 = ("a", "b", "c", "d", "e")
# print(t3[0])
# print(t3[1:3])

# # Reemplazar una tupla
# t4 = ("A", ) + t3[1:]
# print(t4)

# Comparar tuplas
# tupla1 = (0, 1, 2) < (0, 3, 4)
# print(tupla1)

# tupla2 = (0, 1, 2000000) < (0, 3, 4)
# print(tupla1)

# Diseño DSU
# txt = "Pero qué luz se deja ver allí"
# palabras = txt.split()
# print(palabras)
# t = list()
# for palabra in palabras:
#     t.append((len(palabra), palabra))
#     print(palabra) 

# t.sort(reverse=False) # True
# print(t) # Longitudes de cada palabra ya comparadas y en orden de longitud

# res = list()
# for longitud, palabra in t:
#     res.append(palabra)
# print(res)

# Asignación de Tuplas
m = ["Pásalo", "bien"]
# x, y = m
# print(m)
# print(x), print(y)

# x = m[0]
# y = m[1]
# print(x), print(y)

# (x, y) = m
# print(x), print(y)

# b= ()
# a = ()
# a, b = b, a
# print(a)
# print(b)

# dir = "monthy@python.org"
# nombreus, dominio = dir.split("@")
# print(nombreus)
# print(dominio)

# Diccionario y Tuplas
# d = {"a":10, "b":1, "c":22}
# print(d)
# t = list(d.items())
# print(t)
# x = t.sort()
# print(x) # Imprimo el diccionario ordenado

# Asignacion múltiple con diccionarios
# d = {"a":10, "b":1, "c":22}

# for clave, valor in list(d.items()):
#     print(clave, valor)

# d = {"a":10, "b":1, "c":22}
# l = list()
# for clave, valor in d.items():
#     l.append((valor ,clave))
# print(l)
# l.sort(reverse=True)
# print(l)

# Uso de Tuplas en diccionarios
# apellido = "Guzman"
# nombre = "Edwar J."
# numero = 3004568967
# directorio = tuple(apellido, nombre)
# # t = tuple()
# directorio[apellido, nombre] = numero

# for apellido, nombre in directorio:
#     print(nombre, apellido, directorio[apellido, nombre])

# Listas y Tuplas:
# tupla = (1, 2, 3, 4)
# print(tupla)

# print(list(tupla))
# lista = [1, 2, 3, 4]
# print(lista)
# print(tuple(lista))

# Concatenación de Tuplas:
lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6, 7, 8]
lista3 = lista1 + lista2
print(lista3)

tupla1 = (1, 2, 3, 4)
tupla2 = (4, 6, 8, 10)
tupla3 = (3, 5, 7, 9)
tupla4 = tupla1 + tupla2 + tupla3
print(tupla4)

# Valor máximo y mínimo en tuplas
print(max(tupla4))
print(min(tupla1))
print(max(tupla1))

print(len(lista3))
print(len(lista1))
print(len(lista2))


