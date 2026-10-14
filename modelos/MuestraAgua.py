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

    # Getters
    def getFecha(self):
        return self.__fecha

    def getPh(self):
        return self.__ph

    def getTurbidez(self):
        return self.__turbidez

    def getPresenciaEcoli(self):
        return self.__presenciaEcoli

    def getContaminacionMicrobiologica(self):
        return self.__contaminacionMicrobiologica

    def getNivelSedimentos(self):
        return self.__nivelSedimentos

    def getNivelRiesgo(self):
        return self.__nivelRiesgo

    def getFuenteAgua(self):
        return self.__fuenteAgua