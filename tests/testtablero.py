
import unittest
from tablero import Tablero
from excepciones import PosOcupadaException, PosInexistenteException


class TestTablero(unittest.TestCase):
    def setUp(self):
        self.t = Tablero()

    def test_inicio_vacio(self):
        self.assertTrue(all(c == "" for fila in self.t.contenedor for c in fila))

    def test_poner_ficha_valida(self):
        self.t.poner_la_ficha(0, 0, "X")
        self.assertEqual(self.t.contenedor[0][0], "X")

    def test_pos_inexistente(self):
        with self.assertRaises(PosInexistenteException):
            self.t.poner_la_ficha(3, 0, "X")
        with self.assertRaises(PosInexistenteException):
            self.t.casillero_libre(-1, 0)

    def test_pos_ocupada(self):
        self.t.poner_la_ficha(1, 1, "X")
        with self.assertRaises(PosOcupadaException):
            self.t.poner_la_ficha(1, 1, "O")

    def test_hay_linea_con(self):
        for j in range(3):
            self.t.poner_la_ficha(0, j, "X")
        self.assertTrue(self.t.hay_linea_con("X"))
        self.assertFalse(self.t.hay_linea_con("O"))

    def test_lleno(self):
        ficha = "X"
        for i in range(3):
            for j in range(3):
                self.t.poner_la_ficha(i, j, ficha)
                ficha = "O" if ficha == "X" else "X"
        self.assertTrue(self.t.lleno())

if __name__ == "__main__":
    unittest.main()
