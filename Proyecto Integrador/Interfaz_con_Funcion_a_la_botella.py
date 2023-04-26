import math

# Pedir el tamaño de la botella
altura_botella = float(input("Altura de la botella en cm: "))
diametro_botella = float(input("Diámetro de la botella en cm: "))

# Pedir el volumen de la botella
litros = int(input("Litros: "))
mililitros = int(input("Mililitros: "))

# Calcular el volumen de la botella
volumen_botella = litros + (mililitros / 1000)

# Calcular el radio de la botella
radio_botella = diametro_botella / 2

# Calcular la altura del cilindro
altura_cilindro = volumen_botella / (math.pi * (radio_botella ** 2))

# Calcular la distancia total de la botella
distancia_total = altura_botella - altura_cilindro

# Imprimir la distancia total de la botella
print("La distancia total de la botella cortada es:", round(distancia_total, 2), "cm.")
