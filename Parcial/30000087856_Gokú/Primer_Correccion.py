n = int(input("Ingrese un numero"))
while n!=0:
    x = (n//10)
    dig=n-(x*10)
    n=x 
    if dig ==5:
        print ("salto")
    else :
        print(dig)
