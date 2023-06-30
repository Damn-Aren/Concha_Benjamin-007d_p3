#Prueba 3 Benjamin Concha Moreno
from Funciones_Mascotas import *

while True:
    menu_principal()
    opci = vali_opcion()
#{====================================================}
    while True:
        if opci == 1:
            print (reserva_habitacion())
            break
#{====================================================}
        elif opci == 2:
            ruts = vali_ruts()
            ver_habitaciones()
            break
#{====================================================}
        elif opci == 3:
            ruts = vali_ruts()
            break
#{====================================================}
        else:
            print("Gracias por usar este programa")
            break