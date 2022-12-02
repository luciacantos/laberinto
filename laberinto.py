def laberinto(dimension, muros):
    #creamos lista
    laberinto = []

    for i in range(dimension):
        fila = []
        for j in range(dimension):
            fila.append(" ")
            laberinto.append(fila)

    for muro in muros:
        laberinto[muro[0]][muro[1]] = "X"

        laberinto[dimension-1][dimension-1] = "S"

        return laberinto
