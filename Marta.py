# Andrea aAbril Palencia Gutierrez, 18198
# Inteligencia Artificial - Tarea 1
# 06/02/2021

# valor de las casillas
valor_casillas = [[10, 9, 8, 7, 6, 5, 4, 3, 2, -1],
                  [9, 8, 7, 6, 5, 4, 3, 2, 1, -1],
                  [8, 7, 6, 5, 4, 3, 2, 1, -1, -2],
                  [7, 6, 5, 4, 3, 2, 1, -1, -2, -3],
                  [6, 5, 4, 3, 2, 1, -1, -2, -3, -4],
                  [5, 4, 3, 2, 1, -1, -2, -3, -4, -5],
                  [4, 3, 2, 1, -1, -2, -3, -4, -5, -6],
                  [3, 2, 1, -1, -2, -3, -4, -5, -6, -7],
                  [2, 1, -1, -2, -3, -4, -5, -6, -7, -8],
                  [1, -1, -2, -3, -4, -5, -6, -7, -8, -9],
]

# Tablero inicial
jugador = "j"
marta = "m"
vacio = "-"

tablero = [[jugador, jugador, jugador, jugador, jugador, vacio, vacio, vacio, vacio, vacio],
            [jugador, jugador, jugador, jugador, vacio, vacio, vacio, vacio, vacio, vacio],
            [jugador, jugador, vacio, vacio, vacio, vacio, vacio, vacio, vacio, vacio],
            [vacio, jugador, jugador, vacio, vacio, vacio, vacio, vacio, vacio, vacio],
            [jugador, vacio, vacio, vacio, vacio, vacio, vacio, vacio, vacio, vacio],
            [vacio, vacio, vacio, vacio, vacio, vacio, vacio, marta, vacio, marta],
            [vacio, vacio, vacio, vacio, vacio, vacio, vacio, vacio, jugador, marta],
            [vacio, vacio, vacio, vacio, vacio, vacio, vacio, marta, marta, marta],
            [vacio, vacio, vacio, vacio, vacio, vacio, marta, marta, marta, marta],
            [vacio, vacio, vacio, vacio, vacio, marta, marta, marta, marta, marta],
]


def minimax(tablero, profundidad, esMax = True, alpha = -1000, beta = 1000):
    if (profundidad == 0):
        return(evaluar(i, j))
    if (esMax == True):
        mejor_valor = -1000
        movimientos = posible_jugada(tablero, marta)
        return movimientos
    else:
        mejor_valor = 1000
        movimientos = posible_jugada(tablero, jugador)
        movimientos
    
    

def evaluar(i, j):
    valor = valor_casillas[i][j]
    resultado = 1 + valor
    return resultado

def posible_jugada(tablero, turno):
    arreglo_jugadas = []
    for i in range(len(tablero[0])):
        for j in range(len(tablero)):
            desde = [i,j]
            hasta = []
            if (tablero[i][j] == turno):
                # print(tablero[i][j])
                # verificar si a su alrededor hay espacio vacio y si no si el siguen te esta vacio para saltar
                # lados
                if (j-1 >= 0 and j-1 <= 9):
                    if (tablero[i][abs(j-1)] == '-'):
                        hasta.append([i,abs(j-1)])
                    else:
                        if (j-2 >= 0 and j-2 <= 9):
                            if (tablero[i][abs(j-2)] == '-'):
                                hasta.append([i,abs(j-2)])

                if (j+1 >= 0 and j+1 <= 9):
                    if (tablero[i][abs(j+1)] == '-'):
                        hasta.append([i,abs(j+1)])
                    else:
                        if (j+2 >= 0 and j+2 <= 9):
                            print("j: ", j+2)
                            if (tablero[i][j+2] == '-'):
                                hasta.append([i,j+2])

                if (i-1 >= 0 and i-1 <= 9):
                    if (tablero[abs(i-1)][j] == '-'):
                        hasta.append([abs(i-1),j])
                    else:
                        if (i-2 >= 0 and i-2 <= 9):
                            if (tablero[abs(i-2)][j] == '-'):
                                hasta.append([abs(i-2),j])

                if (i+1 >= 0 and i+1 <= 9):
                    if (tablero[abs(i+1)][j] == '-'):
                        hasta.append([abs(i+1),j])
                    else:
                        if (i+2 >= 0 and i+2 <= 9):
                            if (tablero[abs(i+2)][j] == '-'):
                                hasta.append([abs(i+2),j])

                # diagonales
                if (i-1 >= 0 and i-1 <= 9):
                    if (j-1 >= 0 and j-1 <= 9):
                        if (tablero[abs(i-1)][abs(j-1)] == '-'):
                            hasta.append([abs(i-1),abs(j-1)])
                        else:
                            if (i-2 >= 0 and i-2 <= 9):
                                if (j-2 >= 0 and j-2 <= 9):
                                    if (tablero[abs(i-2)][abs(j-2)] == '-'):
                                        hasta.append([abs(i-2),abs(j-2)])
                
                if (i+1 >= 0 and i+1 <=9):
                    if (j+1 >= 0 and j+1 <= 9):
                        if (tablero[abs(i+1)][abs(j+1)] == '-'):
                            hasta.append([abs(i+1),abs(j+1)])
                        else:
                            if (i+2 >= 0 and i+2 <=9):
                                if (j+2 >= 0 and j+2 <= 9):
                                    if (tablero[abs(i+2)][abs(j+2)] == '-'):
                                        hasta.append([abs(i+2),abs(j+2)])
                if (i+1 >= 0 and i+1 <= 9):
                    if (j-1 >= 0 and j-1 <= 9):
                        if (tablero[abs(i+1)][abs(j-1)] == '-'):
                            hasta.append([abs(i+1),abs(j-1)])
                        else:
                            if (i+2 >= 0 and i+2 <= 9):
                                if (j-2 >= 0 and j-2 <= 9):
                                    if (tablero[abs(i+2)][abs(j-2)] == '-'):
                                        hasta.append([abs(i+2),abs(j-2)])
                if (i-1 >= 0 and i-1 <= 9):
                    if (j+1 >= 0 and j+1 <= 9):
                        if (tablero[abs(i-1)][abs(j+1)] == '-'):
                            hasta.append([abs(i-1),abs(j+1)])
                        else:
                            if (i-2 >= 0 and i-2 <= 9):
                                if (j+2 >= 0 and j+2 <= 9):
                                    if (tablero[abs(i-2)][abs(j+2)] == '-'):
                                        hasta.append([abs(i-2),abs(j+2)])
            # hasta([i,j], [i,j], [i,j], [i,j], [i,j], [i,j])
            if not (hasta == []):
                arreglo_jugadas.append([desde,hasta])
    print(arreglo_jugadas)
    return arreglo_jugadas

posible_jugada(tablero, jugador)
# print(evaluar(8, 8, marta))
# print(minimax(tablero, 3))
