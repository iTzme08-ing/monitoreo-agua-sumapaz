  from modelos.FuenteAgua import FuenteAgua
from modelos.MuestraAgua import MuestraAgua
from modelos.Usuario import Usuario
from servicios.SistemaMonitoreo import SistemaMonitoreo


def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Este campo es obligatorio.")


def pedir_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje).replace(",", "."))
            if valor >= 0:
                return valor
            print("El valor no puede ser negativo.")
        except ValueError:
            print("Ingrese un número válido.")


def elegir_usuario():
    roles = list(Usuario.PERMISOS)
    print("=== Monitoreo de calidad del agua - Sumapaz ===")
    for i, rol in enumerate(roles, 1):
        print(f"{i}. {rol}")
    while True:
        opcion = input("Seleccione su rol: ").strip()
        if opcion.isdigit() and 1 <= int(opcion) <= len(roles):
            nombre = pedir_texto("Su nombre: ")
            return Usuario(1, nombre, roles[int(opcion) - 1])
        print("Opción no válida.")


def listar_fuentes(sistema):
    if not sistema.fuentes:
        print("No hay fuentes registradas.")
        return False
    for fuente in sistema.fuentes.values():
        print(" ", fuente)
    return True


def registrar_fuente(sistema, usuario):
    id_fuente = int(pedir_numero("Id de la fuente (número): "))
    nombre = pedir_texto("Nombre: ")
    vereda = pedir_texto("Vereda: ")
    print("Tipos:", ", ".join(FuenteAgua.TIPOS))
    tipo = pedir_texto("Tipo: ").lower()
    sistema.registrar_fuente(usuario, FuenteAgua(id_fuente, nombre, vereda, tipo))
    print("Fuente registrada.")


def registrar_muestra(sistema, usuario):
    if not listar_fuentes(sistema):
        return
    id_fuente = int(pedir_numero("Id de la fuente: "))
    sistema.obtener_fuente(id_fuente)
    mediciones = {}
    for factor in sistema.factores:
        mediciones[factor.nombre] = pedir_numero(f"{factor} -> valor medido: ")
    id_muestra = sum(len(f.muestras) for f in sistema.fuentes.values()) + 1
    sistema.registrar_muestra(usuario, MuestraAgua(id_muestra, id_fuente, mediciones))
    print("Muestra registrada.")


def consultar_estado(sistema, usuario):
    if not listar_fuentes(sistema):
        return
    id_fuente = int(pedir_numero("Id de la fuente: "))
    resultado = sistema.consultar_estado(usuario, id_fuente)
    print(resultado.resumen() if resultado else "La fuente aún no tiene muestras.")


def ver_historial(sistema, usuario):
    if not listar_fuentes(sistema):
        return
    id_fuente = int(pedir_numero("Id de la fuente: "))
    resultados = sistema.historial(usuario, id_fuente)
    if not resultados:
        print("La fuente aún no tiene muestras.")
        return
    for r in resultados:
        print(r.resumen())
    print(f"Muestras no aptas: {sistema.contar_no_aptas(resultados)} de {len(resultados)}")


def ver_alertas(sistema, usuario):
    alertas = sistema.generar_alertas(usuario)
    if not alertas:
        print("Sin alertas: todas las fuentes con muestras están aptas.")
    for fuente, resultado in alertas:
        print(f"ALERTA - {fuente}\n{resultado.resumen()}")


ACCIONES = [
    ("Registrar fuente", registrar_fuente, "registrar_fuente"),
    ("Registrar muestra", registrar_muestra, "registrar_muestra"),
    ("Consultar estado de una fuente", consultar_estado, "consultar"),
    ("Ver historial (recursivo)", ver_historial, "historial"),
    ("Ver alertas", ver_alertas, "alertas"),
]


def acciones_disponibles(usuario):
    """Solo las acciones que el rol del usuario tiene permitidas."""
    return [a for a in ACCIONES if usuario.puede(a[2])]


def main():
    sistema = SistemaMonitoreo()
    usuario = elegir_usuario()
    disponibles = acciones_disponibles(usuario)
    while True:
        print(f"\n--- Menú ({usuario}) ---")
        for numero, (texto, _, _) in enumerate(disponibles, 1):
            print(f"{numero}. {texto}")
        print("0. Salir")
        opcion = input("Opción: ").strip()
        if opcion == "0":
            print("Hasta luego.")
            break
        if not (opcion.isdigit() and 1 <= int(opcion) <= len(disponibles)):
            print("Opción no válida.")
            continue
        _, funcion, _ = disponibles[int(opcion) - 1]
        try:
            funcion(sistema, usuario)
        except (PermissionError, ValueError, KeyError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()