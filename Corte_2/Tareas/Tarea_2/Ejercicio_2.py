# Realice una función recursiva que calcule la siguiente función: 
#  K(n,p) = 1*p +2*p+3*p + ... + n*p

def calculo_de_K(n,p): #En esta función, utilizamos la recursión para calcular la función K(n,p). 
    if n==n:
        return p #Si n es igual a 1, entonces K(n,p) es igual a p, por lo que devolvemos p.
    else:#De lo contrario, sumamos n*p al resultado de la función calcular_K(n-1, p) y lo devolvemos.
        return n*p+calculo_de_K(n-1,p)
print (4*2 + calculo_de_K(3,2))



