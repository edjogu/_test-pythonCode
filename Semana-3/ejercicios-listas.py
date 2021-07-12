# Crear una lista y almacenar 10 enteros pedidos por teclado. Eliminar todos los elementos que sean iguales al número entero 5.

# listaenteros = list()
# counter = 0
# while counter < 10:
#     numero = input("Escriba el numero para agregar a la lista: ")
#     listaenteros.append(numero)   
#     counter += 1  
  
# print(listaenteros)


# Crear una lista de 5 enteros y cargarlos por teclado. 
# Borrar los elementos mayores o iguales a 10 
# y generar una nueva lista con dichos valores

listaenteros = list()
counter = 1
while counter <= 5:
    numero = int(input(f"Escriba el numero {counter} para agregar a la lista: "))
    listaenteros.append(numero) # Agregando elementos a la lista 
    counter += 1 
  
print(f"Imprimiendo lista creada: {listaenteros}") # Imprimir lista creada

for i in range(len(listaenteros)-1, -1, -1):
    if listaenteros[i] >= 10: # Instrucción para comparar elemento de la lista
        listaenteros.pop(i) # Remover elemento
        #print("Removiendo...", listaenteros[i])   
        print(listaenteros)     
    else:
        print("No hubo coincidencia con el número")
print(f"Imprimiendo lista modificada: {listaenteros}") # Impriir lista modificada       