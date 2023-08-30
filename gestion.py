import tkinter as tk
from tkinter import ttk, messagebox
import random
vuelos_output = None
num_vuelo_entry = None
origen_entry = None
destino_entry = None
fechasalida_entry = None
fechavuelta_entry = None
vuelos_agregados = []




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


def agregar_nuevo_vuelo():
    global vuelos_agregados_text
    numerovuelo = num_vuelo_entry.get()
    origenn = origen_entry.get()
    destinoo = destino_entry.get()
    fechasalidaa = fechasalida_entry.get()
    fechavueltaa = fechavuelta_entry.get()

    if numerovuelo and origenn and destinoo and fechasalidaa and fechavueltaa:
        try:
            numerovuelo = int(numerovuelo)

            # Resto del código para agregar el vuelo
            vuelo = {
                "numero": numerovuelo,
                "origen": origenn,
                "destino": destinoo,
                "fecha_salida": fechasalidaa,
                "fecha_vuelta": fechavueltaa
            }
            list_vuelos.append(vuelo)
            vuelos_agregados.append(vuelo)

            vuelos_agregados_text.delete("1.0", "end")
            num_vuelo_entry.delete(0, "end")
            origen_entry.delete(0, "end")
            destino_entry.delete(0, "end")
            fechasalida_entry.delete(0, "end")
            fechavuelta_entry.delete(0, "end")

            # Actualizar el contenido del Text widget con la lista de vuelos agregados
            vuelos_agregados_text.delete("1.0", "end")
            for vuelo in list_vuelos:
                vuelos_agregados_text.insert("end",
                                             f"Vuelo {vuelo['numero']}: \nOrigen: {vuelo['origen']} \nDestino: {vuelo['destino']} \nFecha de Salida: {vuelo['fecha_salida']}  \nFecha de Vuelta: {vuelo['fecha_vuelta']} \n==============================  \n ")

            messagebox.showinfo("Éxito", "Vuelo agregado exitosamente.")
        except ValueError:
            messagebox.showerror("Error", "El número de vuelo debe ser un valor numérico.")
    else:
        messagebox.showerror("Error", "Completa todos los campos.")



def eliminar_vuelo():
    global vuelos_agregados_text, eliminar_num_vuelo_entry
    numerovuelo = eliminar_num_vuelo_entry.get()

    if numerovuelo:
        try:
            numerovuelo = int(numerovuelo)

            # Resto del código para eliminar el vuelo
            vuelo_eliminado = None
            for vuelo in vuelos_agregados:
                if vuelo['numero'] == numerovuelo:
                    vuelo_eliminado = vuelo
                    break

            if vuelo_eliminado:
                vuelos_agregados.remove(vuelo_eliminado)

                vuelos_agregados_text.delete("1.0", "end")
                for vuelo in vuelos_agregados:
                    vuelos_agregados_text.insert("end",
                                                 f"Vuelo {vuelo['numero']}: \nOrigen: {vuelo['origen']} \nDestino: {vuelo['destino']} \nFecha de Salida: {vuelo['fecha_salida']}  \nFecha de Vuelta: {vuelo['fecha_vuelta']} \n==============================  \n ")

                messagebox.showinfo("Éxito", "Vuelo eliminado exitosamente.")
            else:
                messagebox.showerror("Error", "No se encontró un vuelo con ese número.")
        except ValueError:
            messagebox.showerror("Error", "El número de vuelo debe ser un valor numérico.")
    else:
        messagebox.showerror("Error", "Ingresa el número de vuelo a eliminar.")

    eliminar_num_vuelo_entry.delete(0, "end")




def mostrar_vuelos_aleatorios():
    aeropuertos = ['JFK', 'LAX', 'ORD', 'ATL', 'DFW', 'DEN', 'SFO', 'SEA', 'LAS', 'MIA']
    global vuelos_output
    vuelos_text = ""
    for _ in range(20):
        numero_vuelo = random.randint(100, 999)
        origen = random.choice(aeropuertos)
        destino = random.choice(aeropuertos)
        while destino == origen:
            destino = random.choice(aeropuertos)
        fecha_salida = f"{random.randint(1, 28)}/{random.randint(1, 12)}/2023"
        fecha_vuelta = f"{random.randint(1, 28)}/{random.randint(1, 12)}/2023"

        vuelos_text += f"Vuelo {numero_vuelo}:\n"
        vuelos_text += f"Origen: {origen}\n"
        vuelos_text += f"Destino: {destino}\n"
        vuelos_text += f"Fecha de Salida: {fecha_salida}\n"
        vuelos_text += f"Fecha de Vuelta: {fecha_vuelta}\n"
        vuelos_text += "=" * 30 + "\n"

    vuelos_output.delete("1.0", "end")  # Borra el contenido actual del Text widget
    vuelos_output.insert("end", vuelos_text)  # Inserta los vuelos aleatorios en el Text widget

def main_interface():
    global vuelos_agregados_text
    global num_vuelo_entry, origen_entry, destino_entry, fechasalida_entry, fechavuelta_entry, eliminar_num_vuelo_entry
    main_window = tk.Tk()
    main_window.title("Aeropuerto Villada")
gitgi
    tab_control = ttk.Notebook(main_window)

    vuelos_tab = ttk.Frame(tab_control)


    tab_control.add(vuelos_tab, text="Gestión de Vuelos")


    tab_control.pack(expand=1, fill="both")



    agregar_vuelo_button = tk.Button(vuelos_tab, text="Agregar Nuevo Vuelo", command=agregar_nuevo_vuelo)
    agregar_vuelo_button.pack()

    eliminar_vuelo_button = tk.Button(vuelos_tab, text="Eliminar Vuelo", command=eliminar_vuelo)
    eliminar_vuelo_button.pack()

    eliminar_num_vuelo_label = tk.Label(vuelos_tab, text="Número de Vuelo a Eliminar:")
    eliminar_num_vuelo_label.pack()
    eliminar_num_vuelo_entry = tk.Entry(vuelos_tab)
    eliminar_num_vuelo_entry.pack()

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

    global vuelos_output

    mostrar_vuelos_aleatorios_button = tk.Button(vuelos_tab, text="Mostrar Vuelos Disponibles",
                                                 command=mostrar_vuelos_aleatorios)
    mostrar_vuelos_aleatorios_button.pack()

    vuelos_output = tk.Text(vuelos_tab, height=10, width=50)
    vuelos_output.pack()

    vuelos_agregados_text = tk.Text(vuelos_tab, height=10, width=50)
    vuelos_agregados_text.pack()

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


login_window.mainloop()

