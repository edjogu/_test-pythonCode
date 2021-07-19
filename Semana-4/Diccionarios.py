#  Acceder a los elementos de un diccionario
a = {"Nombre" : "Alfredo", "Despacho" : 402, "email" : "alfredo@gmail.com"}
# print(a["Nombre"])
# print(a["Despacho"])
# print(a)
# print(a.get("email"))
# print(a.get("Univeridad", "CEU"))

# Funciones NO Modifican
# print(len(a))
# print(min(a))
# print("email" in a)
# print(a.keys())
# print(a.values())
# print(a.items())

# Funciones SI Modifican
# a["Universidad"] = "USABU"
# print(a)
# a.pop("Despacho")
# print(a)
# # a.popitem("Universidad", "USABU")
# print(a)
# a.clear()
# print(a)

# diccionario = {"one": "uno", "two" : "dos", "three" : "tres"}
# print(diccionario)

# print(diccionario["four"])

# diccionario = {"chuck":"1", "annie":"42", "jan":"100"}
# for par in diccionario:
#     print(par, diccionario[par])

# for par in diccionario:
#     if diccionario[par] > 10:
#         print(par, diccionario[par])

# diccionario = {"chuck":1, "annie":42, "jan":100}
# listacopia = list(diccionario.keys())
# print(listacopia)
# listacopia.sort()
# for par in listacopia:
#     print(par, diccionario[par])

# Métodos principales en los Diccionarios
# Método clear()

# diccionario = {"color":"violeta", "talle":"XS", "precio":174.25}
# print(diccionario)
# diccionario.clear()
# print(diccionario)

# Claves de una secuencia

# secuencia = {"color", "talle", "marca"}
# diccionario1 = dict.fromkeys(secuencia)
# print(diccionario1)

# diccionario2 = dict.fromkeys(secuencia, "valor x defecto")
# print(diccionario2)

# Metodo copy
# diccionario = {"color":"violeta", "talle":"XS", "precio":174.25}
# remera = diccionario.copy()
# print(diccionario)
# print(remera)
# diccionario.clear()
# print(diccionario)
# print(remera)
# musculosa = remera
# print(remera)
# print(musculosa)
# remera.clear()
# print(remera)
# print(musculosa)

# Usando setdefault()
# remera = {"color":"rosa", "marca":"Zara"}
# clave = remera.setdefault("talle", "U")
# print(clave)
# print(remera)

# remera2 = remera.copy()
# print(remera2)
# clave = remera2.setdefault("estampado")
# print(clave)
# print(remera2)

# clave = remera2.setdefault("marca", "Lacoste")
# print(clave)
# print(remera2)

# Concatenar diccionarios
diccionario1 = {"color":"verde", "precio":45}
# diccionario2 = {"talle":"M", "marca":"Lacoste"}
# diccionario1.update(diccionario2)
# print(diccionario1)

# Obtener el valor de una clave
print(diccionario1.get("color"))
print(diccionario1.get("stock", "sin stock"))
print(diccionario1)






