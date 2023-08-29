import tkinter as tk
from tkinter import ttk, messagebox
import funciones
import clases

usuarios = {
    "admin": "password"
}

def registrar_usuario():
    nuevo_usuario = nuevo_usuario_entry.get()
    nueva_contraseña = nueva_contraseña_entry.get()

    if nuevo_usuario and nueva_contraseña:
        if nuevo_usuario not in usuarios:
            usuarios[nuevo_usuario] = nueva_contraseña
            messagebox.showinfo("Registro Exitoso", "Usuario registrado correctamente.")
        else:
            messagebox.showerror("Error", "El usuario ya existe.")
    else:
        messagebox.showerror("Error", "Ingresa un usuario y contraseña válidos.")

def login():
    usuario = usuario_entry.get()
    contraseña = contraseña_entry.get()

    if usuario in usuarios and usuarios[usuario] == contraseña:
        login_window.destroy()
        main_interface()
    else:
        messagebox.showerror("Error", "Credenciales incorrectas")

def mostrar_vuelos():
    vuelos_output.delete("1.0", "end")
    vuelos_output.insert("end", "\n".join(list_vuelos))

def agregar_nuevo_vuelo():
    numerovuelo = int(num_vuelo_entry.get())
    origenn = origen_entry.get()
    destinoo = destino_entry.get()
    fechasalidaa = fechasalida_entry.get()
    fechavueltaa = fechavuelta_entry.get()
    funciones.agregar_vuelo(numerovuelo, origenn, destinoo, fechasalidaa, fechavueltaa, list_vuelos)
    messagebox.showinfo("Éxito", "Vuelo agregado exitosamente.")
    num_vuelo_entry.delete(0, "end")
    origen_entry.delete(0, "end")
    destino_entry.delete(0, "end")
    fechasalida_entry.delete(0, "end")
    fechallegada_entry.delete(0, "end")

def eliminar_vuelo():
    numerovuelo = int(eliminar_num_vuelo_entry.get())
    funciones.eliminar_vuelo(numerovuelo, list_vuelos)
    messagebox.showinfo("Éxito", "Vuelo eliminado exitosamente.")
    eliminar_num_vuelo_entry.delete(0, "end")

def main_interface():
    main_window = tk.Tk()
    main_window.title("Gestión de Vuelos y Itinerarios")

    tab_control = ttk.Notebook(main_window)

    vuelos_tab = ttk.Frame(tab_control)
    itinerarios_tab = ttk.Frame(tab_control)

    tab_control.add(vuelos_tab, text="Gestión de Vuelos")
    tab_control.add(itinerarios_tab, text="Gestión de Itinerarios")

    tab_control.pack(expand=1, fill="both")

    agregar_vuelo_button = tk.Button(vuelos_tab, text="Agregar Nuevo Vuelo", command=agregar_nuevo_vuelo)
    agregar_vuelo_button.pack()

    eliminar_vuelo_button = tk.Button(vuelos_tab, text="Eliminar Vuelo", command=eliminar_vuelo)
    eliminar_vuelo_button.pack()

    num_vuelo_label = tk.Label(vuelos_tab, text="Número de Vuelo:")
    num_vuelo_label.pack()
    num_vuelo_entry = tk.Entry(vuelos_tab)
    num_vuelo_entry.pack()

    origen_label = tk.Label(vuelos_tab, text="Origen:")
    origen_label.pack()
    origen_entry = tk.Entry(vuelos_tab)
    origen_entry.pack()

    destino_label = tk.Label(vuelos_tab, text="Destino:")
    destino_label.pack()
    destino_entry = tk.Entry(vuelos_tab)
    destino_entry.pack()

    fechasalida_label = tk.Label(vuelos_tab, text="Fecha de Salida:")
    fechasalida_label.pack()
    fechasalida_entry = tk.Entry(vuelos_tab)
    fechasalida_entry.pack()

    fechavuelta_label = tk.Label(vuelos_tab, text="Fecha de Vuelta:")
    fechavuelta_label.pack()
    fechavuelta_entry = tk.Entry(vuelos_tab)
    fechavuelta_entry.pack()

    vuelos_output = tk.Text(vuelos_tab, height=10, width=50)
    vuelos_output.pack()

    mostrar_vuelos_button = tk.Button(vuelos_tab, text="Mostrar Vuelos Disponibles", command=mostrar_vuelos)
    mostrar_vuelos_button.pack()

    main_window.mainloop()

login_window = tk.Tk()
login_window.title("Inicio de Sesión")

nuevo_usuario_label = tk.Label(login_window, text="Nuevo Usuario:")
nuevo_usuario_label.pack()

nuevo_usuario_entry = tk.Entry(login_window)
nuevo_usuario_entry.pack()

nueva_contraseña_label = tk.Label(login_window, text="Nueva Contraseña:")
nueva_contraseña_label.pack()

nueva_contraseña_entry = tk.Entry(login_window, show="*")
nueva_contraseña_entry.pack()

registrar_button = tk.Button(login_window, text="Registrar Usuario", command=registrar_usuario)
registrar_button.pack()

usuario_label = tk.Label(login_window, text="Usuario:")
usuario_label.pack()

usuario_entry = tk.Entry(login_window)
usuario_entry.pack()

contraseña_label = tk.Label(login_window, text="Contraseña:")
contraseña_label.pack()

contraseña_entry = tk.Entry(login_window, show="*")
contraseña_entry.pack()

login_button = tk.Button(login_window, text="Iniciar Sesión", command=login)
login_button.pack()

list_vuelos = []
list_itinerarios = []

login_window.mainloop()

