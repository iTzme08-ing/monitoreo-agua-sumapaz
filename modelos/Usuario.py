class Usuario:
    """Usuario del sistema; los permisos dependen de su rol."""

    PERMISOS = {
        "funcionario": {"registrar_fuente", "registrar_muestra", "consultar", "historial", "alertas"},
        "responsable": {"registrar_muestra", "consultar", "alertas"},
        "comunidad": {"consultar", "alertas"},
        "administrador": {"registrar_fuente", "registrar_muestra", "consultar",
                          "historial", "alertas"},
    }

    def __init__(self, id_usuario, nombre, rol):
        if rol not in self.PERMISOS:
            raise ValueError(f"Rol no válido. Opciones: {', '.join(self.PERMISOS)}")
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.rol = rol

    def puede(self, accion):
        return accion in self.PERMISOS[self.rol]

    def __str__(self):
        return f"{self.nombre} ({self.rol})"
