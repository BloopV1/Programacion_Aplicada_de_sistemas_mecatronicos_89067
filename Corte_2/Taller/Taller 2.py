import csv
import funciones

def main():
    with open('organization_data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

    lista_paises = funciones.lista_paises(data)
    id_pais = int(input('Ingrese el id del país que desea buscar: '))
    nombre_pais = lista_paises[id_pais - 1]
    print(f'Pais: {nombre_pais}')

    datos_pais = [fila for fila in data if fila[4].lower() == nombre_pais.lower()]

    if datos_pais:
        empleados = [int(fila[8]) for fila in datos_pais]
        empleados_promedio = round(sum(empleados) / len(empleados), 2)

        empresa_mayor = max(datos_pais, key=lambda x: int(x[8]))
        print(f'La empresa con mayor # de empleados es: ')
        print(f'- Empresa: {empresa_mayor[2]}')
        print(f'- Website: {empresa_mayor[3]}')
        print(f'- Descripcion: {empresa_mayor[5]}')
        print(f'- fundacion: {empresa_mayor[6]}')
        print(f'- industria: {empresa_mayor[7]}')
        print(f'- #Empleados: {empresa_mayor[8]}')

        empresa_menor = min(datos_pais, key=lambda x: int(x[8]))
        print(f'La empresa con menor # de empleados es: ')
        print(f'- Empresa: {empresa_menor[2]}')
        print(f'- Website: {empresa_menor[3]}')
        print(f'- Descripcion: {empresa_menor[5]}')
        print(f'- fundacion: {empresa_menor[6]}')
        print(f'- industria: {empresa_menor[7]}')
        print(f'- #Empleados: {empresa_menor[8]}')

        print(f'El promedio de los empleados es: {empleados_promedio}')
        print(f'La cantidad de empresas es: {len(datos_pais)}')
    else:
        print(f"No se encontraron datos para el país {nombre_pais}.")

if __name__ == '__main__':
    main()
    