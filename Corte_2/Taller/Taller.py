# Realice un programa para calcular el valor bruto de un producto alimenticio según la última reforma tributaria del IVA de la canasta familiar del año 2023.
# leer txt y crear diccionario

archivo = open("Alimentos.txt","r")
contenido = archivo.read()

Al_dic = {}  
with open("Alimentos.txt", "r") as file:
    for line in file:
        item, iva = line.strip().split(",")
        Al_dic[item] = float(iva)

while True:
    producto= input("Ingrese el nombre del producto o escriba 'salir' para salir: ") #ingrese el nombre del producto y su valor neto
    if producto == "salir":
        break
    valor_neto = float(input("Ingrese el valor neto del producto: "))
# busca el producto en el diccionario y encuentra el producto buscado
    if producto in Al_dic: 
        valor_iva = valor_neto * Al_dic[producto]
    else:
        print("El producto ingresado no se encuentra en la lista.")
        continue
    valor_base = valor_neto + valor_iva 

    #imprimir el valor base y el valor del IVA 
    print(f"El valor base del producto es: {valor_base:.2f}")
    print(f"El valor del IVA es: {valor_iva:.2f}")
archivo.close()