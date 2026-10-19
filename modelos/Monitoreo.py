class Monitoreo:
    """Resultado de evaluar una muestra contra los factores de contaminación."""

    def __init__(self, muestra, factores):
        self.muestra = muestra
        self.incumplidos = []    # lista de (factor, valor medido)
        self.no_evaluados = []   # parámetros sin medición en la muestra
        for factor in factores:
            valor = muestra.obtener(factor.nombre)
            if valor is None:
                self.no_evaluados.append(factor.nombre)
            elif not factor.evaluar(valor):
                self.incumplidos.append((factor, valor))

    @property
    def apto(self):
        return not self.incumplidos and not self.no_evaluados

    @property
    def estado(self):
        if self.incumplidos:
            return "NO APTA"
        if self.no_evaluados:
            return "INCOMPLETA"
        return "APTA"

    def resumen(self):
        lineas = [f"{self.muestra} -> {self.estado}"]
        for factor, valor in self.incumplidos:
            lineas.append(f"   x {factor.nombre}: {valor} (permitido {factor.rango_texto()})")
        for nombre in self.no_evaluados:
            lineas.append(f"   ? {nombre}: sin medición")
        return "\n".join(lineas)
