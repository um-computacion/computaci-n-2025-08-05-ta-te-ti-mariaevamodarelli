from tateti import Tateti
from excepciones import PosOcupadaException, PosInexistenteException

QUIT = object()  

def dibujar_tablero(juego: Tateti):
    g = juego.tablero.contenedor
    print("\n    1   2   3")
    print("  ┌───┬───┬───┐")
    for i, fila in enumerate(g, start=1):
        c = [(x if x else " ") for x in fila]
        print(f"{i} │ {c[0]} │ {c[1]} │ {c[2]} │")
        if i < 3:
            print("  ├───┼───┼───┤")
    print("  └───┴───┴───┘")

def pedir_indice(nombre: str):

    while True:
        dato = input(f"Ingrese {nombre} (1-3, o 'q' para salir): ").strip()
        if dato.lower() == "q":
            return QUIT
        try:
            num = int(dato)
        except ValueError:
            print("⚠️  Ingrese solo números (1 a 3), o 'q' para salir.")
            continue
        if not (1 <= num <= 3):
            print("⚠️  Valor fuera de rango. Debe ser 1, 2 o 3.")
            continue
        return num - 1  

def main():
    print("Bienvenidos al Ta-Te-Ti")
    print("Tip: en cualquier momento podés escribir 'q' para salir.")
    juego = Tateti()

    while not juego.finalizado:
        dibujar_tablero(juego)
        print(f"Turno de {juego.turno}")

        fil = pedir_indice("fila")
        if fil is QUIT:
            print("Saliste del juego.")
            return  

        col = pedir_indice("columna")
        if col is QUIT:
            print("Saliste del juego.")
            return

        try:
            juego.ocupar_una_de_las_casillas(fil, col)
        except PosOcupadaException:
            print("Esa casilla ya está ocupada. Elegí otra.")
        except PosInexistenteException:
            print("Posición inexistente (fuera del tablero).")
        except Exception as e:
            print(f"Error inesperado: {e}")

   
    dibujar_tablero(juego)
    print(juego.estado())

if __name__ == "__main__":
    main()
