import tkinter as tk
from tkinter import messagebox
from models.persona import Persona
from models.chinimal import Chinimal

print("Ejecutando GUI actualizado")
# Crear persona y algunos chinimales
persona = Persona("Cristian", "Iglesias")

condor = Chinimal("Cóndor", "Ave", "Negro y blanco", "carne", "acicalar alas")
pingüino = Chinimal("Pingüino", "Ave", "Blanco y negro", "pescado", "acicalar plumaje")
puma = Chinimal("Puma", "Mamífero", "Marrón", "vicuña", "dormir")

# Persona adopta chinimales
persona.adoptar_chinimal(condor)
persona.adoptar_chinimal(pingüino)
persona.adoptar_chinimal(puma)

def actualizar_estado(chinimal):
    estado_text.delete("1.0", tk.END)
    estado = (
        f"🐾 {chinimal.nombre} ({chinimal.especie})\n"
        f"Color: {chinimal.color}\n"
        f"Comida saludable: {chinimal.comida_saludable}\n"
        f"Actividad saludable: {chinimal.actividad_saludable}\n\n"
        f"Salud: {chinimal.salud}\n"
        f"Felicidad: {chinimal.felicidad}\n"
        f"Energía: {chinimal.energia}\n"
    )
    estado_text.insert(tk.END, estado)

def chinimal_seleccionado(event):
    try:
        idx = lista_chinimales.curselection()[0]
        chinimal = persona.chinimales[idx]
        actualizar_estado(chinimal)
    except IndexError:
        pass

def alimentar():
    try:
        idx = lista_chinimales.curselection()[0]
        chinimal = persona.chinimales[idx]
        alimento = entrada_alimento.get().strip()
        if alimento == "":
            messagebox.showwarning("Aviso", "Escribe un alimento para dar.")
            return
        persona.alimentar_chinimal(chinimal, alimento)
        actualizar_estado(chinimal)
    except IndexError:
        messagebox.showerror("Error", "Selecciona un chinimal primero.")

def hacer_actividad():
    try:
        idx = lista_chinimales.curselection()[0]
        chinimal = persona.chinimales[idx]
        persona.hacer_actividad_con_chinimal(chinimal)
        actualizar_estado(chinimal)
    except IndexError:
        messagebox.showerror("Error", "Selecciona un chinimal primero.")

# Crear ventana
ventana = tk.Tk()
ventana.title("Chinimales de Cristian")

# Listbox con chinimales
lista_chinimales = tk.Listbox(ventana, height=6)
for c in persona.chinimales:
    lista_chinimales.insert(tk.END, c.nombre)
lista_chinimales.pack()
lista_chinimales.bind("<<ListboxSelect>>", chinimal_seleccionado)

# Texto para mostrar estado
estado_text = tk.Text(ventana, height=10, width=50)
estado_text.pack()

# Entrada y botón para alimentar
tk.Label(ventana, text="Alimento:").pack()
entrada_alimento = tk.Entry(ventana)
entrada_alimento.pack()

boton_alimentar = tk.Button(ventana, text="Alimentar", command=alimentar)
boton_alimentar.pack()

# Botón para hacer actividad
boton_actividad = tk.Button(ventana, text="Hacer actividad saludable", command=hacer_actividad)
boton_actividad.pack()

# Mostrar estado del primer chinimal al iniciar
if persona.chinimales:
    lista_chinimales.selection_set(0)
    actualizar_estado(persona.chinimales[0])

ventana.mainloop()
