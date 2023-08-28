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

# Pedir el nombre del jugador por teclado
nombre_jugador = input("Ingrese su nombre: ")

# Imprimir mensaje de bienvenida con el nombre
print(f"Bienvenido/a, {nombre_jugador}!Hora de jugar")

print("Mueve al personaje con las teclas direccionales o presiona 'q' para salir:")

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
            laberinto[fila] = laberinto[fila][:columna] + "." + laberinto[fila][columna+1:]
            laberinto[nueva_fila] = laberinto[nueva_fila][:columna] + "P" + laberinto[nueva_fila][columna+1:]
            posicion_personaje = (nueva_fila, columna)
    elif direccion == "↓":
        nueva_fila = fila + 1
        if laberinto[nueva_fila][columna] != "#":
            laberinto[fila] = laberinto[fila][:columna] + "." + laberinto[fila][columna+1:]
            laberinto[nueva_fila] = laberinto[nueva_fila][:columna] + "P" + laberinto[nueva_fila][columna+1:]
            posicion_personaje = (nueva_fila, columna)
    elif direccion == "←":
        nueva_columna = columna - 1
        if laberinto[fila][nueva_columna] != "#":
            laberinto[fila] = laberinto[fila][:columna] + "." + laberinto[fila][columna+1:]
            laberinto[fila] = laberinto[fila][:nueva_columna] + "P" + laberinto[fila][nueva_columna+1:]
            posicion_personaje = (fila, nueva_columna)
    elif direccion == "→":
        nueva_columna = columna + 1
        if laberinto[fila][nueva_columna] != "#":
            laberinto[fila] = laberinto[fila][:columna] + "." + laberinto[fila][columna+1:]
            laberinto[fila] = laberinto[fila][:nueva_columna] + "P" + laberinto[fila][nueva_columna+1:]
            posicion_personaje = (fila, nueva_columna)


# Ciclo del juego
while True:
    imprimir_laberinto()
    direccion = input()

    mover_personaje(direccion)

    if direccion == "q":
        break


    # Limpiar la pantalla
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
