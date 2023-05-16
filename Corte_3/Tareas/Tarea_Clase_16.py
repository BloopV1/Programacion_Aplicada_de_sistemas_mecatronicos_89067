import sqlite3

conn = sqlite3.connect('mi_base_de_datos.db')
conn.execute('''CREATE TABLE IF NOT EXISTS empleados
                 (id INTEGER PRIMARY KEY,
                  nombre TEXT,
                  salario REAL);''')

# Inserción de datos en la tabla
conn.execute("INSERT INTO empleados (nombre, salario) VALUES ('Juan', 3000)")
conn.execute("INSERT INTO empleados (nombre, salario) VALUES ('Pedro', 2500)")
conn.execute("INSERT INTO empleados (nombre, salario) VALUES ('María', 3500)")

# Consulta de datos
cursor = conn.execute("SELECT * FROM empleados WHERE salario > 2800")
for row in cursor:
    print(row)

# Actualización de datos
conn.execute("UPDATE empleados SET salario = 4000 WHERE nombre = 'María'")
conn.execute("DELETE FROM empleados WHERE nombre = 'Pedro'")
conn.close()
