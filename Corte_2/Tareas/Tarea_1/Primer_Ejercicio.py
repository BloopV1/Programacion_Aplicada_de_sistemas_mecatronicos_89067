# Realice un función llamada Aleatorio() donde se retorne un número entre 100 y 120, excepto los números 110, 115 y 119.
# Al final se deben imprimir 10 números retornados de la función Aleatorio(), alternando el orden par, impar (Comenzando con número par).
from random import randint

def Aleatorio(n=10):
    num = []
    while len(num) < n:
        Alea = randint(100, 120)

    if (Alea != 110) and (Alea != 115) and (Alea != 119):
        if (len(num) % 2) == 0 and (Alea % 2 == 0):
            num.append(Alea)

    elif (len(num) % 2) == 1 and (Alea % 2 == 1):
        num.append(Alea)
    return num

num = Aleatorio()
print(num)
