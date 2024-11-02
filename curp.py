import tkinter as tk
from tkinter import ttk
from datetime import datetime
import random

# Funciones auxiliares
def es_anio_bisiesto(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def obtener_vocal(nombre):
    for letra in nombre[1:]:
        if letra in "AEIOU":
            return letra
    return "X"

def obtener_consonante(nombre):
    for letra in nombre[1:]:
        if letra not in "AEIOU":
            return letra
    return "X"

def generar_codigo_anti_homonimia():
    numero = random.randint(0, 9)
    letra = chr(random.randint(65, 90))  # A-Z
    return f"{numero}{letra}"

# Función principal para generar la CURP
def generar_curp():
    nombre = entrada_nombre.get().strip().upper()
    apellido_paterno = entrada_apellido_paterno.get().strip().upper()
    apellido_materno = entrada_apellido_materno.get().strip().upper()
    dia_nacimiento = combo_dia.get()
    mes_nacimiento = combo_mes.get()
    anio_nacimiento = entrada_anio.get()
    genero = combo_genero.get()[0].upper()
    estado_nacimiento = combo_estado.get()

    if not (nombre and apellido_paterno and mes_nacimiento and anio_nacimiento and genero and estado_nacimiento):
        label_resultado.config(text="Por favor, completa todos los campos obligatorios.")
        return

    try:
        anio = int(anio_nacimiento)
        dia = int(dia_nacimiento)
        mes = int(mes_nacimiento)
        if dia == 29 and mes == 2 and not es_anio_bisiesto(anio):
            label_resultado.config(text="Error: el 29 de febrero solo es válido en años bisiestos.")
            return  
        fecha_nacimiento = datetime.strptime(f"{anio_nacimiento}-{mes_nacimiento}-{dia_nacimiento}", "%Y-%m-%d")
    except ValueError:
        label_resultado.config(text="Fecha de nacimiento inválida.")
        return

    curp = apellido_paterno[0] + obtener_vocal(apellido_paterno)
    curp += apellido_materno[0] if apellido_materno else "X"
    curp += nombre[0]
    curp += fecha_nacimiento.strftime("%y%m%d")
    curp += genero
    estados = {
        "Aguascalientes": "AS", "Baja California": "BC", "Baja California Sur": "BS", "Campeche": "CC", 
        "Chiapas": "CS", "Chihuahua": "CH", "Ciudad de México": "DF", "Coahuila": "CL", "Colima": "CM", 
        "Durango": "DG", "Guanajuato": "GT", "Guerrero": "GR", "Hidalgo": "HG", "Jalisco": "JC", 
        "México": "MC", "Michoacán": "MN", "Morelos": "MS", "Nayarit": "NT", "Nuevo León": "NL", 
        "Oaxaca": "OC", "Puebla": "PL", "Querétaro": "QT", "Quintana Roo": "QR", "San Luis Potosí": "SP", 
        "Sinaloa": "SL", "Sonora": "SR", "Tabasco": "TC", "Tamaulipas": "TS", "Tlaxcala": "TL", 
        "Veracruz": "VZ", "Yucatán": "YN", "Zacatecas": "ZS"
    }
    curp += estados.get(estado_nacimiento, "NE")
    curp += obtener_consonante(apellido_paterno)
    curp += obtener_consonante(apellido_materno) if apellido_materno else "X"
    curp += obtener_consonante(nombre)
    curp += generar_codigo_anti_homonimia()

    label_resultado.config(text="CURP generada: " + curp)

# Configuración de la interfaz
ventana = tk.Tk()
ventana.title("Generador de CURP")
ventana.geometry("500x500")
ventana.config(bg="#f0f0f0")

frame_principal = tk.Frame(ventana, bg="#d9e4f5", padx=20, pady=20)
frame_principal.pack(expand=True)

# Widgets de entrada
tk.Label(frame_principal, text="Nombre(s)*:", bg="#d9e4f5").grid(row=0, column=0, pady=5, padx=5, sticky='e')
entrada_nombre = tk.Entry(frame_principal)
entrada_nombre.grid(row=0, column=1, pady=5)

tk.Label(frame_principal, text="Primer apellido*:", bg="#d9e4f5").grid(row=1, column=0, pady=5, padx=5, sticky='e')
entrada_apellido_paterno = tk.Entry(frame_principal)
entrada_apellido_paterno.grid(row=1, column=1, pady=5)

tk.Label(frame_principal, text="Segundo apellido:", bg="#d9e4f5").grid(row=2, column=0, pady=5, padx=5, sticky='e')
entrada_apellido_materno = tk.Entry(frame_principal)
entrada_apellido_materno.grid(row=2, column=1, pady=5)

tk.Label(frame_principal, text="Día de nacimiento*:", bg="#d9e4f5").grid(row=3, column=0, pady=5, padx=5, sticky='e')
combo_dia = ttk.Combobox(frame_principal, values=[str(i) for i in range(1, 32)], width=5)
combo_dia.grid(row=3, column=1, sticky='w')

tk.Label(frame_principal, text="Mes de nacimiento*:", bg="#d9e4f5").grid(row=4, column=0, pady=5, padx=5, sticky='e')
combo_mes = ttk.Combobox(frame_principal, values=[f"{i:02d}" for i in range(1, 13)], width=5)
combo_mes.grid(row=4, column=1, sticky='w')

tk.Label(frame_principal, text="Año de nacimiento*:", bg="#d9e4f5").grid(row=5, column=0, pady=5, padx=5, sticky='e')
entrada_anio = tk.Entry(frame_principal, width=10)
entrada_anio.grid(row=5, column=1, pady=5)

tk.Label(frame_principal, text="Sexo*:", bg="#d9e4f5").grid(row=6, column=0, pady=5, padx=5, sticky='e')
combo_genero = ttk.Combobox(frame_principal, values=["Hombre", "Mujer"], width=10)
combo_genero.grid(row=6, column=1, pady=5)

tk.Label(frame_principal, text="Estado*:", bg="#d9e4f5").grid(row=7, column=0, pady=5, padx=5, sticky='e')
combo_estado = ttk.Combobox(frame_principal, values=[
    "Aguascalientes", "Baja California", "Baja California Sur", "Campeche", 
    "Chiapas", "Chihuahua", "Ciudad de México", "Coahuila", "Colima", 
    "Durango", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco", 
    "México", "Michoacán", "Morelos", "Nayarit", "Nuevo León", 
    "Oaxaca", "Puebla", "Querétaro", "Quintana Roo", "San Luis Potosí", 
    "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", 
    "Veracruz", "Yucatán", "Zacatecas"
])
combo_estado.grid(row=7, column=1, pady=5)

# Botón y resultado
boton_generar = tk.Button(frame_principal, text="Generar CURP", command=generar_curp, bg="#4CAF50", fg="white")
boton_generar.grid(row=8, column=0, columnspan=2, pady=20)

label_resultado = tk.Label(frame_principal, text="", bg="#d9e4f5", font=("Arial", 12))
label_resultado.grid(row=9, column=0, columnspan=2)

ventana.mainloop()
