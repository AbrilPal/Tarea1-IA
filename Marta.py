# Andrea aAbril Palencia Gutierrez, 18198
# Inteligencia Artificial - Tarea 1
# 06/02/2021

# valor de las casillas
valor_casillas = [[10, 9, 9, 9, 9, -1, -2, -3, -4, -5],
                  [9, 8, 7, 6, -1, -2, -3, -4, -5, -6],
                  [9, 7, 6, -1, -2, -3, -4, -5, -6, -7],
                  [9, 6, -1, -2, -3, -4, -5, -6, -7, -8],
                  [9, -1, -2, -3, -4, -5, -6, -7, -8, -9],
                  [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],
                  [-2, -3, -4, -5, -6, -7, -8, -9, -10, -11],
                  [-3, -4, -5, -6, -7, -8, -9, -10, -11, -11],
                  [-4, -5, -6, -7, -8, -9, -10, -11, -11, -12],
                  [-6, -6, -7, -8, -9, -10, -11, -11, -12, -13],
]

def minimax(tablero, profundidad, esMax, alpha = -1000, beta = 1000):
    if (profundidad == 0):
        return (evaluar(tablero, 2), None)
    else: 
        mejor_valor = 0 
        mejor_movimiento = 0
        if (esMax == True):
            mejor_valor = -1000
            turno_j = 'm'
            movimientos = posible_jugada(tablero, turno_j)
        else:
            mejor_valor = 1000
            turno_j = 'j'
            movimientos = posible_jugada(tablero, turno_j)

        for a in range(len(movimientos)):
            # print("hola")
            jugadas_por_ficha = movimientos[a]
            # print(jugadas_por_ficha)
            for b in range(len(jugadas_por_ficha)):
                inicio = jugadas_por_ficha[0]
                jugadas = jugadas_por_ficha[1]
            for c in range(len(jugadas)):
                # print(inicio, jugadas[c])
                jugada = jugadas[c]
                # print(jugada)
                for y in range(len(inicio)):
                    # mover la ficha 
                    y_inicial = inicio[0]
                    x_inicial = inicio[1]
                # cambiar el estado de la celda
                tablero[y_inicial][x_inicial] = '-'
                # print(tablero[y][x])
                for x in range(len(jugada)):
                    y = jugada[0]
                    x = jugada[1]
                tablero[y][x] = turno_j
                # print(tablero[y][x])
                # print(tablero[y][x])

                valor, movimiento = minimax(tablero, profundidad-1, False)

                tablero[y_inicial][x_inicial] = turno_j
                tablero[y][x] = '-'

                if (esMax == True and valor > mejor_valor):
                    mejor_valor = valor
                    mejor_movimiento = [inicio,jugada]
                    alpha = max(alpha, valor)
                if (esMax == True and valor < mejor_valor):
                    mejor_valor = valor
                    mejor_movimiento = [inicio,jugada]
                    beta = min(beta, valor)
                
                if (beta <= alpha):
                    return mejor_valor, mejor_movimiento

        return mejor_valor, mejor_movimiento
            # print(inicio, jugadas)

def evaluar(tablero, jugador_pieza):
    resultado = 0
    if (jugador_pieza == 2):
        for i in range(len(tablero[0])):
            for j in range(len(tablero)):
                if (tablero[i][j] == 'j'):
                    valor = valor_casillas[i][j]
                    resultado = valor + resultado
        return resultado
    if (jugador_pieza == 1):
        for i in range(len(tablero[0])):
            for j in range(len(tablero)):
                if (tablero[i][j] == 'm'):
                    valor = valor_casillas[i][j]
                    resultado = valor + resultado
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
                            # print("j: ", j+2)
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
    # print(arreglo_jugadas)
    return arreglo_jugadas

# posible_jugada(tablero, jugador)
# print(evaluar(tablero, 1))
# minimax(tablero, 3, True)
