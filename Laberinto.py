# Establecer el formato del laberinto
laberinto = [
    "#P#...#####",
    "#...#.....#",
    "#.#####...#",
    "#.......###",
    "#.#####.###",
    "#...#.....#",
    "#..###....#",
    "######.####",
    "######. Fin",
    " "
]

# Coordenadas del personaje
posicion_personaje = (1, 1)

# Imprimir laberinto
def imprimir_laberinto():
    for fila in laberinto:
        print(fila)

# Función para mover al personaje
def mover_personaje(direccion):
    global posicion_personaje

    fila, columna = posicion_personaje

    if direccion == "↑":
        nueva_fila = fila - 1
        if laberinto[nueva_fila][columna] != "#":
            posicion_personaje = (nueva_fila, columna)
    elif direccion == "↓":
        nueva_fila = fila + 1
        if laberinto[nueva_fila][columna] != "#":
            posicion_personaje = (nueva_fila, columna)
    elif direccion == "←":
        nueva_columna = columna - 1
        if laberinto[fila][nueva_columna] != "#":
            posicion_personaje = (fila, nueva_columna)
    elif direccion == "→":
        nueva_columna = columna + 1
        if laberinto[fila][nueva_columna] != "#":
            posicion_personaje = (fila, nueva_columna)

# Pedir el nombre del jugador por teclado
nombre_jugador = input("Ingrese su nombre: ")

# Imprimir mensaje de bienvenida con el nombre
print(f"Bienvenido/a, {nombre_jugador}!Hora de jugar")

# Ciclo del juego
while True:
    imprimir_laberinto()
    print("Mueve al personaje con las teclas direccionales o presiona 'q' para salir:")
    direccion = input()

    if direccion == "q":
        break

    mover_personaje(direccion)

    # Limpiar la pantalla
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
