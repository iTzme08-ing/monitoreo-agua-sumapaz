class Usuario:
    def __init__(self, nombre, rol):
        self.__nombre = nombre
        self.__rol = rol

    # Getters
    def getNombre(self):
        return self.__nombre

    def getRol(self):
        return self.__rol