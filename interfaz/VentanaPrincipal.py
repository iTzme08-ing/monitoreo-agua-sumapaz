
import tkinter as tk
from tkinter import messagebox

from interfaz.FormularioFuente import FormularioFuente
from interfaz.FormularioMuestra import FormularioMuestra


class VentanaPrincipal(tk.Tk):

    def __init__(self, sistema):
        super().__init__()

        self.sistema = sistema
        self.fuentes_registradas = []

        self.title("Sistema de Monitoreo de Agua - Sumapaz")
        self.geometry("650x450")
        self.resizable(False, False)

        titulo = tk.Label(
            self,
            text="MONITOREO DE CALIDAD DEL AGUA",
            font=("Arial", 17, "bold")
        )
        titulo.pack(pady=(25, 8))

        subtitulo = tk.Label(
            self,
            text="Zonas rurales de Sumapaz",
            font=("Arial", 11)
        )
        subtitulo.pack(pady=(0, 25))

        tk.Button(
            self,
            text="Registrar fuente de agua",
            width=30,
            command=self.abrir_formulario_fuente
        ).pack(pady=8)

        tk.Button(
            self,
            text="Registrar muestra de agua",
            width=30,
            command=self.abrir_formulario_muestra
        ).pack(pady=8)

        tk.Button(
            self,
            text="Consultar historial",
            width=30,
            command=self.consultar_historial
        ).pack(pady=8)

        tk.Button(
            self,
            text="Evaluar fuente",
            width=30,
            command=self.evaluar_fuente
        ).pack(pady=8)

        tk.Button(
            self,
            text="Salir",
            width=30,
            command=self.destroy
        ).pack(pady=20)

    def abrir_formulario_fuente(self):
        FormularioFuente(
            self,
            self.sistema,
            self.fuentes_registradas
        )

    def abrir_formulario_muestra(self):
        if not self.fuentes_registradas:
            messagebox.showwarning(
                "Sin fuentes",
                "Primero debes registrar una fuente de agua."
            )
            return

        FormularioMuestra(
            self,
            self.sistema,
            self.fuentes_registradas
        )

    def consultar_historial(self):
        messagebox.showinfo(
            "Funcionalidad pendiente",
            "Esta opción se conectará cuando "
            "esté implementado consultarHistorial."
        )

    def evaluar_fuente(self):
        messagebox.showinfo(
            "Funcionalidad pendiente",
            "Esta opción se conectará cuando "
            "esté implementado evaluarFuente."
        )
