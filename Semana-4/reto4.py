# MinTIC Reto 4 - Cuarta parte
# Autor: guzmanE
# Date        Description
# 01.07.21    Initial version
# 02.07.21    Optimizado (Uso de funciones def)
# 07.07.21    RF01 Actualizar contraseña.
# 07.07.21    RF02 Ingresar coordenadas de los tres sitios que más frecuenta (trabajo, casa, parque).
# 18.07.21    RF03: El programa permite al usuario actualizar las coordenadas de los tres sitios más frecuentados.
# 21.07.21    RF01: El programa dispone de manera predefinida la ubicación de cuatro zonas wifi con su respectivo promedio de usuarios.


# --          --

# Sistema Login @ TicNet Corp @

# Define Variables
#
# if latitude >= -3.002  and latitude <= -4.227: # Validar que este dentro del rango
# if longitud >= -69.714  and longitud <= -70.365: # Validar que este dentro del rango

# RF01
# Datos para trabajar según pemultimo código:
#Lat1: -3,777   #Lon1: -70,302  #Promedio de usuarios: 91
#Lat2: -4,134   #Lon2: -69,983  #Promedio de usuarios: 233
#Lat3: -4,006   #Lon3: -70,132  #Promedio de usuarios:149
#Lat4: -3,846   #Lon4: -70,222  #Promedio de usuarios: 211

import time
import os
from math import asin, cos, sin, sqrt, radians, degrees


#region Variables Globales
msgBienvenido = "Bienvenido al sistema de ubicación para zonas públicas WIFI"
msgError = "Error"
msgOk = "Sesión iniciada"
msg_error_coordinate = "Error coordenada"
msg_error_update = "Error actualización"
msg_error_not_coordinates = "Error sin registro de coordenadas"
msg_error_ubicacion = "Error ubicación"
msg_error_wifi = "Error zona wifi"
name = "52208"
stored_passw = "80225"
calDigito = ((8 // 2) + 8)  - (2 ** 2 + (5 * 2) - 2)
captcha = 208
radio=6372.795477598
iMenu01 = "Cambiar contraseña";
iMenu02 = "Ingresar coordenadas actuales";
iMenu03 = "Ubicar zona wifi más cercana";
iMenu04 = "Guardar archivo con ubicación cercana";
iMenu05 = "Actualizar registros de zonas wifi desde archivo";
iMenu06 = "Elegir opción de menú favorita";
iMenu07 = "Cerrar sesión";
# Definir lista 
optMenuList = [iMenu01, iMenu02, iMenu03, iMenu04, iMenu05, iMenu06, iMenu07];
countErrors = 0
# Definir lista vacía para las coordenadas
coordinates = []
# Definir lista vacía para las distancias calculadas
list_distance=[]
# tmp_coordinates = [[None, None], 
#                 [None, None], 
#                 [None, None]]

tmp_coordinates=[[10.103,-74.902],
                 [10.115,-75.085],
                 [10.108,-74.801]]

pre_coordinates=[[-3.777,-70.302,91],
                [-4.134,-69.983,233],
                [-4.006,-70.132,149],
                [-3,846,-70,222,211]]

current_location=None #Creamos una variable que usaremos globalmente para facilitar un poco el traspaso de información
distancia_tiempo=None # declaramos una nueva variable global para guardar la distancia final


#endregion Variables Globales

#region Funciones
def validatedata(dato1, dato2):
    if dato1 == dato2:
        return True
    else:
        return False

def PrintMenuList():
    for y in range(len(optMenuList)):
        print(f"{y + 1} - {optMenuList[y]}") 

def ReorderMenuList(newFavOpt):
    tempOpt = optMenuList[newFavOpt-1]
    optMenuList.remove(tempOpt)
    optMenuList.insert(0, tempOpt)

def changepassword(current_passw):
    if validatedata(input("Por favor, ingrese su contraseña actual: "), current_passw):
        new_passw = input("Por favor ingrese su nueva contraseña: ")
        if validatedata(new_passw, current_passw):
            ErrorMessage(msgError) # La nueva contraseña no puede ser igual a la contraseña actual.
            return current_passw
        else:            
            if validatedata(input("Confirme su nueva contraseña: "), new_passw):
                return new_passw                
            else:
                ErrorMessage(msgError)
                return current_passw
    else:
        ErrorMessage(msgError)
        exit()    
    
def ErrorMessage(msg):
    os.system("cls")
    print(msg)
    time.sleep(2)

def addcoordinates(list_coordinates):
    lista = list(list_coordinates)
    for i in range (0, 3):
        lista.append([])
        latitude = input("Ingrese la latitud: ") # Ingresar latitud
        if latitude == "" or latitude == " ": # validar que ingrese un valor de latitud válido
            ErrorMessage(msgError) # Muestra error y sale del programa
            lista = []
            exit()
        else:
            latitude = float(latitude) # Cast a float para validar rango de latitud
            if latitude >= -4.227 and latitude <= -3.002: # Validar que este dentro del rango
                longitud = input("Ingrese la longitud: ") # Ingresar longuitud
                if longitud == "" or longitud == " ": # validar que ingrese un valor de longuitud válido
                    ErrorMessage(msgError) # Muestra error y sale del programa
                    lista = []
                    #return lista
                    exit()
                else:
                    longitud = float(longitud) # Cast a float para validar rango de longuitud
                    if longitud >= -70.365  and longitud <= -69.714: # Validar que este dentro del rango
                        lista[i].insert(0, latitude)
                        lista[i].insert(1, longitud)
                    else:
                        ErrorMessage(msg_error_coordinate)
                        lista = []
                        exit()
            else:
                ErrorMessage(msg_error_coordinate)
                lista = []
                exit()
    return lista  

def printcoordinates(list_coordinates):
    lista = list(list_coordinates)
    print(f"Las coordenadas guardadas actualmente son: ")
    for i in range(0, len(lista)):
        print(f"coordenada [latitud,longitud] {i + 1} : {[lista[i][0]]} {[lista[i][1]]}")
    # Llamar a la funcion información coordenadas
    infocoordinates(lista)
    # Llamar a la funcion promedio coordenadas
    avgcoordinates(lista)
    # Modificar opción:
    option = int(input("Presione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú: "))
    if option != 1 and option != 2 and option !=3:
        ErrorMessage(msg_error_update)
        exit()
    else:
        updatecoordinates(option, list_coordinates)             

def infocoordinates(list_coordinates):
    print(f"La coordenada que está mas al occidente: {min(list_coordinates, key=lambda posicion: posicion[0])}")

def avgcoordinates(list_coordinates):
    print(f"Coordenada promedio de todos los puntos: {(list_coordinates[0][0]+list_coordinates[1][0]+list_coordinates[2][0])/3}")
    
def updatecoordinates(option, list_coordinates):
    option -=1
    lista = list(list_coordinates)
    latitude = input("Ingrese la latitud: ") # Ingresar latitud
    if latitude == "" or latitude == " ": # validar que ingrese un valor de latitud válido
        ErrorMessage(msgError) # Muestra error y sale del programa
        exit()
    else:
        latitude = float(latitude) # Cast a float para validar rango de latitud
        if latitude >= -4.227 and latitude <= -3.002: # Validar que este dentro del rango
            longitud = input("Ingrese la longitud: ") # Ingresar longuitud
            if longitud == "" or longitud == " ": # validar que ingrese un valor de longuitud válido
                ErrorMessage(msgError) # Muestra error y sale del programa
                exit()
            else:
                longitud = float(longitud) # Cast a float para validar rango de longuitud
                if longitud >= -70.365  and longitud <= -69.714: # Validar que este dentro del rango
                    lista[option][0] = latitude
                    lista[option][1] = longitud
                else:
                    ErrorMessage(msg_error_coordinate)
                    lista = [list_coordinates]
                    exit()
        else:
            ErrorMessage(msg_error_coordinate)
            lista = [list_coordinates]
            exit()
    return lista 
    
def favorite_wifi_zones(list_coordinates):
    if list_coordinates == []: # Si el usuario aún no ha ingresado previamente las coordenadas de sus ubicaciones frecuentes.
        ErrorMessage(msg_error_not_coordinates)
        exit()
    else:
        print_favorite_wifi_zones(list_coordinates) # Mostrar en pantalla al usuario las tres coordenadas que más frecuenta

def print_favorite_wifi_zones(list_coordinates):
    lista = list(list_coordinates)
    print(f"Las coordenadas guardadas actualmente son: ")
    for i in range(0, len(lista)):
        print(f"coordenada [latitud,longitud] {i + 1} : {[lista[i][0]]} {[lista[i][1]]}")
    
    option = int(input("Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión: "))
    if option == 1 or option == 2 or option == 3:
        global current_location
        current_location = list_distance[option - 1]
        prepare_data(option, list_coordinates, pre_coordinates)
    else:
        ErrorMessage(msg_error_ubicacion)
        exit()

def prepare_data(optwifizone, list_coordinates, predefined_coordinates): # Obtener valores para pasarlo al calculo de la distancia, usando la formula
    lista = list(list_coordinates)
    lista_predefined = list(predefined_coordinates)    
    latitud1 = lista[optwifizone-1][0]
    longitud1 = lista[optwifizone-1][1]        
    latitud1 = convert_2_radians(latitud1) # Convertimos a radianes la latitud
    longitud1 = convert_2_radians(longitud1) # Convertimos a radianes la longitud 

    for i in range(0, len(lista_predefined)):
        for j in range(0,2):
            lista_predefined[i][j] = convert_2_radians(lista_predefined[i][j])

    calculate_distance(latitud1, longitud1, lista_predefined)

def convert_2_radians(param1): # Función que convierte a radianes
    return radians(param1)

def calculate_distance(lat1, lon1, list_converted_2_radians):  
    
    for i in range(0, 4):
        lat2 = list_converted_2_radians[i][0]
        lon2 = list_converted_2_radians[i][1]
        delta_latitude = lat2 - lat1
        delta_longitud = lon2 - lon1
        res = sin(delta_longitud/2)**2
        res = res * (cos(lat1) * cos(lat2))
        res = (sin(delta_latitude/2)**2) + res
        res = sqrt(res)
        res = asin(res)
        res = (2 * radio) * res
        res = res * 1000 # Convertir a metros
        res = round(res)
        list_distance.append(res)
    # llamar  a la función sort_distances() para mostrar al usuario en pantalla los dos valores más cercanos a su ubicación, 
    # las cuales deberán estar ordenados según la cantidad de usuarios promedio conectados, de menor a mayor
    sort_distances(list_distance)

def sort_distances(distances):
    duplicate_distances = list(distances)
    min1 = duplicate_distances.index(min(duplicate_distances))
    duplicate_distances.pop(min1)
    min2 = distances.index(min(duplicate_distances))
    print_distances(min1, min2, pre_coordinates, distances)

def print_distances(minimo1, minimo2, pre_coordinates_db, list_distance):
    for i in range (0, 4):
        pre_coordinates_db[i][0] = degrees(pre_coordinates_db[i][0])
        pre_coordinates_db[i][0] = degrees(pre_coordinates_db[i][1])    
    print(f"Zonas wifi cercanas con menos usuarios")

    # Para comparar por numero de personas conectadas
    for j in range (0,len(pre_coordinates_db)):
        if pre_coordinates_db[minimo1][0]==pre_coordinates_db[j][0] and pre_coordinates_db[minimo1][1] == pre_coordinates_db[j][1]:
            if pre_coordinates_db[j][2]>pre_coordinates_db[minimo1][2]:
                minimo1=pre_coordinates_db.index(pre_coordinates_db[j])    

    global distancia_tiempo

    if  pre_coordinates_db[minimo1][2] < pre_coordinates_db[minimo2][2]:
        print(f"La zona wifi 1: ubicada en ['{pre_coordinates_db[minimo1][0]}', '{pre_coordinates_db[minimo1][1]}'] a {list_distance[minimo1]} metros, tiene en promedio {pre_coordinates_db[minimo1][2]} usuarios")
        print(f"La zona wifi 2: ubicada en ['{pre_coordinates_db[minimo2][0]}', '{pre_coordinates_db[minimo2][1]}'] a {list_distance[minimo2]} metros, tiene en promedio {pre_coordinates_db[minimo2][2]} usuarios")
        optdestino = int(input("Elija 1 o 2 para recibir indicaciones de llegada: "))
        
        if optdestino==1: #comparamos si es la opción 1 o 2 y mostramos error en caso de que no exista.
            distancia_tiempo = list_distance[minimo1]
            give_instructions(current_location,pre_coordinates_db[minimo1])
        elif optdestino==2:
            distancia_tiempo = list_distance[minimo2]
            give_instructions(current_location,pre_coordinates_db[minimo2])
        else:
            ErrorMessage(msg_error_wifi)
            exit()

    else:
        print(f"La zona wifi 1: ubicada en ['{pre_coordinates_db[minimo2][0]}', '{pre_coordinates_db[minimo2][1]}'] a {list_distance[minimo2]} metros, tiene en promedio {pre_coordinates_db[minimo2][2]} usuarios")
        print(f"La zona wifi 2: ubicada en ['{pre_coordinates_db[minimo1][0]}', '{pre_coordinates_db[minimo1][1]}'] a {list_distance[minimo1]} metros, tiene en promedio {pre_coordinates_db[minimo1][2]} usuarios")
        optdestino = int(input("Elija 1 o 2 para recibir indicaciones de llegada: "))

        if optdestino==1:
            distancia_tiempo = list_distance[minimo2]
            give_instructions(current_location,pre_coordinates_db[minimo2])
        elif optdestino==2:
            distancia_tiempo = list_distance[minimo1]
            give_instructions(current_location,pre_coordinates_db[minimo1])
        else:
            ErrorMessage(msg_error_wifi)
            exit()

def give_instructions(location, destino):
    latlocation=location[0]
    lonlocation=location[1]
    latdestino=destino[0]
    londestino=destino[1]

    if latlocation > latdestino:
        txt1="el sur"
    elif latlocation < latdestino:
        txt1="el norte"
    #si es igual no ponemos nada
    else:
        txt1=""
        
    #hacemos lo mismo para la longitud    
    if lonlocation > londestino:
        txt2="el occidente"
    elif lonlocation < londestino:
        txt2="el oriente"
    else:
        txt2=""

    #Si el texto uno es igual a nada, y el texto 2 tiene algo, mostramos solo el texto 2
    if txt1=="" and txt2!="": 
        print(f"Debe ir hacia {txt2}")
    #Si el texto uno es igual a algo, y el texto 2 no tiene nada, mostramos solo el texto 1
    elif txt2=="" and txt1!="": 
        print(f"Debe ir hacia {txt1}")
    #Si ambos textos son iguales; mostramos que ya está en el destino
    elif txt1=="" and txt2=="":
        print("Usted ya está en el destino")
        
    #Si no se cumple ninguna, mostramos un mensaje con el texto 1 y el texto 2
    else:
        print(f"Para llegar a la zona wifi dirigirse primero {txt1} y luego hacia {txt2}")

    #llamamos una nueva función para calcular el tiempo de recorrido.
    CalcularTiempoRecorrido()      
    

def CalcularTiempoRecorrido():
    tiempo1="segundos" #creamos una variable para la unidad de tiempo de cada vehículo
    tiempo2="segundos"
    
    if distancia_tiempo==0: #Si la distancia es 0 no hacemos nada
        pass
        
    else:
        pie=distancia_tiempo/0.483 #en caso contrario calculamos el tiempo que se demorará el recorrido
        bici=distancia_tiempo/3.33
        
        if pie > 60: #en caso de ser más de 60 segundos convertimos a minutos 
            pie = pie / 60
            tiempo1="minutos"
        
        
        if bici > 60:
            bici = bici / 60
            tiempo2="minutos"
        
        moto=round(bici,2) #hacemos un redondeo a 2 cifras
        pie=round(pie,2)
        
        #concatenamos el texto y finalmente hacemos un sleep para que se pueda leer el mensaje.
        print(f"El tiempo promedio que puede tardar en llegar al punto a pie es {pie} {tiempo1} y {bici} {tiempo2} en bicicleta")
        time.sleep(5)

#endregion Funciones

print(msgBienvenido) # Mensaje de bienvendida
userName = input("Nombre de usuario: ")
if validatedata(name, userName):
    userPass = input("Contraseña: ")
    if validatedata(stored_passw, userPass):
        valorCaptcha = int(input(f"Valor Captcha: {captcha} + {calDigito}: "))
        if validatedata(captcha, valorCaptcha):        
            os.system("cls")
            print(msgOk)
            time.sleep(2)
            while countErrors < 3:
                list_distance = []
                os.system("cls")
                PrintMenuList() # Visualizar menu de opciones         
                selectOpt = int(input("Elija una opción: "))
                if selectOpt > 0 and selectOpt < 8:
                    selectOptList = optMenuList[selectOpt-1]
                    if selectOptList == iMenu01:
                        # RF01
                        stored_passw = changepassword(stored_passw)                        
                    elif selectOptList == iMenu02:
                        # RF02
                        if coordinates == []:
                            coordinates = addcoordinates(coordinates)                             
                        else:
                            # RF03
                            # Llamar a la función imprimir coordenadas (printcoordinates)
                            printcoordinates(coordinates)
                    elif selectOptList == iMenu03:
                        favorite_wifi_zones(list_distance)                        
                    elif selectOptList == iMenu04:
                        print(f"Usted ha elegido la opción {selectOpt}")
                        exit()
                    elif selectOptList == iMenu05:
                        print(f"Usted ha elegido la opción {selectOpt}")
                        exit()
                    elif selectOptList == iMenu06:
                        newFavOpt = int(input("Seleccione opción favorita: "))
                        if newFavOpt == 1 or newFavOpt == 2 or newFavOpt == 3 or newFavOpt == 4 or newFavOpt == 5:
                            # Doble check for user
                            check1 = int(input("Para confirmar por favor responda: Si me giras pierdo tres unidades por eso debes colocarme siempre de pie, la respuesta es: "))
                            if check1 == 0:
                                check2 = int(input("Para confirmar por favor responda: Me separaron de mi hermano siamés, antes era un ocho y ahora soy un… la respuesta es: "))
                                if check2 == 8:
                                    ReorderMenuList(newFavOpt) # Reordenar lista con la opcion eegida como favorita                                   
                                else:
                                    ErrorMessage(msgError)                                    
                            else:
                                ErrorMessage(msgError)                                
                        else:
                            ErrorMessage(msgError)
                            exit()                                           
                    elif selectOptList == iMenu07:
                        ErrorMessage("Hasta pronto")
                        exit()                    
                else:
                    countErrors += 1 # Incremento el contador
                    ErrorMessage(msgError)
                    continue                
        else:
            ErrorMessage(msgError) 
    else:
        ErrorMessage(msgError) 
else:
    ErrorMessage(msgError)

