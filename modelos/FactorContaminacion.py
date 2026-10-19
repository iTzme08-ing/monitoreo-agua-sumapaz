class FactorContaminacion:
    """Parámetro de calidad del agua con su rango permitido."""

    def __init__(self, nombre, unidad, minimo=None, maximo=None):
        if minimo is None and maximo is None:
            raise ValueError("Debe definir al menos un límite (mínimo o máximo).")
        if minimo is not None and maximo is not None and minimo > maximo:
            raise ValueError("El mínimo no puede ser mayor que el máximo.")
        self.nombre = nombre
        self.unidad = unidad
        self.minimo = minimo
        self.maximo = maximo

    def evaluar(self, valor):
        """Devuelve True si el valor está dentro del rango permitido."""
        if self.minimo is not None and valor < self.minimo:
            return False
        if self.maximo is not None and valor > self.maximo:
            return False
        return True

    def rango_texto(self):
        if self.minimo is not None and self.maximo is not None:
            return f"{self.minimo} - {self.maximo} {self.unidad}".strip()
        if self.maximo is not None:
            return f"<= {self.maximo} {self.unidad}".strip()
        return f">= {self.minimo} {self.unidad}".strip()

    def __str__(self):
        return f"{self.nombre} ({self.rango_texto()})"


def factores_por_defecto():
    """Valores de referencia para agua de consumo humano.
    Verifica los límites con la norma vigente (Resolución 2115 de 2007)
    antes de la entrega."""
    return [
        FactorContaminacion("pH", "", minimo=6.5, maximo=9.0),
        FactorContaminacion("Turbidez", "NTU", maximo=2.0),
        FactorContaminacion("Cloro residual libre", "mg/L", minimo=0.3, maximo=2.0),
        FactorContaminacion("Coliformes totales", "UFC/100 mL", maximo=0),
        FactorContaminacion("E. coli", "UFC/100 mL", maximo=0),
    ]
