def mayor(datos_pais):
    empleados = [int(fila[8]) for fila in datos_pais]
    return max(empleados)

def menor(datos_pais):
    empleados = [int(fila[8]) for fila in datos_pais]
    return min(empleados)

def suma(datos_pais):
    empleados = [int(fila[8]) for fila in datos_pais]
    return sum(empleados)

def lista_paises(data):
    paises = {fila[4] for fila in data}
    return sorted(paises)