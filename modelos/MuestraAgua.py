class MuestraAgua:
    def __init__(self, fecha, ph, turbidez, presenciaEcoli,
                 contaminacionMicrobiologica, nivelSedimentos,
                 fuenteAgua):
        self.__fecha = fecha
        self.__ph = ph
        self.__turbidez = turbidez
        self.__presenciaEcoli = presenciaEcoli
        self.__contaminacionMicrobiologica = contaminacionMicrobiologica
        self.__nivelSedimentos = nivelSedimentos
        self.__nivelRiesgo = "Sin evaluar"
        self.__fuenteAgua = fuenteAgua