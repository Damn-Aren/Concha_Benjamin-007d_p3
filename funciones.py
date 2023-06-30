#{====================================RUTS========================================================}
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
#{===================================NOMBRES======================================================}
def vali_nombres():
    while True:
        nombre = input("\nIngrese su nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha:
            return nombre
        else:
            print("Nombre mal ingresado, reintente con 3 letras o más")
#{===================================CORREOS======================================================}
def vali_correos():
    while True:
        correo = input("\nIngrese su correo: ")
        if "@" in correo:
            return correo
        else:
            print("El formato de correo no es valido")
#{===================================OPCIONES=====================================================}
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
            os.system('cls')
#{====================================EDAD========================================================}
def vali_edad():
    while True:
        try:
            edad = int(input("\nIngrese su Edad: "))
            if edad >= 5 and edad <= 120:
                return edad
            else:
                print("Usted no puede manejar este programa")
        except:
            print ("???")
#{===================================CANTIDAD=====================================================}
def validar_cantidad(algo):
    while True:
        try:
            cantidad = int(input(f"\tIngrese la cantidad de {algo}: "))
            if cantidad >= 0:
                return cantidad
            else:
                print ("\nLa cantidad debe ser positiva")
        except:
            print("Debe ingresar una cantidad valida")
#{================================================================================================}
