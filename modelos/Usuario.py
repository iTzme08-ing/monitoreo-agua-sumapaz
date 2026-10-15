class Usuario:
    def __init__(self, nombre, rol):
        self.__nombre = nombre
        self.__rol = rol

    # Getters
    def getNombre(self):
        return self.__nombre

    def getRol(self):
        return self.__rol

    # Setters
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setRol(self, rol):
        self.__rol = rol

    # Métodos de consulta
    def consultarFuente(self, fuentes):
        if not fuentes:
            return "No hay fuentes de agua registradas."
        return fuentes