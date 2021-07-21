
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

import time
import os

#region Variables Globales
msgBienvenido = "Bienvenido al sistema de ubicación para zonas públicas WIFI"
msgError = "Error"
msgOk = "Sesión iniciada"
msg_error_coordinate = "Error coordenada"
msg_error_update = "Error actualización"
name = "52208"
stored_passw = "80225"
calDigito = ((8 // 2) + 8)  - (2 ** 2 + (5 * 2) - 2)
captcha = 208
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
tmp_coordinates = [[None, None], 
                [None, None], 
                [None, None]]

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
                        print(f"Usted ha elegido la opción {selectOpt}")
                        exit()
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
