import csv

def main():
    with open('Catalogo.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

class Articulo:
    def __init__(self, idArticulo, precioBase, unidExistencia):
        self.idArticulo = idArticulo
        self.precioBase = precioBase
        self.unidExistencia = unidExistencia

    def setPrecioBase(self, precioBase):
        self.precioBase = precioBase

    def setunidExistencia(self, unidExistencia):
        self.unidExistencia = unidExistencia

    def getPrecioBase(self):
        return self.precioBase

    def getunidExistencia(self):
        return self.unidExistencia

    def precioFinal(self):
        raise NotImplementedError("Subclase debe implementar el método precioFinal")

class Bebida(Articulo):
    def __init__(self, idArticulo, precioBase, unidExistencia, cantUnidad, proveedor):
        super().__init__(idArticulo, precioBase, unidExistencia)
        self.cantUnidad = cantUnidad
        self.proveedor = proveedor

    def setcantUnidad(self, cantUnidad):
        self.cantUnidad = cantUnidad

    def setProveedor(self, proveedor):
        self.proveedor = proveedor

    def getcantUnidad(self):
        return self.cantUnidad

    def getProveedor(self):
        return self.proveedor

    def precioFinal(self):
        return self.getPrecioBase() * 1.1

class Lacteo(Articulo):
    def __init__(self, idArticulo, precioBase, unidExistencia, cantUnidad, proveedor):
        super().__init__(idArticulo, precioBase, unidExistencia)
        self.cantUnidad = cantUnidad
        self.proveedor = proveedor

    def setcantUnidad(self, cantUnidad):
        self.cantUnidad = cantUnidad

    def setProveedor(self, proveedor):
        self.proveedor = proveedor

    def getcantUnidad(self):
        return self.cantUnidad

    def getProveedor(self):
        return self.proveedor

    def precioFinal(self):
        return self.getPrecioBase() * 1.2

class Condimento(Articulo):
    def __init__(self, idArticulo, precioBase, unidExistencia, cantUnidad, proveedor):
        super().__init__(idArticulo, precioBase, unidExistencia)
        self.cantUnidad = cantUnidad
        self.proveedor = proveedor

    def setcantUnidad(self, cantUnidad):
        self.cantUnidad = cantUnidad

    def setProveedor(self, proveedor):
        self.proveedor = proveedor

    def getcantUnidad(self):
        return self.cantUnidad

    def getProveedor(self):
        return self.proveedor

    def precioFinal(self):
        return self.getPrecioBase() * 1

def leer ():
    with open("Catalogo.csv","r") as archivo:
        lectura = csv.reader(archivo)
        datos = list(lectura)
        print(datos)


def Categorias(datos):
    Categoria = set()
    for fila in datos:
        Categoria.add(fila[3])
        return sorted (Categoria)
    