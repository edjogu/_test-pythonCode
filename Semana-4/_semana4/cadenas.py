fruta = "banana"
# letra = fruta[1]
# letra = fruta[1.5] # muestra un error

# letra = len(fruta)
# tamano = letra
# ultima = fruta[tamano-1]
# ultima = fruta[len(fruta) - 1]

# print(letra)
# print(ultima)

# contador = 0
# while contador < len(fruta):
#     letra = fruta[contador]
#     print(letra)
#     contador += 1

# for letra in fruta:
#     print(letra)


# s = "Monty Python"
# print(s[0:5])
# print(s[6:12])

# print(fruta[:3])
# print(fruta[3:])
# print(fruta[3:3])

# saludo = "Hola mundo"
# # saludo[0] = "J"
# nuevo_saludo = "J" + saludo[1:]
# print(nuevo_saludo)


# palabra = "banana"
# palabra2 = "Hola mundo"
# contador = 0
# for letra in palabra:
#     if letra == "a":
#         contador += 1
# print(f"La cantidad de veces que el caracter {letra} aparace en la cadena {palabra} es {contador}")

# x = "a" not in palabra
# y = "semilla" in palabra
# print(x)
# print(y)


# print(dir(palabra2))
# print(palabra2.count(palabra2))
# print(palabra2.upper())

# Cantidad de veces que aparace un caracyer en especifico dentro de una cadena
# caracter = "a"
# x = palabra.count(caracter)
# print(f"La cantidad de veces que aparace {caracter} en la cadena {palabra} es {x}")


# print(palabra.find("na"))

# linea = " Aqui vamos"
# print(linea.strip())

# linea = "Que tengas buen día"
# buscar = "Que"
# buscar2 = "q"
# print(linea.startswith(buscar))
# # print(linea.startswith(buscar2))
# print(linea.lower().startswith(buscar))

# dato = "From edwar.guzman@utc.ac.za Sat 5 09:14:16 2021"
# posarroba = dato.find("@")
# print(posarroba)

# posesp = dato.find(" ",posarroba)
# print(posesp)

# direccion = dato[posarroba + 1 : posesp]
# print(direccion)

# cadena = "bienvenido a mi aplicación"
# # print(cadena.capitalize())
# # print(cadena.title())
# print(cadena.center(50, "="))
# print(cadena.center(50, "="))
# print(cadena.rjust(50, "="))
# print(cadena.ljust(50, "="))


# # List Comprehension in Python
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # for x in lst:
# #     print(x)
# a = [x for x in lst]
# # print(a)

# for x in lst:
#     a.append(x)

# a = [x+1 for x in lst]
# print(a)

# a = [x*2 for x in lst]
# print(a)

# for x in lst:
#     if x > 4:
#         a.append(x)
# print(a)

# c = [x for x in lst if x > 4]
# print(c)

cadena = "pepegrillo 75"
cadena1 = "pepegrillo"
cadena2 = "1234"
cadena3 = "12.34"
cadena4 = "pepegrillo75"
cadena5 = "PEPEGRILLO"
cadena6 = "pepe grillo"
cadena7 = "   "
print(cadena.isalnum())
cadena8 = "Pepe Grillo"
# res = cadena.trip()
# print(res.isalnum())

print(cadena.isalpha())
print(cadena1.isalpha())
print(cadena1.isdigit())
print(cadena2.isdigit())
print(cadena3.isdigit())
print(cadena4.islower())
print(cadena5.isupper())
print(cadena6.isspace())
print(cadena7.isspace())
print(cadena8.istitle())

# buscar = "nombre apellido"
# reemplazar_por = "Edwar Guzman"
# print(f"Estimado Sr. nombre apellido:".replace(buscar, reemplazar_por))

# cadena10 = " www.python.com "
# cadena11 = "       www.python.com"
# print(cadena10.strip())
# print(cadena10.strip(" "))
# print(cadena10.lstrip(" w." ))
# print(cadena11.lstrip())


# area_triangulo = lambda base, altura : (base * altura) / 2
# print((lambda b, a : (b*a)/2)(12, 4))
# print(area_triangulo(12, 4))

# palabras = "phyton, guia, curso, tutorial".split(", ")
# print(palabras)

palabra = "piña"
# palabra = "banana"

# if palabra == "banana":
#     print("Muy bien, bananas.")

if palabra.lower() < "banana":
    print("Tu palabra, " + palabra + ", esta antes de banana.")
elif palabra.lower() > "banana":
    print("Tu palabra, " + palabra + ", esta despues de banana.")
else:
    print("Muy bien, bananas.")

datos = [
    [9, "Jc", 2],
    [7, "aK", 5],
    [4, "Sv", 6],
    [3, "Dw", 5],
    [5, "mx", 4]
]

datos.sort(key = lambda x : x[0] + x[2])
print(datos)

letras = ["Ec", "ar", "ij", "Iw", "An", "es"]
#letras.sort(key = str.lower)
letras.sort(key = lambda cadena : cadena.lower())
print(letras)

datos = [257, 573, -714, 321, -158, 642, 407]
print(max(datos))
print(min(datos))
print(min(datos, key=abs))



