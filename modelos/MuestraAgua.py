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

    # Setters

    def setFecha(self, fecha):
        if not isinstance(fecha, str) or not fecha.strip():
            raise ValueError("La fecha no puede estar vacía.")
        self.__fecha = fecha.strip()

    def setPh(self, ph):
        if type(ph) not in (int, float) or not 0 <= ph <= 14:
            raise ValueError("El pH debe estar entre 0 y 14.")
        self.__ph = float(ph)

    def setTurbidez(self, turbidez):
        if type(turbidez) not in (int, float) or turbidez < 0:
            raise ValueError("La turbidez no puede ser negativa.")
        self.__turbidez = float(turbidez)

    def setPresenciaEcoli(self, presencia):
        if type(presencia) != bool:
            raise ValueError("La presencia de E. coli debe ser True o False.")
        self.__presenciaEcoli = presencia

    def setContaminacionMicrobiologica(self, contaminacion):
        if not isinstance(contaminacion, str) or not contaminacion.strip():
            raise ValueError("Debe describir el resultado microbiológico.")
        self.__contaminacionMicrobiologica = contaminacion.strip()

    def setNivelSedimentos(self, nivel):
        if type(nivel) not in (int, float) or nivel < 0:
            raise ValueError("El nivel de sedimentos no puede ser negativo.")
        self.__nivelSedimentos = float(nivel)

    def setFuenteAgua(self, fuente):
        from modelos.FuenteAgua import FuenteAgua

        if not isinstance(fuente, FuenteAgua):
            raise ValueError("Debe asociar una fuente de agua válida.")
        self.__fuenteAgua = fuente

    # Metodos principales

    def calcularRiesgo(self):
        anomalías = 0

        if self.__presenciaEcoli:
            self.__nivelRiesgo = "Crítico"
            return self.__nivelRiesgo

        resultado = self.__contaminacionMicrobiologica.strip().lower()
        if resultado not in ("ninguna", "no detectada", "ausente"):
            anomalías += 1

        # Criterios para determinar el nivel de riesgo basado en los parámetros de la muestra
        if not 6.5 <= self.__ph <= 8.5:
            anomalías += 1

        if self.__turbidez > 5:
            anomalías += 1

        if self.__nivelSedimentos > 5:
            anomalías += 1

        if anomalías >= 2:
            self.__nivelRiesgo = "Alto"
        elif anomalías == 1:
            self.__nivelRiesgo = "Medio"
        else:
            self.__nivelRiesgo = "Bajo"

        return self.__nivelRiesgo

    def evaluarCalidad(self):
        riesgo = self.calcularRiesgo()

        if riesgo == "Bajo":
            return "Sin alertas según los criterios del prototipo"
        elif riesgo == "Medio":
            return "Requiere seguimiento"
        elif riesgo == "Alto":
            return "Requiere atención prioritaria"
        else:
            return "Riesgo crítico: requiere atención inmediata"