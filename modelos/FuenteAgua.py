class FuenteAgua:
    def __init__(self, nombre, ubicacion, tipoFuente,
                 poblacionBeneficiada, nivelRiesgo):
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__tipoFuente = tipoFuente
        self.__poblacionBeneficiada = poblacionBeneficiada
        self.__nivelRiesgo = nivelRiesgo

    def getNombre(self):
            return self.__nombre
    
    def getUbicacion(self):
            return self.__ubicacion
    
    def getTipoFuente(self):
            return self.__tipoFuente
    
    def getPoblacionBeneficiada(self):
            return self.__poblacionBeneficiada
    
    def getNivelRiesgo(self):
            return self.__nivelRiesgo