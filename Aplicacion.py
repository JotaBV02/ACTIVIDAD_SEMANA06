# ACTIVIDAD - SEMANA 06
# Jorge ALberto Bravo Veintemilla

import Gestion_archivos

def menu():
    print("*** MENU PRINCIPAL ***")
    print("1. Crear Archivo")
    print("2. Eliminar Archivo")
    print("3. Agregar Contenido")
    print("4. Mostrar contenido del archivo")
    print("5. Salir")

def crear():
    print("-- Crear Archivo --")
    archivo = input("Archivo: ")
    contenido = input("Contenido: ")
    Gestion_archivos.crear_archivo(archivo, contenido)

def eliminar():    
    print("-- Eliminar Archivo")
    archivo = input("Archivo: ")
    Gestion_archivos.eliminar_archivo(archivo)

def agregar():
    print("-- Agregar Datos a un Archivo --")
    archivo = input("Archivo: ")
    contenido = input("Contenido: ")
    Gestion_archivos.agregar_contenido_archivo(archivo, contenido)
    
def listar():
    print("-- Mostrar contenido de un archivo -- ")
    archivo = input("Archivo: ")
    print(Gestion_archivos.leer_archivo(archivo))

def salir():
    print("Gracias por su visita....")

def error():
    print("Opción incorrecta")

opcion = 1
while opcion!=5:
    menu()
    opcion = int(input("Opcion: "))
    if opcion == 1:
        crear()
    elif opcion == 2:
        eliminar()
    elif opcion == 3:
        agregar()
    elif opcion == 4:
        listar()
    elif opcion == 5:
        salir()
    else:
        error()


