
import tkinter as tk
from tkinter import messagebox, ttk

from modelos.FuenteAgua import FuenteAgua


class FormularioFuente(tk.Toplevel):

    def __init__(self, padre, sistema, fuentes_registradas):
        super().__init__(padre)

        self.sistema = sistema
        self.fuentes_registradas = fuentes_registradas

        self.title("Registrar fuente de agua")
        self.geometry("430x440")
        self.resizable(False, False)

        tk.Label(
            self,
            text="Registro de fuente de agua",
            font=("Arial", 14, "bold")
        ).pack(pady=12)

        self.campos = {}

        campos = [
            ("Nombre de la fuente", "nombre"),
            ("Ubicación", "ubicacion"),
            ("Tipo de fuente", "tipo"),
            ("Población beneficiada", "poblacion")
        ]

        for etiqueta, clave in campos:
            tk.Label(self, text=etiqueta).pack()

            entrada = tk.Entry(self, width=35)
            entrada.pack(pady=4)

            self.campos[clave] = entrada

        tk.Label(self, text="Nivel de riesgo").pack()

        self.riesgo = ttk.Combobox(
            self,
            state="readonly",
            width=32,
            values=["Bajo", "Medio", "Alto", "Crítico"]
        )
        self.riesgo.pack(pady=4)
        self.riesgo.set("Bajo")

        tk.Button(
            self,
            text="Guardar fuente",
            command=self.guardar_fuente
        ).pack(pady=18)

    def guardar_fuente(self):
        try:
            nombre = self.campos["nombre"].get().strip()
            ubicacion = self.campos["ubicacion"].get().strip()
            tipo = self.campos["tipo"].get().strip()
            poblacion_texto = self.campos["poblacion"].get().strip()
            riesgo = self.riesgo.get()

            if not all([nombre, ubicacion, tipo, poblacion_texto, riesgo]):
                raise ValueError("Debes completar todos los campos.")

            poblacion = int(poblacion_texto)

            fuente = FuenteAgua(
                nombre,
                ubicacion,
                tipo,
                poblacion,
                riesgo
            )

            self.sistema.registrarFuente(fuente)

            self.fuentes_registradas.append(fuente)

            messagebox.showinfo(
                "Registro exitoso",
                "La fuente se registró correctamente.",
                parent=self
            )

            self.destroy()

        except (ValueError, TypeError) as error:
            messagebox.showerror(
                "Error de registro",
                str(error),
                parent=self
            )
