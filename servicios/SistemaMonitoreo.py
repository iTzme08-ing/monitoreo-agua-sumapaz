from modelos.FactorContaminacion import factores_por_defecto
from modelos.Monitoreo import Monitoreo


class SistemaMonitoreo:
    """Lógica principal: registro, consulta y evaluación de la calidad del agua."""

    def __init__(self, factores=None):
        self.factores = factores if factores is not None else factores_por_defecto()
        self.fuentes = {}

    # ---------- control de acceso ----------
    @staticmethod
    def _exigir(usuario, accion):
        if not usuario.puede(accion):
            raise PermissionError(f"El rol '{usuario.rol}' no puede realizar: {accion}")

    # ---------- registro ----------
    def registrar_fuente(self, usuario, fuente):
        self._exigir(usuario, "registrar_fuente")
        if fuente.id_fuente in self.fuentes:
            raise ValueError(f"Ya existe una fuente con id {fuente.id_fuente}.")
        self.fuentes[fuente.id_fuente] = fuente

    def registrar_muestra(self, usuario, muestra):
        self._exigir(usuario, "registrar_muestra")
        fuente = self.obtener_fuente(muestra.id_fuente)
        fuente.agregar_muestra(muestra)

    def obtener_fuente(self, id_fuente):
        if id_fuente not in self.fuentes:
            raise KeyError(f"No existe la fuente {id_fuente}.")
        return self.fuentes[id_fuente]

    # ---------- consulta ----------
    def consultar_estado(self, usuario, id_fuente):
        """Evalúa la última muestra de la fuente. None si no tiene muestras."""
        self._exigir(usuario, "consultar")
        muestra = self.obtener_fuente(id_fuente).ultima_muestra()
        return Monitoreo(muestra, self.factores) if muestra else None

    def historial(self, usuario, id_fuente):
        self._exigir(usuario, "historial")
        return self.analizar_muestras(self.obtener_fuente(id_fuente).muestras)

    def generar_alertas(self, usuario):
        self._exigir(usuario, "alertas")
        alertas = []
        for fuente in self.fuentes.values():
            muestra = fuente.ultima_muestra()
            if muestra:
                resultado = Monitoreo(muestra, self.factores)
                if not resultado.apto:
                    alertas.append((fuente, resultado))
        return alertas

    # ---------- recursividad ----------
    def analizar_muestras(self, lista, posicion=0):
        """Recorre el historial de forma recursiva.
        Caso base: no quedan muestras. Caso recursivo: analiza la muestra
        actual y se llama con posicion + 1."""
        if posicion >= len(lista):
            return []
        actual = Monitoreo(lista[posicion], self.factores)
        return [actual] + self.analizar_muestras(lista, posicion + 1)

    def contar_no_aptas(self, resultados, posicion=0):
        """Cuenta recursivamente cuántos resultados no son aptos."""
        if posicion >= len(resultados):
            return 0
        actual = 0 if resultados[posicion].apto else 1
        return actual + self.contar_no_aptas(resultados, posicion + 1)
