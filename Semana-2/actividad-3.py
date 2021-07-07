# 1. Saludar 
# 2. Calcular si un número es par 
# 3. Calcular el promedio de 5 notas
# 4. Calcular el módulo 
# 5. Calcular el porcentaje 
# 6. Elevar a una potencia

import time


opcion0 = "Salir";
opcion1 = "Saludar";
opcion2 = "Calcular si un número es par";
opcion3 = "Calcular el promedio de 5 notas";
opcion4 = "Calcular el módulo";
opcion5 = "Calcular el porcentaje ";
opcion6 = "Elevar a una potencia";
opcionLista = [opcion0, opcion1, opcion2, opcion3, opcion4, opcion5, opcion6];

# Imprimir opciones
def imprimiropciones():
    for x in range(0, len(opcionLista)):
        print(f"{x} - {opcionLista[x]}")

# Función Saludar
def saludar():
    saludo = 'Saludos desde Python'
    print (saludo) 

# Funcion Validar si un número es par
def validarpar(num):
    if num % 2 == 0:
        print (f"El numero {num} es par.")
    else:
        print(f"El numero {num} no es par.")

# Calcula promedio
def calcularpromedio():
    # Definir constante
    materias = 5

    # Pedir daos del estudiante
    nombre = input("Nombre completo del Estudiante: ")
    grado = input("Grado: ")
    grupo = input("Grupo: ")

    # Hacer ciclo para pedir datos y hacer la sumatoria
    # Uso de contador count
    counter = 1
    # Uso de Acumulador
    sumatoria = 0

    while counter <= materias:
        asignatura = input(f"Nombre asignatura {counter}: ")
        nota_asignatura = float(input(f"Ingrese calificacion de la asignatura {asignatura}: "))
        # Sumar la calificacion por asignatura
        sumatoria = sumatoria + nota_asignatura
        # Aumentar counter para controlar el ciclo
        counter += 1;

    #Calcular e imprimir
    promedio =  sumatoria / materias

    print(f"******************** Resultados ********************")
    print(f"Estudiante: {nombre} | {grado} {grupo}")
    print(f"********************  ********************")
    print(f"Promedio: {promedio}")
    print(f"********************  ********************")

# Calcular el módulo
def calcularmodulo(num1, num2):
    mod = num1 % num2
    return mod 

# Calcular Pocentaje
def calcularporcentaje(porcentaje, num1):
    return (porcentaje * num1) / 100

# Elevar potencia 
def elevarpotencia(num1, num2):
    res = (num1 ** num2) 
    return res


#region Main
select_opt = None
while select_opt != 0:    
    imprimiropciones()
    select_opt = int(input("Elija una opción: "))
    if select_opt > 0 and select_opt < 6:
        opcion = opcionLista[select_opt]
        if opcion == opcion1:
            saludar()
            time.sleep(2) 
        elif opcion == opcion2:
            validarpar(int(input("Escriba el número a evaluar: ")))
            time.sleep(2)  
        elif opcion == opcion3:
            calcularpromedio()
            time.sleep(2) 
        elif opcion == opcion4:
            resto = calcularmodulo(int(input("Escriba el primer número: ")), int(input("Escriba el segundo número: ")))
            print(f"El resto o módulo de los dos números es: {resto}")
            time.sleep(2) 
        elif opcion == opcion5:
            valor_porcentaje = calcularporcentaje(float(input("Escriba el porcentaje a aplicar: ")), float(input("Escriba el número: ")))
            print(f"El porcentaje es: {valor_porcentaje}")
            time.sleep(2) 
        elif opcion == opcion6:
            valor_potencia = elevarpotencia(int(input("Escriba el primer número: ")), int(input("Escriba el segundo número: ")))
            print(f"El resultado de la potencia es: {valor_potencia}")
            time.sleep(2)
    else:
        print("Opción no válida")
print("Saliendo del programa...")  

#endregion Main