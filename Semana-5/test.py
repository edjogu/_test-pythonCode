# RF02 
# # Función para leer/actualizar la matriz de ubicaciones desde un archivo existente (Importar desde archivo)


pre_coordinates=[[-3.777,-70.302,91],
                [-4.134,-69.983,233],
                [-4.006,-70.132,149],
                [-3,846,-70,222,211]]


def import_coordinates_file(archivo):
    line=open(archivo).readline()
    line=line.split(";")
    listupdate=[]
    for i in range(0,4):
        listupdate.append([])
        tmp=line[i].split(",")
        for j in range(0,3):
            listupdate[i].append(tmp[j])
        
    for i in range(len(listupdate)):
        for j in range(0,len(listupdate[i])):
            listupdate[i][j]=float(listupdate[i][j])
            if j==2:
                listupdate[i][j]=int(listupdate[i][j])

    # Mostrar al usuario la actualización de las coordenadas
    print("Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal: ")
    opt_exit = input(" ")
    if opt_exit == 0:
        pass
    else:
        pass
    return listupdate

print(pre_coordinates)
pre_coordinates = (import_coordinates_file(r"C:\MinTIC\Semana-5\updatecoordenadas.txt"))
print(pre_coordinates)