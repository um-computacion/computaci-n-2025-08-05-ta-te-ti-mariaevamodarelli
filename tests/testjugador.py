import unittest
from jugador import Jugador

class TestJugador(unittest.TestCase):
    def test_creacion_jugador(self):
        j = Jugador("Ana", "X")
        self.assertEqual(str(j), "Ana")
        self.assertEqual(j.ficha, "X")

    def test_ficha_invalida(self):
        with self.assertRaises(ValueError):
            Jugador("Beto", "Z")

if __name__ == "__main__":
    unittest.main()
