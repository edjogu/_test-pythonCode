import os


#path = "C:\_curso\_semana5\dato2.txt"
#path = "C:\_curso\_semana5\dato2.txt"
# archivo = open(path, "a", encoding="utf8")

# path = "C:\_curso\_semana5\datos.txt"
# archivo = open(path, "a")
#archivo.write("Ya casi terminamos!")
#archivo.write("Bienvenido a Python nuevamente!")
# archivo.write("\n ¡Casi terminamos!")
#archivo.write("\n ¡Ya Casi terminamos!")
# archivo.write("\n ¡Hola niñas!")

# read
# archivo = open(path, "r")
# contenido = archivo.read()
# print(contenido)

# readline
# archivo = open(path, "r", encoding='utf8') 
# for linea in archivo.readline():
#     print(linea)
# archivo.close()

# seek()
# archivo = open(path, "r", encoding="utf-8")
# contenido = archivo.read()
# archivo.seek(10)
# print(archivo.tell())
# print(archivo.read())

# tell()
# archivo = open(path, "r", encoding='utf8') 
# linea1 = archivo.readline()
# mas = archivo.read(archivo.tell() * 2)
# if archivo.tell() > 50:
#     archivo.seek(50)
# print(archivo)

# archivo = open(path, "r+", encoding='utf8')
# contenido = archivo.read()
# end_of_file = archivo.tell()
# lista = ["Linea 1\n", "Linea 2"]
# archivo.writelines(lista)
# archivo.seek(end_of_file)
# print(archivo.readline())
# print(archivo.readline())
# archivo.close()

# archivo = open(path, "r+", encoding='utf8')
# contenido = archivo.read()
# archivo.close()
# print(contenido)

# Propiedades del objeto file

# archivo = open(path, "r+", encoding='utf8')
# contenido = archivo.read()
# nombre = archivo.name
# modo = archivo.mode
# enco = archivo.encoding
# archivo.close()

# print(nombre, modo, enco)
# if archivo.closed:
#     print(f"El archivo {nombre} se ha cerrado correctamente.")
# else:
#     print(f"El archivo {nombre} permanece abierto.")

# Renombrar y mover ficheros

# ruta = "C:\_curso\_semana5\bienvenida.txt"
path = "C:\_curso\_semana5\dato1.txt"

if os.path.isfile(path):
    os.rename(path, "saludo.txt") # Renombrar archivo si existe
else:
    print(f"El archivo: {path} NO existe!")

# ruta = "C:\file\bienvenida.txt"
# if os.path.isfile(ruta):
#     os.remove(ruta) # Borrarlo
# else:
#     print(f"El archivo: {ruta} NO existe!")







