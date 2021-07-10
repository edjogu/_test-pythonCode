# MinTIC Reto 3 - Tercera parte
# Autor: guzmanE
# Date        Description
# 01.07.21    Initial version
# 02.07.21    Optimizado (Uso de funciones def)
# 07.07.21    RF01 Actualizar contraseña
# 07.07.21    RF02 Ingresar coordenadas de los tres sitios que más frecuenta (trabajo, casa, parque).

# --          --

# Sistema Login @ TicNet Corp @

# Define Variables
#

import time
import os

#region Variables Globales
msgBienvenido = "Bienvenido al sistema de ubicación para zonas públicas WIFI"
msgError = "Error"
msgOk = "Sesión iniciada"
msg_error_coordinate = "Error coordenada"
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
#endregion Funciones

# RF01:
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
                # RF01
                os.system("cls")
                PrintMenuList() # Visualizar menu de opciones         
                #region RF03
                selectOpt = int(input("Elija una opción: "))
                if selectOpt > 0 and selectOpt < 8:
                    selectOptList = optMenuList[selectOpt-1]
                    if selectOptList == iMenu01:
                        stored_passw = changepassword(stored_passw)                        
                    elif selectOptList == iMenu02:
                        print(f"Usted ha elegido la opción {selectOpt}")
                        exit()
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
                        #region RF02
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
                        #endregion RF02                      
                    #region RF05
                    elif selectOptList == iMenu07:
                        ErrorMessage("Hasta pronto")
                        exit()
                    #endregion RF05
                else:
                    countErrors += 1 # Incremento el contador
                    ErrorMessage(msgError)
                    continue
                #endregion RF03
        else:
            ErrorMessage(msgError) 
    else:
        ErrorMessage(msgError) 
else:
    ErrorMessage(msgError)