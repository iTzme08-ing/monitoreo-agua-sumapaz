from datetime import date


class MuestraAgua:
    """Muestra tomada en una fuente, con sus mediciones por parámetro."""

    def __init__(self, id_muestra, id_fuente, mediciones, fecha=None):
        if not isinstance(mediciones, dict) or not mediciones:
            raise ValueError("La muestra debe tener al menos una medición.")
        for nombre, valor in mediciones.items():
            if not isinstance(valor, (int, float)) or valor < 0:
                raise ValueError(f"Valor inválido para '{nombre}': {valor}")
        self.id_muestra = id_muestra
        self.id_fuente = id_fuente
        self.mediciones = dict(mediciones)
        self.fecha = fecha or date.today()

    def obtener(self, nombre_factor):
        """Valor medido del parámetro, o None si no se midió."""
        return self.mediciones.get(nombre_factor)

    def __str__(self):
        return f"Muestra {self.id_muestra} ({self.fecha})"
