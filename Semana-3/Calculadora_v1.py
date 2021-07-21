# 4. Crea un programa que se llame Calculadora.py y que calcule la suma, la resta, la multiplicación, la división y la potencia cuadrada entre dos numeros

# Variables
msgError = "Opción no válida"
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

#endregion Operaciones

def menu():
    print("-------------------Calculadora-------------------")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potenciar")
    print("-------------------------------------------------")


#region Main

menu()
operador = int(input("Que operación desea realizar: "))
num1 = int(input("Escriba primer numero:" ))
num2 = int(input("Escriba segundo numero:" ))

if  operador == 1:
    resultado = suma(num1, num2)
    print(f"La suma es {resultado}")
elif operador == 2:
    resultado = resta(num1, num2)
    print(f"La resta es {resultado}")
elif operador == 3:
    resultado = multiplicar(num1, num2)
    print(f"La multiplicación es {resultado}")
elif operador == 4:
    resultado = division(num1, num2)
    print(f"La división es {resultado}")
elif operador == 5:
    resultado = potencia(num1, num2)
    print(f"La potencia es {resultado}")
else:
    print(f"{operador} {msgError}")
#endregion Main