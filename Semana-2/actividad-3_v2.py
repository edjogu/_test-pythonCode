import time


#  Funcion menu
def menu():
    print("================================= Menu de Opciones =================================")
    print("0. Salir")
    print("1. Saludar")
    print("2. Calcular si un número es par")
    print("3. Calcular el promedio de 5 notas")
    print("4. Calcular el porcentaje")
    print("5. Elevar a una potencia")
    print("6. Calcular el módulo")
    print("====================================================================================")

# Función Saludar
def saludar():
    saludo = 'Saludos desde Python'
    print (saludo)

#region Main
opcion = None
while opcion != 0:
    menu()
    opcion = int(input("Seleccione una opción: "))
    if opcion >= 0 and opcion <= 6:
        if opcion == 1:
            saludar() # Llamo a la fución saludar()
            time.sleep(2)
        elif opcion == 2:
            print("Calcular número par") # Llamo a la función calcularpar()
            time.sleep(2)
        elif opcion == 3:
            print("Calcular promedio de 5 notas") # Llamo a la función calcularpromedio()
            time.sleep(2)
        elif opcion == 4:
            print("Calcular porcentaje") # Llamo a la función calcularporcentaje()
            time.sleep(2)
        elif opcion == 5:
            print("Elevar a una potencia") # Llamo a la función calcularpotencia()
            time.sleep(2)
        elif opcion == 6:
            print("Calcular el módulo") # Llamo a la función calcularmodulo()
            time.sleep(2)        
    else:
        print("Opción no válida")
        time.sleep(2)
print("Saliendo del programa")
time.sleep(2)
exit()    
#endregion Main

