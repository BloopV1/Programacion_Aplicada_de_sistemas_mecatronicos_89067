horarios = {
    "Fundamentos de Investigacion": ["Lunes", "9:00 am - 11:00 am", "Salón 206 PS", " jaja no me acuerdo "],
    "Calculo Multivariado": ["Martes , Jueves", "2:00 PM", "Salón 407 DB", "Jairo Lalynde"],
    "Cirtcuitos AC": ["Miércoles , Viernes", "9:00 AM", "Salón 306 DB", "Roberto Bohorquez Avila"],
    "Programacion Aplicada": ["Martes , Jueves", "11:00 AM", "Salón 303 GO", "David Torres"],
    "Materiales": ["Viernes , Miercoles ", "9:00 am - 11:00 am","Salon 307 DB", "Elmer Cepeda"],
    "Estatica": ["Martes , Jueves", "9:00 am - 11:00 am", "Salón 306 DB", "Elmer Cepeda"]
}

# Pedir al usuario el nombre de la materia
materia = input("Ingrese el nombre de la materia para consultar su horario: ")

# Obtener el horario de la materia
if materia in horarios:
    horario = horarios[materia]
    print(f"La materia {materia} se dicta los {horario[0]} a las {horario[1]} en el {horario[2]}, con el profesor {horario[3]}.")
else:
    print("La materia ingresada no se encuentra en el horario.")