import csv
import funciones

def main():
    with open('organization_data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

    lista_paises = funciones.lista_paises(data)
    id_pais = int(input('Ingrese el id del país que desea buscar: '))
    nombre_pais = lista_paises[id_pais - 1]
    print(f'País: {nombre_pais}')

    datos_pais = []
    for fila in data:
        if fila[4].lower() == nombre_pais.lower():
            datos_pais.append(fila)

    if len(datos_pais) > 0:
        empresa_mayor = []
        empresa_menor = []

        for fila in datos_pais:
            if int(fila[8]) == funciones.mayor(datos_pais):
                empresa_mayor.append(fila)
                print('La empresa con mayor # de empleados es: ')
                print(f'- Empresa: {fila[2]}')
                print(f'- Website: {fila[3]}')
                print(f'- Descripción: {fila[5]}')
                print(f'- Fundación: {fila[6]}')
                print(f'- Industria: {fila[7]}')
                print(f'- #Empleados: {fila[8]}')

            if int(fila[8]) == funciones.menor(datos_pais):
                empresa_menor.append(fila)
                print('La empresa con menor # de empleados es: ')
                print(f'- Empresa: {fila[2]}')
                print(f'- Website: {fila[3]}')
                print(f'- Descripción: {fila[5]}')
                print(f'- Fundación: {fila[6]}')
                print(f'- Industria: {fila[7]}')
                print(f'- #Empleados: {fila[8]}')

        print(f'El promedio de los empleados es: {round(funciones.suma(datos_pais) / len(datos_pais), 2)}')
        print(f'La cantidad de empresas es: {len(datos_pais)}')

    else:
        print(f"No se encontraron datos para el país {nombre_pais}.")

if __name__ == '__main__':
    main()
    