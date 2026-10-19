class FuenteAgua:
    """Fuente hídrica de una vereda de Sumapaz con su historial de muestras."""

    TIPOS = ("quebrada", "nacimiento", "rio", "pozo", "acueducto veredal")

    def __init__(self, id_fuente, nombre, vereda, tipo="quebrada"):
        if not nombre.strip() or not vereda.strip():
            raise ValueError("Nombre y vereda son obligatorios.")
        if tipo not in self.TIPOS:
            raise ValueError(f"Tipo no válido. Opciones: {', '.join(self.TIPOS)}")
        self.id_fuente = id_fuente
        self.nombre = nombre.strip()
        self.vereda = vereda.strip()
        self.tipo = tipo
        self.muestras = []

    def agregar_muestra(self, muestra):
        if muestra.id_fuente != self.id_fuente:
            raise ValueError("La muestra pertenece a otra fuente.")
        self.muestras.append(muestra)

    def ultima_muestra(self):
        return self.muestras[-1] if self.muestras else None

    def __str__(self):
        return f"[{self.id_fuente}] {self.nombre} - {self.tipo}, vereda {self.vereda}"
