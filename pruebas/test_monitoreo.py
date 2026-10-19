import unittest

from modelos.FactorContaminacion import FactorContaminacion, factores_por_defecto
from modelos.FuenteAgua import FuenteAgua
from modelos.Monitoreo import Monitoreo
from modelos.MuestraAgua import MuestraAgua
from modelos.Usuario import Usuario
from servicios.SistemaMonitoreo import SistemaMonitoreo
from main import acciones_disponibles

BUENA = {"pH": 7.2, "Turbidez": 1.0, "Cloro residual libre": 0.8,
         "Coliformes totales": 0, "E. coli": 0}
MALA = {"pH": 5.0, "Turbidez": 6.0, "Cloro residual libre": 0.8,
        "Coliformes totales": 3, "E. coli": 1}


class TestFactor(unittest.TestCase):
    def test_rango(self):
        ph = FactorContaminacion("pH", "", 6.5, 9.0)
        self.assertTrue(ph.evaluar(7))
        self.assertFalse(ph.evaluar(6.0))
        self.assertFalse(ph.evaluar(9.5))

    def test_sin_limites(self):
        with self.assertRaises(ValueError):
            FactorContaminacion("x", "u")


class TestMonitoreo(unittest.TestCase):
    def test_apta(self):
        m = Monitoreo(MuestraAgua(1, 1, BUENA), factores_por_defecto())
        self.assertTrue(m.apto)
        self.assertEqual(m.estado, "APTA")

    def test_no_apta(self):
        m = Monitoreo(MuestraAgua(1, 1, MALA), factores_por_defecto())
        self.assertEqual(m.estado, "NO APTA")
        self.assertEqual(len(m.incumplidos), 4)

    def test_incompleta(self):
        m = Monitoreo(MuestraAgua(1, 1, {"pH": 7}), factores_por_defecto())
        self.assertEqual(m.estado, "INCOMPLETA")


class TestSistema(unittest.TestCase):
    def setUp(self):
        self.s = SistemaMonitoreo()
        self.func = Usuario(1, "Ana", "funcionario")
        self.com = Usuario(2, "Luis", "comunidad")
        self.s.registrar_fuente(self.func, FuenteAgua(1, "La Playa", "Nazareth"))

    def test_permisos(self):
        with self.assertRaises(PermissionError):
            self.s.registrar_fuente(self.com, FuenteAgua(2, "X", "Y"))

    def test_fuente_duplicada(self):
        with self.assertRaises(ValueError):
            self.s.registrar_fuente(self.func, FuenteAgua(1, "Otra", "Y"))

    def test_recursividad_historial(self):
        for i, datos in enumerate([BUENA, MALA, BUENA, MALA, MALA], 1):
            self.s.registrar_muestra(self.func, MuestraAgua(i, 1, datos))
        resultados = self.s.historial(self.func, 1)
        self.assertEqual(len(resultados), 5)
        self.assertEqual(self.s.contar_no_aptas(resultados), 3)

    def test_caso_base_lista_vacia(self):
        self.assertEqual(self.s.analizar_muestras([]), [])

    def test_alertas(self):
        self.s.registrar_muestra(self.func, MuestraAgua(1, 1, MALA))
        alertas = self.s.generar_alertas(self.com)
        self.assertEqual(len(alertas), 1)

    def test_estado_sin_muestras(self):
        self.assertIsNone(self.s.consultar_estado(self.com, 1))


class TestMenuPorRol(unittest.TestCase):
    def test_responsable_no_ve_registrar_fuente(self):
        textos = [a[0] for a in acciones_disponibles(Usuario(1, "Rosa", "responsable"))]
        self.assertNotIn("Registrar fuente", textos)
        self.assertIn("Registrar muestra", textos)

    def test_funcionario_ve_registrar_fuente(self):
        textos = [a[0] for a in acciones_disponibles(Usuario(1, "Ana", "funcionario"))]
        self.assertIn("Registrar fuente", textos)


if __name__ == "__main__":
    unittest.main()
