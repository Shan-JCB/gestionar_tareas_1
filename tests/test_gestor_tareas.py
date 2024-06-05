import unittest
from src.logica.gestor_tareas import GestorTareas

class TestGestorTareas(unittest.TestCase):
    def setUp(self):
        self.gestor = GestorTareas()

        with self.assertRaises(ValueError):
            self.gestor.agregar_tarea("", "Descripción")

    def test_ver_tareas_vacio(self):
        self.assertEqual(self.gestor.ver_tareas(), [])


if __name__ == "__main__":
    unittest.main()