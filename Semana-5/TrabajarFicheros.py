
# Defino la ruta del archivo
# path = "C:\_curso\_semana5\datos.txt"
path = "C:\_curso\_semana5\dato2.txt"
# Abro archivo en modo lectura
archivo = open(path, "r", encoding='utf8') 

# inicia bucle infinito para leer línea a línea
while True: 
    linea = archivo.readline()  # lee línea
    if not linea: 
        break  # Si no hay más se rompe bucle
    print(linea)  # Muestra la línea leída
archivo.close()  # Cierra archivo

