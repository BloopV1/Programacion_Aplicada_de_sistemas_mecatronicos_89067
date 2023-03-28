# Definimos un diccionario con la información de nuestro horario
horario = {
    "Lunes": {
        "08:00 - 10:00": {
            "Materia": "Fundamentos ",
            "Salón": "PS - 204",
            "Profesor": "Juan Pérez"
        }
    },
    "Martes": {
        "07:00 - 09:00": {
            "Materia": "Calculo Multivariado",
            "Salón": "DB - 406",
            "Profesor": "Jairo lalynde"
        },
        "09:00 - 11:00": {
            "Materia": "Estatica",
            "Salón": "DB - 305",
            "Profesor": "Elmer cepeda"
        },
        "14:00 - 16:00": {
            "Materia": "Programación",
            "Salón": "GO - 303",
            "Profesor": "David Torres"
        }
    },
    # Agregar aquí información para otros días de la semana
}

# Pedimos al usuario que ingrese el nombre de la materia
materia = input("Ingresa el nombre de la materia: ")

# Buscamos la materia en el horario y mostramos su información
encontrada = False
for dia, clases in horario.items():
    for horario, info in clases.items():
        if info["Materia"] == materia:
            encontrada = True
            print(f"Día: {dia}")
            print(f"Hora: {horario}")
            print(f"Salón: {info['Salón']}")
            print(f"Profesor: {info['Profesor']}")
            break
    if encontrada:
        break

# Si la materia no fue encontrada, mostramos un mensaje de error
if not encontrada:
    print("No se encontró la materia en el horario.")
