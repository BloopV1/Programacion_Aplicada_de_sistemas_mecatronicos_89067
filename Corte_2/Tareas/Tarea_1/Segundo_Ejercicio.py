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
    return print(f"el logaritmo natural de la funcion{n} = {num_result}")

def exponencial(n):
    print("la funcion exponencial calculadad de",n)
    num_result=math.exp(n)
    return print(f"la funcion exponencial de{n} = {num_result}")
