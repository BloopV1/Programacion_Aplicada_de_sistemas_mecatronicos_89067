# Realice un programa donde se cree una matriz de 5x10, después se imprima en pantalla la matriz creada
# indicando cuál es el número más alto y más bajo dentro de la lista, incluyendo su respectiva posición. 
# Finalmente se organice la matriz del número mayor al menor, empezando desde la posición [0,0].

import numpy as np
#crearemos una matriz de 5 columnas y 10 filas con numeros aleatorios del 1 al 100
matriz =np.random.randint(1,101,size=(5,10))
print("matriz og:")
print(matriz)
#Dentro de esta funcion con la libreria encontramos el numero con mayor posicion
maxi = matriz.max()
maxi_pos = np.unravel_index(matriz.argmax(),matriz.shape)

#Dentro de esta funcion con la libreria encontramos el numero con menor posicion
min = matriz.min()
mini_pos = np.unravel_index(matriz.argmax(),matriz.shape)

#Dentro de ambos prints en la fila 17 vamos a imprimir el numero con mayor posicion y luego en la 18 con la menor posicion
print ("el numero mas alto de la matriz es:",maxi,"dentro de la pocision",maxi_pos)
print ("el numero mas alto de la matriz es:",min,"dentro de la pocision",mini_pos)

#con esta funcion vamops a aordenar la matriz desde un mayor a un menor
matriz_ordenada=np.sort(matriz,axis=None)[::-1].reshape(matriz.shape)

#imprimimos la matriz de forma organizada 
print("la matriz ordenada desde un mayor a nu menor:")
print(matriz_ordenada)



