from modelos.FuenteAgua import FuenteAgua
from modelos.MuestraAgua import MuestraAgua

class SistemaMonitoreo:
    def __init__(self):
        self.__fuentes = []
        self.__muestras = []

    def registrarFuente(self, fuente):
        if not isinstance(fuente, FuenteAgua):
            raise ValueError("Debe ingresar una fuente de agua válida.")

        for registrada in self.__fuentes:
            if registrada.getNombre().lower() == fuente.getNombre().lower():
                raise ValueError("La fuente ya está registrada.")

        fuente.registrarFuente()
        self.__fuentes.append(fuente)