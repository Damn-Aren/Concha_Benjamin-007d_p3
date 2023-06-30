import numpy as np
import os
import time
import msvcrt
#{==================================================}
list_ruts = []
list_nombres = []
list_mascota = []
list_filas = []
list_columnas = []
#{==================================================}
hotel_mascotas = np.zeros((2,5),int)
#{==================================================}
def vali_ruts():
    while True:
        try:
            rut = int(input("\nIngrese su Rut: "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("Rut no valido")
        except:
            print ("Formato de Rut no valido")
#{==================================================}
def vali_nombres():
    while True:
        nombre = input("\nIngrese su nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha:
            return nombre
        else:
            print("Nombre mal ingresado, reintente con 3 letras o más")
#{==================================================}
def menu_principal():
    os.system('cls')
    print("""
== Bienvenido al Hotel de Mascotas! ==
1.- Ingresar Mascota
2.- Buscar Mascota
3.- Retirarse

\n4.- Salir
""")
#{==================================================}
def vali_opcion():
    while True:
        try:
            opci = int(input("Ingrese una opción: "))
            if opci in (1,2,3):
                return opci
            else:
                print("Opcion no valida, reintente")
        except:
            print("Debe ingresar un numero de opcion")
#{==================================================}
def ver_habitaciones():
    print("  = Enseñando Habitaciones =")
    print("")
    for x in range(2): #filas
        print(f"Piso {(x+1)*1} |", end=" ")
        for y in range(5): #columnas
            if hotel_mascotas [x][y] == 0:
                print (f"{hotel_mascotas[x][y]}", end=" ")
            else:
                print (f"{hotel_mascotas[x][y]}", end=" ")
        print ()
    print("       ------------")
    print("       | 1 2 3 4 5 |")
    print("")
    print("Presione una tecla para continuar")
    msvcrt.getch()
#{==================================================}
def vali_nombres_mascotas():
    while True:
        nombre = input("\nIngrese nombre de su mascota: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha:
            return nombre
        else:
            print("Nombre mal ingresado, reintente con 3 letras o más")
#{==================================================}
def dias_aque():
    while True:
        try:
            dias = int(input("\nIngrese los Dias de estadia: "))
            if dias >= 1 and dias <= 7:
                dias = {dias * 150000}
                return dias
            else:
                print("Usted no puede reservar esa cantidad")
        except:
            print ("Ingrese el formato en numeros")
#{==================================================}
def seleccion_piso():
        while True:
            try:
                fila = int(input("Ingrese el piso a comprar: "))
                if fila in (1,2):
                    break
                else:
                    print("Piso no existente")
            except:
                print("Debe ingresar el numero del piso a comprar")
#{==================================================}
def seleccion_habitacion():
        while True:
            try:
                columna = int(input("Ingrese el departamento a comprar: "))
                if columna in (1,2,3,4,5):
                    break
                else:
                    print("Habitacion no existente")
            except:
                print("Debe ingresar el numero de habitacion a comprar")
#{==================================================}
def reserva_habitacion():
    nombre = vali_nombres()
    ruts = vali_ruts()
    mascota = vali_nombres_mascotas()
    dias = dias_aque()
    print("Habitaciones disponibles: ")
    ver_habitaciones()

    fila = seleccion_piso()
    columna = seleccion_habitacion()

    for x in range(2):
        for y in range(5):
            if hotel_mascotas [x][y] == 0:
                hotel_mascotas[x][y] = 1
                list_ruts.append(ruts)
                list_nombres.append(nombre)
                list_filas.append(x)
                list_columnas.append(y)
                print("Habitacion registrada con exito!")
                time.sleep(3)
                return
#{==================================================}