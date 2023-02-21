#GUÍA DE EJERCICIOS

import math as math

#1. Escriba un programa que solicite a un usuario dos números por teclado y calcule su suma, resta, producto y división.

def eje1():
    print("     EJERCICIO 1     ")
    num1 = int(input("Ingresa un número: "))
    num2 = int(input("Ingresa segundo número: "))
    print ("La suma es "+str(num1+num2))
    print ("La resta es "+str(num1-num2))
    print ("La multiplicación es "+str(num1*num2))
    print ("La resta es "+str(num1*num2))    

#2. Escriba un programa que permita calcular el área de un rectángulo. ¿Cómo modificaría su programa 
# para que ahora calcule el área de un cuadrado de igual medida al ancho del rectángulo anterior?

def eje2():
    print("     EJERCICIO 2    ")
    ancho = int(input("Ingrese el ancho del rectángulo: "))
    largo = int(input("Ingrese el largo del rectángulo: "))
    print ("El área del rectángulo es "+str(ancho*largo))
    print ("Tomando el ancho del rectángulo como lado para un cuadrado su area sería "+str(ancho*ancho))

#3. Escriba un programa que, dada una cantidad de dinero en pesos chilenos ingresada por teclado, calcule la cantidad de dólares que se pueden comprar

def eje3() :
    print("     EJERCICIO 3    ")
    pesosChile = int(input("Ingrese los pesos chilenos que desea convertir a dolares: "))
    dolares = pesosChile/802,29
    print ("El valor ingresado corresponde a "+str(dolares)+" en dolares.")

#4. Escriba un algoritmo que permita calcular la edad de una persona según su año de nacimiento.
def eje4():
    print("     EJERCICIO 4    ")
    anoNacimiento = int(input("Ingresa tu año de nacimiento: "))
    anoActual = int(input("Ingrese el año actual: "))
    print("Tu edad es "+str(anoActual-anoNacimiento))


print("HH  HH    OOOOOO     JJ   AAAAAA           DDDDD   EEEEE   \n"
    + "HH  HH    OO  OO     JJ   AA  AA           DD  DD  EE     \n"
    + "HHHHHH    OO  OO     JJ   AAAAAA           DD   DD EEEEE  \n"
    + "HH  HH    OO  OO  JJ JJ   AA  AA           DD  DD  EE   \n"
    + "HH  HH    OOOOOO  JJJJJ   AA  AA           DDDDD   EEEEE \n"
   +"\nEEEE     JJ  EEEE   RRR   CCCC  II  CCCC  II  OOO  SSSS\n"
    + "E        JJ  E      R  R  C     II  C     II  O O  S   \n"
    + "EEE      JJ  EEE    RRR   C     II  C     II  O O  SSSS\n"
    + "E     JJ JJ  E      R R   C     II  C     II  O O     S\n"
    + "EEEE  JJJJJ  EEEE   R  R  CCCC  II  CCCC  II  OOO  SSSS\n")

def opcionBinaria (function, pregunta):
    opt = "y"
    while (opt != "n"):
        function
        while (opt != "n" or opt != "s"):
            opt=input(pregunta+" s = Si ; n = No: ")
            if opt == "s": break
            elif opt== "n": break
            else: print("Entrada no válida. Intente de nuevo.")     

        
        
        
def menu():
    opcion = 1
    while (opcion != 0 ):
        print("\n¿Que desea realizar?\n"
              +"1) Imprime suma, resta, multiplicación y divisón de dos números.\n"
              +"2) Calcula rectángulo y cuadrado.\n"
              +"3) Calcula CLP a Dolares.\n"
              +"4) Calcula edad.\n"
              +"SALIR ingrese un cero (0).\n"
              )
              
        opcion = int(input("Ingrese número de opción: "))
        if (math.isnan(opcion)):
            print("Debe ingresar un número. Intente de nuevo.")
        elif (opcion == 0):
            print ("Hasta pronto!")
            break
        elif (opcion == 1): opcionBinaria(eje1(),"¿Desea realizar de nuevo el ejercicio?")
        elif (opcion == 2): opcionBinaria(eje2(),"¿Desea realizar de nuevo el ejercicio?")
        elif (opcion == 3): opcionBinaria(eje3(),"¿Desea realizar de nuevo el ejercicio?")
        elif (opcion == 4): opcionBinaria(eje4(),"¿Desea realizar de nuevo el ejercicio?")
        else:
            print("El número está fuera de rango. Intente de nuevo.")
menu()