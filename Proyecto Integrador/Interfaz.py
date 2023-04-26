import math
import tkinter as tk

# Crear una ventana
ventana = tk.Tk()
ventana.title("Calculadora de distancia de corte de botellas")

# Crear los widgets
lbl_altura_botella = tk.Label(ventana, text="Altura de la botella en cm:")
txt_altura_botella = tk.Entry(ventana)

lbl_diametro_botella = tk.Label(ventana, text="Diámetro de la botella en cm:")
txt_diametro_botella = tk.Entry(ventana)

lbl_litros = tk.Label(ventana, text="Litros:")
txt_litros = tk.Entry(ventana)

lbl_mililitros = tk.Label(ventana, text="Mililitros:")
txt_mililitros = tk.Entry(ventana)

lbl_resultado = tk.Label(ventana, text="La distancia total de la botella cortada es:")

lbl_distancia_total = tk.Label(ventana, text="")
btn_calcular = tk.Button(ventana, text="Calcular")

# Colocar los widgets en la ventana
lbl_altura_botella.grid(row=0, column=0, padx=10, pady=10)
txt_altura_botella.grid(row=0, column=1, padx=10, pady=10)

lbl_diametro_botella.grid(row=1, column=0, padx=10, pady=10)
txt_diametro_botella.grid(row=1, column=1, padx=10, pady=10)

lbl_litros.grid(row=2, column=0, padx=10, pady=10)
txt_litros.grid(row=2, column=1, padx=10, pady=10)

lbl_mililitros.grid(row=3, column=0, padx=10, pady=10)
txt_mililitros.grid(row=3, column=1, padx=10, pady=10)

lbl_resultado.grid(row=4, column=0, padx=10, pady=10)
lbl_distancia_total.grid(row=4, column=1, padx=10, pady=10)

btn_calcular.grid(row=5, column=1, padx=10, pady=10)

# Definir la función que se ejecutará al hacer clic en el botón
def calcular_distancia_total():
    # Obtener los valores de entrada
    altura_botella = float(txt_altura_botella.get())
    diametro_botella = float(txt_diametro_botella.get())
    litros = int(txt_litros.get())
    mililitros = int(txt_mililitros.get())

    # Calcular la distancia total
    volumen_botella = litros + (mililitros / 1000)
    radio_botella = diametro_botella / 2
    altura_cilindro = volumen_botella / (math.pi * (radio_botella ** 2))
    distancia_total = altura_botella - altura_cilindro

    # Mostrar el resultado
    lbl_distancia_total.config(text=str(round(distancia_total, 2)) + " cm.")

# Asociar la función al botón
btn_calcular.config(command=calcular_distancia_total)

# Ejecutar la ventana
ventana.mainloop()

