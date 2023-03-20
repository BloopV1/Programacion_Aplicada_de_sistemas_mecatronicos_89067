####################################################################################
####################### Primer Ejercicio ###########################################
####################################################################################
def digitos():
n=int(input('ingrese su numero'))
digit_equal=0
digit_different=0
while n!=0:
    x=(n//10)
    dig=n-(x*10)
    n=x
    if dig==5:
        print('salto')
        digit_equal+=1
    else:
        print(dig)
        digit_different+=1
print(f'iguales a 5 {digit_equal}')
print(f'iguales a 5 {digit_different}')
print(f'iguales a 5 {digit_equal+digit_different}')

####################################################################################
####################### segundo Ejercicio ##########################################
####################################################################################

def fibonacci():
n=int(input('ingrese la cantidad deseada'))
a=0
b=1
print(a,'\n',b)
for i in range(n-2):
    c=a+b
    a=b
    b=c
    print(c)

####################################################################################
####################### tercer Ejercicio ###########################################
####################################################################################

def primos():
num=int(input('especifique la cantidad de numeros'))
j=2; x=0; n=2
print('1')
while x <=num-2:
    div=n%j
    if div==0:
        if n==j:
            print(n, end=',')
            x+=1
        j=2
        n+=1
    else:
        j+=1

####################################################################################
####################### cuarto Ejercicio ###########################################
####################################################################################

if __name__=='__name__':
    main()

def main():
    opc=input('ingrese su eleccion')
    if opc=='1':
        .digitos()
    if opc=='2':
        .fibonacci()
    if opc=='3':
        .primos()