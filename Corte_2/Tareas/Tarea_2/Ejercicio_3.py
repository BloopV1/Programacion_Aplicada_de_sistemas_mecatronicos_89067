#Realice una función recursiva que calcule el factorial o el número de fibonacci 
#(dependiendo del ejercicio que le salió en el parcial).

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print (fibonacci)