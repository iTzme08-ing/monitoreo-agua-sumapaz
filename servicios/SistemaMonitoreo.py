from modelos.FuenteAgua import FuenteAgua
from modelos.MuestraAgua import MuestraAgua

class SistemaMonitoreo:
    def __init__(self):
        self.__fuentes = []
        self.__muestras = []

    # Metodos principales

    def registrarFuente(self, fuente):
        if not isinstance(fuente, FuenteAgua):
            raise ValueError("Debe ingresar una fuente de agua válida.")

        for registrada in self.__fuentes:
            if registrada.getNombre().lower() == fuente.getNombre().lower():
                raise ValueError("La fuente ya está registrada.")

        fuente.registrarFuente()
        self.__fuentes.append(fuente)

    def registrarMuestra(self, muestra):
        if not isinstance(muestra, MuestraAgua):
            raise ValueError("Debe ingresar una muestra válida.")

        fuente = muestra.getFuenteAgua()

        if not any(fuente is registrada for registrada in self.__fuentes):
            raise ValueError("La fuente de la muestra no está registrada.")

        muestra.calcularRiesgo()
        self.__muestras.append(muestra)