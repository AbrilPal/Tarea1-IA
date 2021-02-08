# Andrea aAbril Palencia Gutierrez, 18198
# Inteligencia Artificial - Tarea 1
# 06/02/2021

# importamos a marta
from Marta import * 

# Tablero inicial
jugador = "j"
marta = "m"
vacio = "-"
tablero = [[jugador, jugador, jugador, jugador, jugador, vacio, vacio, vacio, vacio, vacio],
            [jugador, jugador, jugador, jugador, vacio, vacio, vacio, vacio, vacio, vacio],
            [jugador, jugador, jugador, vacio, vacio, vacio, vacio, vacio, vacio, vacio],
            [jugador, jugador, vacio, vacio, vacio, vacio, vacio, vacio, vacio, vacio],
            [jugador, vacio, vacio, vacio, vacio, vacio, vacio, vacio, vacio, vacio],
            [vacio, vacio, vacio, vacio, vacio, vacio, vacio, vacio, vacio, marta],
            [vacio, vacio, vacio, vacio, vacio, vacio, vacio, vacio, marta, marta],
            [vacio, vacio, vacio, vacio, vacio, vacio, vacio, marta, marta, marta],
            [vacio, vacio, vacio, vacio, vacio, vacio, marta, marta, marta, marta],
            [vacio, vacio, vacio, vacio, vacio, marta, marta, marta, marta, marta],
]

# imprimir tablero
print(tablero[0])
print(tablero[1])
print(tablero[2])
print(tablero[3])
print(tablero[4])
print(tablero[5])
print(tablero[6])
print(tablero[7])
print(tablero[8])
print(tablero[9])

# ver turno
turno_jugador = True

# funcion del jugador
def Jugador_juega(tablero):
    # pedir la jugada en cordenada (y,x)
    jugada = input("ingrese su jugada: ")
    # print(jugada)
    # separar cada cordenada ingresada por un espacio
    jugada_arreglo = jugada.split( )
    valido_input =jugada_valida(tablero, jugada_arreglo)
    # print(jugada_arreglo)
    if (valido_input == True):
        # la ficha seleccionada
        ficha_selec = jugada_arreglo[0]
        # print(ficha_selec)
        pos = ficha_selec.split(",")
        pos1 = pos[0].split("(")
        y = int(pos1[1])
        pos1 = pos[1].split(")")
        x = int(pos1[0])
        # cambiar estado de la casilla seleccionada
        tablero[y][x] = "-"
        # ultima posicion de la jugada ingresada
        jugada_final = jugada_arreglo[-1]
        # print(jugada_final)
        pos = jugada_final.split(",")
        pos1 = pos[0].split("(")
        y = int(pos1[1])
        pos1 = pos[1].split(")")
        x = int(pos1[0])
        # cambiar estado de la casilla final
        tablero[y][x] = "j"
        # imprimir tablero nuevo
        print(tablero[0])
        print(tablero[1])
        print(tablero[2])
        print(tablero[3])
        print(tablero[4])
        print(tablero[5])
        print(tablero[6])
        print(tablero[7])
        print(tablero[8])
        print(tablero[9])
    else:
        print("no seas pendejo")

# verificar si la jugada ingresada es valida
def jugada_valida(tablero, jugada_e):
    # print(jugada_e)
    for i in range(int(len(jugada_e)) - 1):
        resultado_jugada = True
        # posicion inicial
        casilla_inicial = jugada_e[i]
        pos = casilla_inicial.split(",")
        pos1 = pos[0].split("(")
        y_inicial = int(pos1[1])
        pos1 = pos[1].split(")")
        x_inicial = int(pos1[0])
        # print(y_inicial, x_inicial)
        # print(jugada_e[i])
        casilla = jugada_e[i + 1]
        # print(casilla_inicial)
        # print(casilla)
        pos = casilla.split(",")
        pos1 = pos[0].split("(")
        y = int(pos1[1])
        pos1 = pos[1].split(")")
        x = int(pos1[0])
        # print(y, x)
        if (tablero[y_inicial][x_inicial] == "j" ):
            # verificar si es una jugada de saltos o solo un espacio
            if ((y == y_inicial+1) or (y == y_inicial-1) or (x == x_inicial+1) or (x == x_inicial-1)):
                # solo verifica si esta vacia
                if (tablero[y][x] == 'm' or tablero[y][x] == 'j'):
                    resultado_jugada = False
            else:
                # primero verificar que esten vacias
                if (tablero[y][x] == '-'):
                    # print("esta vacia")
                    # sacar las casillas ceracnas
                    cercanas_diagonales = ["", "", "", ""]
                    cercanas_lados = ["", "", "", ""]
                    # diagonales
                    cercanas_diagonales[0] = y_inicial-1,x_inicial-1
                    cercanas_diagonales[1] = y_inicial+1,x_inicial+1
                    cercanas_diagonales[2] = y_inicial-1,x_inicial+1
                    cercanas_diagonales[3] = y_inicial+1,x_inicial-1
                    # misma columna
                    cercanas_lados[0] = y_inicial-1,x_inicial
                    cercanas_lados[1] = y_inicial+1,x_inicial
                    # misma fila
                    cercanas_lados[2] = y_inicial,x_inicial-1
                    cercanas_lados[3] = y_inicial,x_inicial+1
                    # print(cercanas_diagonales)
                    # print(cercanas_lados)
                    # quiero mover a un mismo lado
                    if (y_inicial == y or x_inicial == x):
                        # print("entro putos ")
                        celda = y-1,x
                        # print(celda)
                        if (celda in cercanas_lados):
                            # print("hay")
                            if (tablero[y-1][x] == '-'):
                                # print("esta vacia la casilla de en medio, no se puede")
                                resultado_jugada = False
                        else:
                            celda = y+1,x
                            if (celda in cercanas_lados):
                                # print("hay")
                                if (tablero[y+1][x] == '-'):
                                    # print("esta vacia la casilla de en medio, no se puede")
                                    resultado_jugada = False
                            else:
                                celda = y,x-1
                                if (celda in cercanas_lados):
                                    # print("hay")
                                    if (tablero[y][x-1] == '-'):
                                        # print("esta vacia la casilla de en medio, no se puede")
                                        resultado_jugada = False
                                else:
                                    celda = y,x+1
                                    if (celda in cercanas_lados):
                                        # print("hay")
                                        if (tablero[y][x+1] == '-'):
                                            # print("esta vacia la casilla de en medio, no se puede")
                                            resultado_jugada = False
                                    else:
                                        # print("no hay casilla de inter 1")
                                        resultado_jugada = False
                    else:
                        # calculo de la celdas cercanas de la otra para encontrar inter
                        celda_diagonal = y-1,x-1
                        # print(celda)
                        if (celda_diagonal in cercanas_diagonales):
                            # print("hay")
                            # print(y-1,x-1)
                            # print(tablero[y-1][x-1])
                            if (tablero[y-1][x-1] == '-'):
                                # print("esta vacia la casilla de en medio, no se puede hacer")
                                resultado_jugada = False
                        else:
                            celda_diagonal = y+1,x+1
                            if (celda_diagonal in cercanas_diagonales):
                                # print("hay")
                                if (tablero[y+1][x+1] == '-'):
                                    # print("esta vacia la casilla de en medio, no se puede hacer")
                                    resultado_jugada = False
                            else:
                                celda_diagonal = y-1,x+1
                                if (celda_diagonal in cercanas_diagonales):
                                    # print("hay")
                                    if (tablero[y-1][x+1] == '-'):
                                        # print("esta vacia la casilla de en medio, no se puede hacer")
                                        resultado_jugada = False
                                else:
                                    celda_diagonal = y+1,x-1
                                    if (celda_diagonal in cercanas_diagonales):
                                        # print("hay")
                                        if (tablero[y+1][x-1] == '-'):
                                            # print("esta vacia la casilla de en medio, no se puede hacer")
                                            resultado_jugada = False
                                    else:
                                        celda = y-1,x
                                        if (celda in cercanas_lados):
                                            # print("hay")
                                            if (tablero[y-1][x] == '-'):
                                                # print("esta vacia la casilla de en medio, no se puede")
                                                resultado_jugada = False
                                        else:
                                            celda = y+1,x
                                            if (celda in cercanas_lados):
                                                # print("hay")
                                                if (tablero[y+1][x] == '-'):
                                                    # print("esta vacia la casilla de en medio, no se puede")
                                                    resultado_jugada = False
                                            else:
                                                celda = y,x-1
                                                if (celda in cercanas_lados):
                                                    # print("hay")
                                                    if (tablero[y][x-1] == '-'):
                                                        # print("esta vacia la casilla de en medio, no se puede")
                                                        resultado_jugada = False
                                                else:
                                                    celda = y,x+1
                                                    if (celda in cercanas_lados):
                                                        # print("hay")
                                                        if (tablero[y][x+1] == '-'):
                                                            # print("esta vacia la casilla de en medio, no se puede")
                                                            resultado_jugada = False
                                                    else:
                                                        # print("no hay casilla de inter 3")
                                                        resultado_jugada = False     
                else:
                    # print("no esta vacia")
                    resultado_jugada = False
        else:
            # print("no hay ficha en esa casilla")
            resultado_jugada = False
    if (resultado_jugada == False):
        return False
    else:
        return True

# # verificar si ya se gano
# def ganador(tablero):

def hoppers(tablero, turno_jugador):
    if (turno_jugador == True):
        Jugador_juega(tablero)


hoppers(tablero, turno_jugador)