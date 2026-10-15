import tkinter as tk

from servicios.SistemaMonitoreo import SistemaMonitoreo
from interfaz.VentanaPrincipal import VentanaPrincipal

def main():
    sistema = SistemaMonitoreo()
    aplicacion = VentanaPrincipal(sistema)
    aplicacion.mainloop()

if __name__ == "__main__":
    main()