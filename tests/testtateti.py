
import unittest
from tateti import Tateti
from excepciones import PosOcupadaException

class TestTateti(unittest.TestCase):
    def setUp(self):
        self.j = Tateti()

    def test_flujo_basico_turnos(self):
        self.assertEqual(self.j.turno, "X")
        self.j.ocupar_una_de_las_casillas(0,0)
        self.assertEqual(self.j.turno, "O")
        self.j.ocupar_una_de_las_casillas(1,1)
        self.assertEqual(self.j.turno, "X")

    def test_gana_fila(self):
        self.j.ocupar_una_de_las_casillas(0,0)  
        self.j.ocupar_una_de_las_casillas(1,0)  
        self.j.ocupar_una_de_las_casillas(0,1)  
        self.j.ocupar_una_de_las_casillas(1,1)  
        self.j.ocupar_una_de_las_casillas(0,2)  
        self.assertTrue(self.j.finalizado)
        self.assertEqual(self.j.ganador, "X")
        self.assertIn("Ganó X", self.j.estado())

    def test_empate(self):
        
        seq = [
            (0,0), (1,1), (2,2),
            (0,2), (0,1),
            (2,1), (1,2),
            (1,0), (2,0),
        ]
        for r,c in seq:
            self.j.ocupar_una_de_las_casillas(r,c)
        self.assertTrue(self.j.finalizado)
        self.assertIsNone(self.j.ganador)
        self.assertEqual(self.j.estado(), "Empate")

    def test_no_permite_jugar_sobre_ocupada(self):
        self.j.ocupar_una_de_las_casillas(0,0)
        with self.assertRaises(PosOcupadaException):
            self.j.ocupar_una_de_las_casillas(0,0)

if __name__ == "__main__":
    unittest.main()
