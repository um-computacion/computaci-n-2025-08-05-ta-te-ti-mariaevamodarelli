from tateti import Tateti

class Jugador:
    def __init__(self, nombre: str, ficha: str = "X"):
        if ficha not in ("X", "O"):
            raise ValueError("La ficha debe ser 'X' u 'O'")
        self.nombre = nombre
        self.ficha = ficha

    def jugar(self):
        self.tateti.ocupar_una_de_las_casillas(1, 1)        
        self.tateti.ocupar_una_de_las_casillas(2, 1)
        self.tateti.ocupar_una_de_las_casillas(3, 1)
        self.tateti.ocupar_una_de_las_casillas(4, 1)
        self.tateti.ocupar_una_de_las_casillas(5, 1)
        self.tateti.ocupar_una_de_las_casillas(6, 1)
        self.tateti.ocupar_una_de_las_casillas(7, 1)
        self.tateti.ocupar_una_de_las_casillas(8, 1)                

    def __str__(self):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        return self.nombre                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      