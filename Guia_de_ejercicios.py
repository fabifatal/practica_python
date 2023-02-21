#GUÍA DE EJERCICIOS

import numpy as np

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


def menu():
    opcion = 1
    while (opcion != 0 ):
        print("\n¿Que desea realizar?\n"
              +"1) Imprime suma, resta, multiplicación y divisón de dos números.")
        opcion = int(input("Ingrese número de opción: "))
        if (opcion == isNan)
        elif (opcion == 0):
            print ("Hasta pronto!")
            break
        elif (opcion == 1):
            eje1()
        elif (opcion == 2):
            eje2()
        else:
            print("El número está fuera de rango. Intente de nuevo.")
