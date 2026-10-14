class FuenteAgua:
    def __init__(self, nombre, ubicacion, tipoFuente,
                 poblacionBeneficiada, nivelRiesgo):
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__tipoFuente = tipoFuente
        self.__poblacionBeneficiada = poblacionBeneficiada
        self.__nivelRiesgo = nivelRiesgo

    # Getters
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

    # Setters
    def setNombre(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = nombre.strip()

    def setUbicacion(self, ubicacion):
        if not isinstance(ubicacion, str) or not ubicacion.strip():
            raise ValueError("La ubicación no puede estar vacía.")
        self.__ubicacion = ubicacion.strip()

    def setTipoFuente(self, tipoFuente):
        if not isinstance(tipoFuente, str) or not tipoFuente.strip():
            raise ValueError("El tipo de fuente no puede estar vacío.")
        self.__tipoFuente = tipoFuente.strip()

    def setPoblacionBeneficiada(self, poblacion):
        if type(poblacion) != int or poblacion < 0:
            raise ValueError(
                "La población debe ser un entero mayor o igual a cero."
            )
        self.__poblacionBeneficiada = poblacion

    def setNivelRiesgo(self, nivelRiesgo):
        niveles = ["Bajo", "Medio", "Alto", "Crítico"]

        if not isinstance(nivelRiesgo, str):
            raise ValueError("El nivel de riesgo debe ser texto.")

        if nivelRiesgo.strip().capitalize() not in niveles:
            raise ValueError(
                "El riesgo debe ser Bajo, Medio, Alto o Crítico."
            )

        self.__nivelRiesgo = nivelRiesgo.strip().capitalize()

