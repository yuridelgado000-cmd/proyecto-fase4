import tkinter as tk
from tkinter import messagebox, ttk

from logica import SistemaReservas

from excepciones import (
    ClienteInvalido,
    ErrorReserva,
    ServicioNoDisponible,
    ErrorCliente
)
#La clase Aplicacion se encarga de crear y estionar toda la interfaz

class Aplicacion:

    def __init__(self, root):

        self.root = root
        self.root.title("Sistema de Reservas")
        self.root.geometry("750x650")
        self.root.config(bg="#dbeeff")

        
        self.sistema = SistemaReservas()


        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure(
            "TCombobox",
            fieldbackground="white",
            background="#1e88e5",
            foreground="black"
        )

       
        titulo = tk.Label(
            root,
            text="SISTEMA DE RESERVAS",
            font=("Arial", 22, "bold"),
            bg="#dbeeff",
            fg="#0d47a1"
        )

        titulo.pack(pady=15)

    
        frame = tk.Frame(
            root,
            bg="white",
            bd=3,
            relief="ridge"
        )

        frame.pack(
            padx=20,
            pady=10,
            fill="both",
            expand=True
        )
        
        etiquetas = [
            "Nombre:",
            "Edad:",
            "Correo:",
            "Tipo de Servicio:",
            "Nombre Servicio:",
            "Precio:",
            "Duración:"
        ]

        for i, texto in enumerate(etiquetas):

            tk.Label(
                frame,
                text=texto,
                bg="white",
                fg="#0d47a1",
                font=("Arial", 11, "bold")
            ).grid(
                row=i,
                column=0,
                pady=12,
                padx=15,
                sticky="w"
            )

        # ENTRADAS

        self.entry_nombre = tk.Entry(
            frame,
            width=32,
            font=("Arial", 10),
            bg="#f5fbff"
        )

        self.entry_nombre.grid(row=0, column=1)

        self.entry_edad = tk.Entry(
            frame,
            width=32,
            font=("Arial", 10),
            bg="#f5fbff"
        )

        self.entry_edad.grid(row=1, column=1)

        self.entry_correo = tk.Entry(
            frame,
            width=32,
            font=("Arial", 10),
            bg="#f5fbff"
        )

        self.entry_correo.grid(row=2, column=1)

        # COMBOBOX
        
        self.combo_servicio = ttk.Combobox(
            frame,
            values=[
                "Reserva Sala",
                "Alquiler Equipo",
                "Asesoría"
            ],
            state="readonly",
            width=29,
            font=("Arial", 10)
        )

        self.combo_servicio.grid(row=3, column=1)
        self.combo_servicio.current(0)

        self.entry_servicio = tk.Entry(
            frame,
            width=32,
            font=("Arial", 10),
            bg="#f5fbff"
        )

        self.entry_servicio.grid(row=4, column=1)

        self.entry_precio = tk.Entry(
            frame,
            width=32,
            font=("Arial", 10),
            bg="#f5fbff"
        )

        self.entry_precio.grid(row=5, column=1)

        self.entry_duracion = tk.Entry(
            frame,
            width=32,
            font=("Arial", 10),
            bg="#f5fbff"
        )

        self.entry_duracion.grid(row=6, column=1)

        # BOTONES
        
        boton_reservar = tk.Button(
            frame,
            text="Confirmar Reserva",
            bg="#1976d2",
            fg="white",
            font=("Arial", 11, "bold"),
            width=18,
            command=self.realizar_reserva
        )

        boton_reservar.grid(
            row=7,
            column=0,
            pady=25
        )

        boton_cancelar = tk.Button(
            frame,
            text="Cancelar Reserva",
            bg="#64b5f6",
            fg="white",
            font=("Arial", 11, "bold"),
            width=18,
            command=self.cancelar_reserva
        )

        boton_cancelar.grid(
            row=7,
            column=1
        )

        # RESULTADOS
        
        self.texto_resultado = tk.Text(
            root,
            height=12,
            width=85,
            bg="white",
            fg="#0d47a1",
            font=("Consolas", 10)
        )

        self.texto_resultado.pack(pady=15)

    
    # REALIZAR RESERVA

    def realizar_reserva(self):

     try:

        resultado = self.sistema.realizar_reserva(
            self.entry_nombre.get(),
            self.entry_edad.get(),
            self.entry_correo.get(),
            self.combo_servicio.get(),
            self.entry_servicio.get(),
            self.entry_precio.get(),
            self.entry_duracion.get()
        )

        self.texto_resultado.delete(
            "1.0",
            tk.END
        )

        self.texto_resultado.insert(
            tk.END,
            resultado
        )

        messagebox.showinfo(
            "Éxito",
            "Reserva realizada correctamente"
        )
        self.entry_nombre.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)
        self.entry_correo.delete(0, tk.END)
        self.entry_servicio.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)
        self.entry_duracion.delete(0, tk.END)
     except (
    ClienteInvalido,
    ErrorReserva,
    ServicioNoDisponible,
    ErrorCliente,
    ValueError
) as e:

        messagebox.showerror(
            "Error",
            str(e)
        )
    # CANCELAR RESERVA
    
    def cancelar_reserva(self):

        try:

            mensaje = self.sistema.cancelar_reserva()

            self.texto_resultado.delete(
                "1.0",
                tk.END
            )

            self.texto_resultado.insert(
                tk.END,
                mensaje
            )

            messagebox.showwarning(
                "Cancelado",
                "Reserva cancelada"
            )

        except ErrorReserva as e:

            messagebox.showerror(
                "Error",
                str(e)
            )