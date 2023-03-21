#Realice un función llamada Aleatorio() donde se retorne un número entre 100 y 120, excepto los números 110, 115 y 119. 
#Al final se deben imprimir 10 números retornados de la función Aleatorio(), alternando el orden par, impar (Comenzando con número par).
from random import randint

def Aleatorio(n=10):
    num=[]
    while len(num)<n:
        a=randint(100, 120)
        if (a!= 110) and (a!=115) and (a!=119):
           if (len(num)%2)==0 and (a%2==0):
             num.append(a)
    
        elif (len(num)%2)==1 and (a%2==1):
            num.append(a)
    return num

num=Aleatorio()
print(num)
