#Realizar un ejercicio donde se calcule el IMC de las siguientes 4 personas, cuyos valores se ven en la tabla.
#El sistema debe mostrar según el valor de IMC obtenido para cada uno de las personas indicando su correspondiente escala. 

# NOMBRE ESTATURA(cm) PESO(kg)
# Pedro     188         97
# Maria     160         47
# Julian    158         58
#Jessica    170         73

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

personas = [ #Tupla de personas
    {"nombre": "Pedro", "peso": 97, "altura": 1.88},
    {"nombre": "María", "peso": 47, "altura": 1.60},
    {"nombre": "Julian", "peso": 58, "altura": 1.58},
    {"nombre": "Jessica", "peso": 73, "altura": 1.73}]

for persona in personas: #calcular el IMC de cada persona
    imc = calcular_imc(persona["peso"], persona["altura"])
    # Porcentaje de IMC
    if imc < 18.5:
        print("Bajo peso")
    elif imc < 25:
        print("Peso normal")
    elif imc < 30:
        print("Sobrepeso")
    else:
        print("Obesidad")

    print(f"{persona['nombre']}: IMC = {imc:.2f}")