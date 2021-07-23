# def decimal_a_binario(numero_decimal):
#     numero_binario = 0
#     multiplicador = 1

#     while numero_decimal != 0:
#         # se almacena el módulo en el orden correcto
#         numero_binario = numero_binario + numero_decimal % 2 * multiplicador
#         numero_decimal //= 2
#         multiplicador *= 10

#     return numero_binario

# ejemplos de uso

# print(decimal_a_binario(5))
# print(decimal_a_binario(35))
# print(decimal_a_binario(22301))

# def binarizar(decimal):
#     binario = ''
#     while decimal // 2 != 0:
#         binario = str(decimal % 2) + binario
#         decimal = decimal // 2
#     return str(decimal) + binario

# numero = int(input('Introduce el número a convertir a binario: '))
# print(binarizar(numero))

print(5//2)
print(5%2)
print(2//2)
print(2%2)
print(1//2)
print(1%2)

def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

numero = int(input('Introduce el número a convertir a binario: '))
print(binarizar(numero))