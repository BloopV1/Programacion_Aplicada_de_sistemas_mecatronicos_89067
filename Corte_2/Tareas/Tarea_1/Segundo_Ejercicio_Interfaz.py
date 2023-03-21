#Realice un programa donde se cree una función que permita calcular el seno, cose, tangente, exponencial y logaritmo natural. 
#El usurio deberá ingresar como entrada el valor y la función a aplicar, mostrando por pantalla el valor ingresado seguido del resultado de la función matemática implementada.
#Interfaz de usuario

import Segundo_Ejercicio as eje
print("_____________________________________________________________________________")
print("|      hola usuari@ dentro de lo que nesecitas que operaciones vas a tomar  |")
print("|                   ----(1)seno de un angulo                                |")                      
print("|                   ----(2)coseno de un angulo                              |")
print("|                   ----(3)tangente de un angulo                            |")
print("|                   ----(4)exponencial                                      |")
print("|                   ----(5)logaritmo natural                                |")
print("|___________________________________________________________________________|")

eleccion= int(input("¿Cual vas a escoger? "))
if eleccion==1:
    n=float(input("ingrese el valor "))
    result=eje.seno(n)
if eleccion==2:
    n=float(input("ingrese el valor "))
    result=eje.cos(n)
if eleccion==3:
    n=float(input("ingrese el valor "))
    result=eje.tangente(n)
if eleccion==4:
    n=float(input("ingrese el valor "))
    result=eje.exponencial(n)
if eleccion==5:
    n=float(input("ingrese el valor "))
    result=eje.logaritmo(n)
