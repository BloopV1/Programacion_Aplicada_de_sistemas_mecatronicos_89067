from math import sqrt 

n = int(input("Escriba un número: "))
def fibonacci(n):
    if n < 2:
        return n
    else:
        u = ((1+sqrt(n))/2)
        j = ((u**n-(1-u)**n)/sqrt(n))
        return round(j)
print(fibonacci)
