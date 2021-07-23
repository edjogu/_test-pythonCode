# Defino mi funcion
def sumar (num1, num2):
    return( num1 + num2 )# Retorno el resultado
    

#region Main

operacion = sumar(4, 5) # A la variable operacion, le voy asignar el resultado de la funcion suma(num1, num2)
print(f"El resultado es: {operacion}")

# Puedo llamar a la funcion, las veces que sea necesario

operacion2 = sumar(3, 2) # A la variable operacion, le voy asignar el resultado de la funcion suma(num1, num2)
print(f"El resultado es: {operacion2}")

#endregion Main