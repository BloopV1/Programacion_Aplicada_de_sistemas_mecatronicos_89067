#Realice un programa donde se cree una función que permita calcular el seno, cose, tangente, exponencial y logaritmo natural. 
#El usurio deberá ingresar como entrada el valor y la función a aplicar, mostrando por pantalla el valor ingresado seguido del
#resultado de la función matemática implementada.
import math 
#Funciones 
def seno(n):                                              
    print("se calcula el seno de el angulo:",n)          
    f=math.radians(n)                                    
    num_result=math.sin(f)
    return print(f"el seno de {n} = {num_result}")

def cos(n):
    print("se calcula el coseno de el angulo:",n)
    f=math.radians(n)
    num_result=math.cos(f)
    return print(f"el cos de {n} = {num_result}")

def tangente(n):
    print("se calcula la tangente de el angulo:",n)
    f=math.radians(n)
    num_result=math.tan(f)
    return print(f"la tangente de {n} = {num_result}")

def logaritmo(n):
    print("el calculo del logaritmo natural de",n)
    num_result=math.log(n)
    return print(f"el logaritmo natural de la funcion {n} = {num_result}")

def exponencial(n):
    print("la funcion exponencial calculadad de",n)
    num_result=math.exp(n)
    return print(f"la funcion exponencial de {n} = {num_result}")


# Interfaz de usuario
print("hola usuari@ dentro de lo que nesecitas que operaciones vas a tomar")
print("1:seno de un angulo")
print("2:coseno de un angulo")
print("3:tangente de un angulo")
print("4:exponencial de")
print("5:logaritmo natural de")

eleccion = int(input("¿Cual vas a escoger? "))
if eleccion == 1:
    n = float(input("ingrese el valor "))
    result = seno(n)
if eleccion == 2:
    n = float(input("ingrese el valor "))
    result = cos(n)
if eleccion == 3:
    n = float(input("ingrese el valor "))
    result = tangente(n)
if eleccion == 4:
    n = float(input("ingrese el valor "))
    result = exponencial(n)
if eleccion == 5:
    n = float(input("ingrese el valor "))
    result = logaritmo(n)
