
# 4. Crea un programa que se llame Calculadora.py y que calcule la suma, la resta, la multiplicación, la división y la potencia cuadrada entre dos numeros
# Operaciones disponibles para la calculadora: suma, resta, multiplicación, logaritmo, coseno, seno, raíz cuadrada, convertir decimal a binario y binario a decimal.

# MinTIC 
# Autor: guzmanE
# Date        Description
# 01.07.21    Initial version
# 14.07.21    Optimizado (Uso de funciones y otras operaciones)
# --          --

# Variables
import time
import math


msgError = "Opción no válida"

def menu():
    print("-------------------Calculadora-------------------")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potenciar")
    print("6. Logaritmo")
    print("7. Coseno")
    print("8. Seno")
    print("9. Raiz Cuadrada")
    print("10. Convertir Decimal a Binario")
    print("11. Convertir Binario a Decimal")
    print("-------------------------------------------------")

def validaropcion(opt):
    if opt == "S":
        return 1
    elif opt == "N":
        return 0
    else:
        print("Por favor escriba S o N")

#region Operaciones

# Suma
def suma(num1, num2):
    return num1 + num2
# Resta
def resta(num1, num2):
    return num1 - num2
# Multiplicar
def multiplicar(num1, num2):
    return num1 * num2
# División
def division(num1, num2):
    return num1 / num2
# Potencia cuadrada
def potencia(num1, num2):
    return num1 ** num2

def logaritmo(num1):    
    return math.log10(num1)

def coseno(num1):
    return math.cos(num1)

def seno(num1):
    return math.sin(num1)

def raizcuadrada(num1):
    return math.sqrt(num1)

def decimal2binario(num1):
    num_binario = ""
    while num1 // 2 != 0:
        num_binario = str(num1 % 2) + num_binario
        num1 = num1 // 2
    return str(num1) + num_binario

def binario2decimal(num1):
    return int(str(num1), 2)

#endregion Operaciones

#region Main
continuar = None
while continuar != 0:
    menu()
    operador = int(input("Que operación desea realizar: "))
    if operador > 0 and operador <= 5:
        operando1 = int(input("Escriba primer numero: " ))
        operando2 = int(input("Escriba segundo numero: " ))
        if  operador == 1:
            resultado = suma(operando1, operando2)
            print(f"La suma es {resultado}")
        elif operador == 2:
            resultado = resta(operando1, operando2)
            print(f"La resta es {resultado}")
        elif operador == 3:
            resultado = multiplicar(operando1, operando2)
            print(f"La multiplicación es {resultado}")
        elif operador == 4:
            resultado = division(operando1, operando2)
            print(f"La división es {resultado}")
        elif operador == 5:
            resultado = potencia(operando1, operando2)
            print(f"La potencia es {resultado}")        
    elif operador >= 6 and operador <= 11:
        numero = int(input("Escriba el numero a evaluar: " ))            
        if  operador == 6:
            resultado = logaritmo(numero)
            print(f"EL logaritmo de {numero} es {resultado}")  
        elif operador == 7:
            resultado = coseno(numero)
            print(f"EL coseno de {numero} es {resultado}")
        elif operador == 8:
            resultado = seno(numero)
            print(f"EL seno de {numero} es {resultado}")
        elif operador == 9:
            resultado = raizcuadrada(numero)
            print(f"El numero {numero} en binario es {resultado}")
        elif operador == 10:
            resultado = decimal2binario(numero)
            print(f"El numero {numero} en binario es {resultado}")
        elif operador == 11:
            resultado = binario2decimal(numero)
            print(f"El numero {numero} en decimal es {resultado}")        
    else:
        print("Opción no válida")    
    opcion = input("Desea Continuar (S/N) ? ")
    continuar = validaropcion(opcion)
    time.sleep(2)
print("Saliendo del programa")
#endregion Main




