import random

# Generamos una lista de 10 números aleatorios entre 1 y 50
lista = [random.randint(1, 50) for i in range(10)]

# Definimos la función mayor para encontrar el número mayor de la lista
def mayor(lista):
    mayor_num = lista[0]
    for num in lista:
        if num > mayor_num:
            mayor_num = num
    print("El número mayor de la lista es:", mayor_num)

# Definimos la función primos para encontrar los números primos de la lista
def primos(lista):
    primos = []
    for num in lista:
        if num > 1:
            es_primo = True
            for i in range(2, num):
                if (num % i) == 0:
                    es_primo = False
                    break
            if es_primo:
                primos.append(num)
    print("Los números primos de la lista son:", primos)

# Llamamos a las funciones con la lista como parámetro
print("Lista generada:", lista)
mayor(lista)
primos(lista)
