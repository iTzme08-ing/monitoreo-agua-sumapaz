import tkinter as tk

from modelos.SistemaMonitoreo import SistemaMonitoreo
from interfaz.VentanaPrincipal import VentanaPrincipal

def main():
    sistema = SistemaMonitoreo()

    ventana = tk.Tk()
    aplicacion = VentanaPrincipal(ventana, sistema)

    ventana.mainloop()


if __name__ == "__main__":
    main()