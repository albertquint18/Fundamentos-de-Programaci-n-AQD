import time
#este import es para poder hacer la pantalla de carga
import pdb
#este import es para la depuración del codigo
import os
#este import es para ver si un archivo ya existe o no y en caso de que si, no se sobre escriba
import threading
#Este import es para poder hacer diferentes tareas al mismo tiempo
def nom_usuario():
    while True:
        persona = input("Ingresa tu nombre: ").strip() #.strip es para que en caso de que el usuario meta su nombre con un espacio, este se elimine
        if persona != "":
            return persona
        else:
            print("Error, debes ingresar un nombre")
        #esta funcion hace que si el dato que la persona ingresa es diferente a nada, regrese el nombre, si no que mande un error
def pedir_semestre():
    while True:
        try:
            semestre = int(input("Ingresa tu semestre: "))
            if semestre >= 1 and semestre <= 8:
                return semestre
            else:
                print("Error: el semestre debe estar entre 1 y 8")
        except ValueError:
            print("Error: debes ingresar un número entero")
#aquí para pedir el semstre metemos el while para que se repita hasta que de un valor correcto, entonces el try pide un número entero y en caso de meter un valor incorrecto da un value error
def fecha():
    while True:
        fecha = input("Ingresa la fecha (dia/mes/año): ")
        partes = fecha.split("/") #esto sirve para que al meter la fecha separe los datos cuando encuntra un /
        if len(partes) == 3:#este len mide que los datos ingresados si sean 3, osea en caso de meter 29/20 no dejara pues la longitud es de 2 y no de 3
            try:
                dia = int(partes[0])
                mes = int(partes[1])
                amo = int(partes[2])
                #ahora aquí es donde se estan guardando los datos de las fechas, con el split se separan los datos en 3 y se almacenan aquí
                if mes < 1 or mes > 12:
                    print("Error: el mes debe estar entre 1 y 12.")
                    continue
                #esta parte es para evitar que se metan fechas correctamente incorrectas osea como 30/02/26, aquí es para meses con 31 días
                if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                    dias_mes = 31
                #esta parte es para meses de 30 días
                elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                    dias_mes = 30
                #y esta para el mes de febrero
                else:
                    dias_mes = 28
                if dia >= 1 and dia <= dias_mes:
                    Fecha = dia, mes, amo
                    return Fecha
                else:
                    print("Error, el día no es válido para ese mes")
            except ValueError:
                print("Error, debes escribir números en la fecha")
        else:
            print("Error, utiliza el formato dia/mes/año")
def pedir_opcion(minimo, maximo):
    while True:
        try:
            opcion = int(input("Selecciona una opción: "))
            if minimo <= opcion <= maximo:
                return opcion
            else:
                print("Error, selecciona una opción válida")
        except ValueError:
            print("Error, debes ingresar un número")
            #Esta función esta para que a la hora en que el usuario eliga en el menú la opción, no introduzca valores erroneos fuera de 1, 2, 3, 4 o 5
#Lo anterior fue para ingresar los datos de usuario, semestre, fecha y para la elección el menú, lo siguiente es para la pantalla de carga
def pantalla_carga():
    print("\nIniciando sistema...")
    for i in range(3):
        print("Cargando" + "." * (i + 1))
        #esto es para que en la pantalla de carga los puntos vayan aumenatdo, por eso se multiplican por el resultado de i+1
        time.sleep(1)
        #esto es para que el programa espere 1 segundo para imprimir cada cargando, esto con el fin de que no suelte de golpe las 3 lineas
    print("Sistema listo.\n")
#La siguiente parte es para crear los archivos principales
def crear_archivos():
    archivos = {
        "balones_futbol.txt":
            "BALONES DE FÚTBOL\n\nEstado: Disponible\n",

        "balones_basquetbol.txt":
            "BALONES DE BÁSQUETBOL\n\nEstado: Disponible\n",

        "balones_voleibol.txt":
            "BALONES DE VÓLEIBOL\n\nEstado: Disponible\n",

        "ubicacion_balones.txt":
            "UBICACIÓN DE ENTREGA\n\nLugar: Gimnasio\n"
    }
    #esto es un diccionario de los archivos para ver el estado de los balones, poniendo el nombre del archivo y su estado
    for nombre, contenido in archivos.items(): #esto es para poder recorrer el diccionario, el items es para tener el valor y la clave a la vez
        if not os.path.exists(nombre):#aquí es para que si el archivo ya existe, si no existe lo crea
            try:
                with open(nombre, "w") as archivo:
                    archivo.write(contenido)#aquí se escribe en el archivo lo que se tenía guardado en el diccionario
            except PermissionError:
                print("Error, no se tienen permisos para crear los archivos")#esto es para que en caso de que se quiera crear un archivo pero no se tengan los permisos, no se deje
#Ahora esta parte es la funcion para mostrar los balones
def mostrar_balones():
    print("\n========== BALONES ==========")
    archivos = [
        "balones_futbol.txt",
        "balones_basquetbol.txt",
        "balones_voleibol.txt"
    ]#aquí se hizo una lista con los archivos que tienen la información de los de los balones
    for archivo in archivos:#en esta parte se va recorriendo los archivos, tomando uno a la vez
        try:#esto es para intentar abrir el archivo
            with open(archivo, "r") as documento:#abre el archivo, que son los tipos de balones
                contenido = documento.read()#lee lo que hay en el documento
            print("\n" + contenido)#imprime el contenido, que es lo que se leyo del documento
        except FileNotFoundError:
            print("Error, no se encontró", archivo) #en caso de no encontrarse ese archivo
        except PermissionError:
            print("Error, no hay permisos para leer", archivo)#en caso de que no se tengan perimos para leer
#ahora la función sera para pedir el balón:
def prestar_balon():
    print("\n========== PRESTAR BALÓN ==========")
    balones = [
        ["1", "Fútbol", "balones_futbol.txt"],
        ["2", "Básquetbol", "balones_basquetbol.txt"],
        ["3", "Vóleibol", "balones_voleibol.txt"]
    ]#una lista para los balones
    for balon in balones:
        print(balon[0] + ". " + balon[1])
    opcion = pedir_opcion(1, 3)
    archivo_nombre = balones[opcion - 1][2]#con esta parte se busca el nombre del archivo seleccionado
    tipo_balon = balones[opcion - 1][1]
#ver si el balon está disponible
    try:
        with open(archivo_nombre, "r") as archivo:
            contenido = archivo.read()
        if "Estado: Prestado" in contenido:
            print("\nEse balón ya está prestado.")
            print("No se puede realizar otro préstamo.")
            return
    except FileNotFoundError:
        print("Error: no se encontró el archivo.")
        return
    except PermissionError:
        print("Error: no tienes permisos para acceder al archivo.")
        return
#ahora se van a ver los datos del alumno
    print("\nDatos del préstamo")
    nombre = nom_usuario()
    semestre = pedir_semestre()
    Fecha = fecha()
#para ver los datos de donde se esta entregando el balón
    print("\nLugar donde se entregan los balones:")
    print("1. Gimnasio")
    print("2. Oficina de preparatoria")
    print("3. Oficina de Coordinación VIVE")
    lugar_opcion = pedir_opcion(1, 3)
    lugares = [
        "Gimnasio",
        "Oficina de preparatoria",
        "Oficina de Coordinación VIVE"
    ]
    lugar = lugares[lugar_opcion - 1]
#para guardar la información
    try:
        with open(archivo_nombre, "w") as archivo:#abre el archivo que eligio el usuario como balones_furbol.txt, todo esto para escribir el nuevo estado del balon, remplazando la información que ya tenía
            archivo.write("BALÓN DE " + tipo_balon.upper() + "\n")
            archivo.write("Estado: Prestado\n")
            archivo.write("Alumno: " + nombre + "\n")
            archivo.write("Semestre: " + str(semestre) + "\n")
            archivo.write(
                "Fecha: "
                + str(Fecha[0]) + "/"
                + str(Fecha[1]) + "/"
                + str(Fecha[2]) + "\n"
            )#aqui captura la fecha que introdujimos primeramente
            archivo.write("Lugar de entrega: " + lugar + "\n")
        print("\nPréstamo registrado correctamente")
    except PermissionError:
        print("Error, no se tienen permisos para modificar el archivo")
#Lo siguiente es la parte que va a registrar cuando un balón se dvuelva 
def devolver_balon():
    print("\n========== DEVOLVER BALÓN ==========")
    balones = [
        ["1", "Fútbol", "balones_futbol.txt"],
        ["2", "Básquetbol", "balones_basquetbol.txt"],
        ["3", "Vóleibol", "balones_voleibol.txt"]
    ]#auí se hizo otra lista como la de pedir balones
    for balon in balones:
        print(balon[0] + ". " + balon[1])#este for recorre y muestra las 3 opciones de balones
    opcion = pedir_opcion(1, 3)
    archivo_nombre = balones[opcion - 1][2]
    try:
        with open(archivo_nombre, "r") as archivo:
            contenido = archivo.read()#abre el archivo, revisa su estado y si esta diponible muestra que ya lo está
        if "Estado: Disponible" in contenido:
            print("Ese balón ya está disponible.")
            return
    #aca registra la devolución
        Fecha = fecha()#llamndo de nuevo a la fecha
        with open(archivo_nombre, "w") as archivo:#abre el archivo y guarda la información de devolución
            archivo.write(
                "\nDEVOLUCIÓN\n"
            )
            archivo.write("Estado: Disponible\n")
            archivo.write(
                "Fecha de devolución: "
                + str(Fecha[0]) + "/"
                + str(Fecha[1]) + "/"
                + str(Fecha[2]) + "\n"
            )
        print("\nDevolución registrada correctamente")
    except FileNotFoundError:
        print("Error, el archivo no existe")
    except PermissionError:
        print("Error, no tienes permisos para modificar el archivo")
#Esta parte va a ser para poder consultar la información de los archivos
def consultar_archivo():
    archivos = [
        "balones_futbol.txt",
        "balones_basquetbol.txt",
        "balones_voleibol.txt",
        "ubicacion_balones.txt"
    ]#se vulve a hacer una lista para los archivos
    print("\n========== ARCHIVOS DISPONIBLES ==========")
    for i in range(len(archivos)):#esta parte es para poder ver los archivos
        print(str(i + 1) + ". " + archivos[i])
    opcion = pedir_opcion(1, len(archivos))
    nombre_archivo = archivos[opcion - 1]
    while True:#esta parte es para poder abrir el archivo y en caso de que no exista se repita hasta que si
        try:
            with open(nombre_archivo, "r") as archivo:
                contenido = archivo.read()
            print("\n========== CONTENIDO ==========")
            print(contenido)#muestra el contenido del archivo
            break
        except FileNotFoundError:
            print("Error: el archivo no existe.")
            print("Selecciona otro archivo.")
            opcion = pedir_opcion(1, len(archivos))
            nombre_archivo = archivos[opcion - 1]
        except PermissionError:
            print("Error: no tienes permisos para abrir este archivo.")
            break
#Lo siguiente es el timmer de 10 minutos de inactividad
def cont_temp(detener):
    for i in range(600):
        if detener.is_set():
            return
        time.sleep(1)

    print("\nHan pasado 10 segundos de inactividad.")
#Esta parte es la que defince la función que invoca al menú
def mostrar_menu():
    menu = [
        ["1", "Mostrar balones"],
        ["2", "Prestar balón"],
        ["3", "Devolver balón"],
        ["4", "Consultar archivos"],
        ["5", "Salir"]
    ]
    print("\n========== MENÚ PRINCIPAL ==========")
    for opcion in menu:
        print(opcion[0] + ". " + opcion[1])
    print("====================================")
#Y esto ya es el programa, el cual invoca las opciones mediante las funciones definidas
print("==============================================")
print(" ADMINISTRACIÓN Y USO DE BALONES TECMILENIO")
print("==============================================")
usuario = nom_usuario()
print("\nBienvenido/a, " + usuario + ".")
print("Sistema de administración de balones deportivos.")
pantalla_carga()
crear_archivos()
while True:
    mostrar_menu()
    detener = threading.Event()#es una especie de señal para decir al temporizador que se detenga
    hilo = threading.Thread(target=cont_temp, args=(detener,))#Esta parte hace que el temporizador pueda ejeciutarse aparte del menu, ejecutando el contador
    hilo.start()
    opcion = pedir_opcion(1, 5)
    detener.set()
    hilo.join()
    if opcion == 1:
        mostrar_balones()
    elif opcion == 2:
        prestar_balon()
    elif opcion == 3:
        devolver_balon()
    elif opcion == 4:
        consultar_archivo()
    elif opcion == 5:
        print("\nGracias por utilizar el sistema, " + usuario + ".")
        break
   