def mostrarnombre(nombre, apellido):
    full_name = nombre, apellido
    print(full_name)

def area_traingulo(base, altura):
    return (base * altura) / 2

def bienvenida(nombre, lenguaje="Python"):
    print("Bienvenido a", lenguaje, nombre + "!")
    #return

def menudeldia(*platos):
    print("Hoy tenemos: ", end=" ")
    for plato in platos:
        print(plato, end=" ")
    #return

# Llamar la función
# nombre1 = input("Escriba el primer nombre: ")
# apellido1 = input("Escriba el primer apelido: ")
# mostrarnombre(nombre1, apellido1)

# print(area_traingulo(10, 5))
# resultado = area_traingulo (10, 5)
# print(resultado)
# resutado = bienvenida("Edwar")
# resutado2 = bienvenida("Edwar", "C#")
# print(bienvenida("Edwar"))
# print(bienvenida("Edwar", "Java"))

menudeldia("Pasta", "Sopa", "Bagre", "Salmon")
