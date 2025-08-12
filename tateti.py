
from tablero import Tablero
from excepciones import PosOcupadaException, PosInexistenteException

class Tateti:
    def __init__(self):
        self.tablero = Tablero()
        self.turno = "X"
        self.ganador = None
        self.finalizado = False

    def _cambiar_turno(self):
        self.turno = "O" if self.turno == "X" else "X"

    def ocupar_una_de_las_casillas(self, fil: int, col: int):
       
        if self.finalizado:
            return  
        self.tablero.poner_la_ficha(fil, col, self.turno)
        
        if self.tablero.hay_linea_con(self.turno):
            self.ganador = self.turno
            self.finalizado = True
            return
        
        if self.tablero.lleno():
            self.finalizado = True
            return
        
        self._cambiar_turno()

    def estado(self) -> str:
        if self.ganador:
            return f"Ganó {self.ganador}"
        if self.finalizado:
            return "Empate"
        return f"Turno de {self.turno}"