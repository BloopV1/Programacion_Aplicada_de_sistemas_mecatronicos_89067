#Diseñar una interfaz gráfica para realizar el registró de las ventas de una tienda de barrio, (recuerde los datos de la reforma tributaría).
#Cada vez que se haga clic en el botón de venta, se debe imprimir la factura con los detalles de la venta en la consola.

#Establecimiento(Nombre, Dirección)
#Producto (CódigoProducto, Nombre)
#ItemVenta (#factura, Cantidad, Precio 
#Bruto, IVA, PrecioTotal)
#Ventas (Fecha,#Cliente)

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi

class VentasApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Cargar el archivo .ui creado en Qt Designer
        loadUi("interfaz_de_ventas.ui", self)
        # Conectar el botón de registro de ventas con el método registrar_venta
        self.registrar_button.clicked.connect(self.registrar_venta)
        
    def registrar_venta(self):
        # Obtener los datos de la venta desde los widgets de entrada
        establecimiento = self.establecimiento_lineEdit.text()
        producto = self.producto_lineEdit.text()
        codigo_producto = self.codigo_lineEdit.text()
        cantidad = self.cantidad_lineEdit.text()
        precio_bruto = self.precio_lineEdit.text()
        cliente = self.cliente_lineEdit.text()
        
        # Calcular los valores de la venta
        precio_bruto = float(precio_bruto)
        iva = precio_bruto * 0.19
        precio_total = precio_bruto + iva
        
        # Crear la factura y mostrarla en la consola
        factura = f"Establecimiento: {establecimiento}\nProducto: {producto}\nCódigo Producto: {codigo_producto}\nCantidad: {cantidad}\nPrecio Bruto: {precio_bruto}\nIVA: {iva}\nPrecio Total: {precio_total}\nCliente: {cliente}\n"
        print(factura)

if __name__ == "__main__":
    # Crear la aplicación Qt
    app = QApplication(sys.argv)
    # Crear la ventana principal de la aplicación
    ventana = VentasApp()
    ventana.show()
    # Ejecutar el bucle de eventos Qt
    sys.exit(app.exec_())

