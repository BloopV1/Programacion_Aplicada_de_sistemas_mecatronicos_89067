# Realice una función recursiva que calcule la siguiente función: 
#  K(n,p) = 1*p +2*p+3*p + ... + n*p

def calculo_de_K(n,p):
    if n==n:
        return p
    else:
        return n*p+calculo_de_K(n-1,p)
print (4*2 + calculo_de_K(3,2))