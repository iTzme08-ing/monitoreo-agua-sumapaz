from modelos.FuenteAgua import FuenteAgua
from modelos.MuestraAgua import MuestraAgua

class SistemaMonitoreo:
    def __init__(self):
        self.__fuentes = []
        self.__muestras = []