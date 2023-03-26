#Realice una función recursiva que calcule el factorial o el número de fibonacci (dependiendo del ejercicio que le salió en el parcial).

def fibonacci(n): #Esta función toma un argumento, n, que representa el número de Fibonacci para calcular. 
    if n <= 1: #Si n es menor o igual a 1, la función simplemente devuelve n.
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) # Si n es mayor que 1, la función se llama a sí misma dos veces con n-1 y n-2 como argumentos y luego suma los resultados para obtener el número de Fibonacci deseado.
print(fibonacci(10))
