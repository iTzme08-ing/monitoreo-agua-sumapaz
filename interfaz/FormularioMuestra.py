
import tkinter as tk
from tkinter import messagebox, ttk

from modelos.MuestraAgua import MuestraAgua


class FormularioMuestra(tk.Toplevel):

    def __init__(self, padre, sistema, fuentes_registradas):
        super().__init__(padre)

        self.sistema = sistema
        self.fuentes_registradas = fuentes_registradas

        self.title("Registrar muestra de agua")
        self.geometry("460x610")
        self.resizable(False, False)

        tk.Label(
            self,
            text="Registro de muestra de agua",
            font=("Arial", 14, "bold")
        ).pack(pady=12)

        tk.Label(self, text="Fuente de agua").pack()

        self.fuente_seleccionada = ttk.Combobox(
            self,
            state="readonly",
            width=35,
            values=[
                fuente.getNombre()
                for fuente in self.fuentes_registradas
            ]
        )
        self.fuente_seleccionada.pack(pady=5)

        self.campos = {}

        campos = [
            ("Fecha (ej. 2026-10-14)", "fecha"),
            ("pH", "ph"),
            ("Turbidez", "turbidez"),
            ("Nivel de sedimentos", "sedimentos"),
            ("Resultado microbiológico", "microbiologica")
        ]

        for etiqueta, clave in campos:
            tk.Label(self, text=etiqueta).pack()

            entrada = tk.Entry(self, width=35)
            entrada.pack(pady=3)

            self.campos[clave] = entrada

        tk.Label(self, text="¿Presencia de E. coli?").pack(pady=(5, 0))

        self.ecoli = ttk.Combobox(
            self,
            state="readonly",
            width=32,
            values=["No", "Sí"]
        )
        self.ecoli.pack(pady=4)
        self.ecoli.set("No")

        tk.Button(
            self,
            text="Guardar muestra",
            command=self.guardar_muestra
        ).pack(pady=15)

    def guardar_muestra(self):
        try:
            nombre_fuente = self.fuente_seleccionada.get()

            fuente = next(
                (
                    f for f in self.fuentes_registradas
                    if f.getNombre() == nombre_fuente
                ),
                None
            )

            if fuente is None:
                raise ValueError("Selecciona una fuente válida.")

            fecha = self.campos["fecha"].get().strip()
            ph_texto = self.campos["ph"].get().strip()
            turbidez_texto = self.campos["turbidez"].get().strip()
            sedimentos_texto = self.campos["sedimentos"].get().strip()
            microbiologica = (
                self.campos["microbiologica"].get().strip()
            )

            if not all([
                fecha,
                ph_texto,
                turbidez_texto,
                sedimentos_texto,
                microbiologica,
                self.ecoli.get()
            ]):
                raise ValueError("Debes completar todos los campos.")

            ph = float(ph_texto)
            turbidez = float(turbidez_texto)
            sedimentos = float(sedimentos_texto)
            presencia_ecoli = self.ecoli.get() == "Sí"

            muestra = MuestraAgua(
                fecha,
                ph,
                turbidez,
                presencia_ecoli,
                microbiologica,
                sedimentos,
                fuente
            )

            self.sistema.registrarMuestra(muestra)

            messagebox.showinfo(
                "Registro exitoso",
                "La muestra se registró correctamente.",
                parent=self
            )

            self.destroy()

        except (ValueError, TypeError) as error:
            messagebox.showerror(
                "Error de registro",
                str(error),
                parent=self
            )
