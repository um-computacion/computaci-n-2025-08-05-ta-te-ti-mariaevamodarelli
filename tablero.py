
from excepciones import PosOcupadaException, PosInexistenteException

class Tablero:
    TAM = 3

    def __init__(self):
        
        self.contenedor = [["" for _ in range(self.TAM)] for _ in range(self.TAM)]

    def _validar_indices(self, fil: int, col: int):
        if not (0 <= fil < self.TAM and 0 <= col < self.TAM):
            raise PosInexistenteException(f"Posición inexistente: ({fil}, {col})")

    def poner_la_ficha(self, fil: int, col: int, ficha: str):
        
        self._validar_indices(fil, col)
        if self.contenedor[fil][col] != "":
            raise PosOcupadaException(f"La posición ({fil}, {col}) ya está ocupada.")
        self.contenedor[fil][col] = ficha

    def casillero_libre(self, fil: int, col: int) -> bool:
        self._validar_indices(fil, col)
        return self.contenedor[fil][col] == ""

    def lleno(self) -> bool:
        return all(c != "" for fila in self.contenedor for c in fila)

    def hay_linea_con(self, ficha: str) -> bool:
        
        g = self.contenedor
        # filas
        for i in range(self.TAM):
            if all(g[i][j] == ficha for j in range(self.TAM)):
                return True
        # columnas
        for j in range(self.TAM):
            if all(g[i][j] == ficha for i in range(self.TAM)):
                return True
        # diagonales
        if all(g[i][i] == ficha for i in range(self.TAM)):
            return True
        if all(g[i][self.TAM-1-i] == ficha for i in range(self.TAM)):
            return True
        return False

    def __str__(self) -> str:
        
        filas = []
        for i in range(self.TAM):
            filas.append("|".join(c if c else " " for c in self.contenedor[i]))
        return "\n-+-+-\n".join(filas)
