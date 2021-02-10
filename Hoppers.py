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
            [jugador, vacio, vacio, vacio, vacio, vacio, vacio, vacio, vacio, vacio],
            [jugador, jugador, vacio, vacio, vacio, vacio, vacio, vacio, vacio, vacio],
            [jugador, jugador, vacio, jugador, vacio, vacio, vacio, vacio, vacio, vacio],
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

def jugada_ia(tablero, movimiento):
    inicio = movimiento[0]
    fin = movimiento[1]
    y_in = inicio[0]
    x_in = inicio[1]
    y = fin[0]
    x = fin[1]
    tablero[y][x] = 'm'
    tablero[y_in][x_in] = '-'

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
        # tablero[y][x] = "-"
        # ultima posicion de la jugada ingresada
        jugada_final = jugada_arreglo[-1]
        # print(jugada_final)
        pos = jugada_final.split(",")
        pos1 = pos[0].split("(")
        y = int(pos1[1])
        pos1 = pos[1].split(")")
        x = int(pos1[0])
        # cambiar estado de la casilla final
        # tablero[y][x] = "j"
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
                    tablero[y_inicial][x_inicial] = "-"
                    tablero[y][x] = "j"
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
                                tablero[y_inicial][x_inicial] = "-"
                                tablero[y][x] = "j"
                        else:
                            celda = y+1,x
                            if (celda in cercanas_lados):
                                # print("hay")
                                if (tablero[y+1][x] == '-'):
                                    # print("esta vacia la casilla de en medio, no se puede")
                                    resultado_jugada = False
                                else:
                                    tablero[y_inicial][x_inicial] = "-"
                                    tablero[y][x] = "j"
                            else:
                                celda = y,x-1
                                if (celda in cercanas_lados):
                                    # print("hay")
                                    if (tablero[y][x-1] == '-'):
                                        # print("esta vacia la casilla de en medio, no se puede")
                                        resultado_jugada = False
                                    else:
                                        tablero[y_inicial][x_inicial] = "-"
                                        tablero[y][x] = "j"
                                else:
                                    celda = y,x+1
                                    if (celda in cercanas_lados):
                                        # print("hay")
                                        if (tablero[y][x+1] == '-'):
                                            # print("esta vacia la casilla de en medio, no se puede")
                                            resultado_jugada = False
                                        else:
                                            tablero[y_inicial][x_inicial] = "-"
                                            tablero[y][x] = "j"
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
                                tablero[y_inicial][x_inicial] = "-"
                                tablero[y][x] = "j"
                        else:
                            celda_diagonal = y+1,x+1
                            if (celda_diagonal in cercanas_diagonales):
                                # print("hay")
                                if (tablero[y+1][x+1] == '-'):
                                    # print("esta vacia la casilla de en medio, no se puede hacer")
                                    resultado_jugada = False
                                else:
                                    tablero[y_inicial][x_inicial] = "-"
                                    tablero[y][x] = "j"
                            else:
                                celda_diagonal = y-1,x+1
                                if (celda_diagonal in cercanas_diagonales):
                                    # print("hay")
                                    if (tablero[y-1][x+1] == '-'):
                                        # print("esta vacia la casilla de en medio, no se puede hacer")
                                        resultado_jugada = False
                                    else:
                                        tablero[y_inicial][x_inicial] = "-"
                                        tablero[y][x] = "j"
                                else:
                                    celda_diagonal = y+1,x-1
                                    if (celda_diagonal in cercanas_diagonales):
                                        # print("hay")
                                        if (tablero[y+1][x-1] == '-'):
                                            # print("esta vacia la casilla de en medio, no se puede hacer")
                                            resultado_jugada = False
                                        else:
                                            tablero[y_inicial][x_inicial] = "-"
                                            tablero[y][x] = "j"
                                    else:
                                        celda = y-1,x
                                        if (celda in cercanas_lados):
                                            # print("hay")
                                            if (tablero[y-1][x] == '-'):
                                                # print("esta vacia la casilla de en medio, no se puede")
                                                resultado_jugada = False
                                            else:
                                                tablero[y_inicial][x_inicial] = "-"
                                                tablero[y][x] = "j"
                                        else:
                                            celda = y+1,x
                                            if (celda in cercanas_lados):
                                                # print("hay")
                                                if (tablero[y+1][x] == '-'):
                                                    # print("esta vacia la casilla de en medio, no se puede")
                                                    resultado_jugada = False
                                                else:
                                                    tablero[y_inicial][x_inicial] = "-"
                                                    tablero[y][x] = "j"
                                            else:
                                                celda = y,x-1
                                                if (celda in cercanas_lados):
                                                    # print("hay")
                                                    if (tablero[y][x-1] == '-'):
                                                        # print("esta vacia la casilla de en medio, no se puede")
                                                        resultado_jugada = False
                                                    else:
                                                        tablero[y_inicial][x_inicial] = "-"
                                                        tablero[y][x] = "j"
                                                else:
                                                    celda = y,x+1
                                                    if (celda in cercanas_lados):
                                                        # print("hay")
                                                        if (tablero[y][x+1] == '-'):
                                                            # print("esta vacia la casilla de en medio, no se puede")
                                                            resultado_jugada = False
                                                        else:
                                                            tablero[y_inicial][x_inicial] = "-"
                                                            tablero[y][x] = "j"
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

# verificar si ya se lleno el del jugador
def ganador_jugador(tablero):
    # verificar si el lado izquierdo esta lleno
    # print(tablero[0][0])
    if (tablero[0][0] == '-' or tablero[0][1] == '-' or tablero[0][2] == '-' or tablero[0][3] == '-' or tablero[0][4] == '-' or tablero[1][0] == '-' or tablero[1][1] == '-' or tablero[1][2] == '-' or tablero[1][3] == '-' or tablero[2][0] == '-' or tablero[2][1] == '-' or tablero[2][2] == '-' or tablero[3][0] == '-' or tablero[3][1] == '-' or tablero[3][0] == '-'):
        # print(ganador)
        # print(ganador)
        print("no esta lleno 1")
        return False
    else:
        print("gano el jugador")
        return True
    
# verificar si ya se lleno el de Marta
def ganador_marta(tablero):
    print("si entro con Marta")
    # verificar si el lado derecho esta lleno
    if (tablero[9][5] == '-' or tablero[9][6] == '-' or tablero[9][7] == '-' or tablero[9][8] == '-' or tablero[9][9] == '-' or tablero[8][6] == '-' or tablero[8][7] == '-' or tablero[8][8] == '-' or tablero[8][9] == '-' or tablero[7][7] == '-' or tablero[7][8] == '-' or tablero[7][9] == '-' or tablero[6][8] == '-' or tablero[6][9] == '-' or tablero[5][9] == '-'):
        # print(ganador)
        # print(ganador)
        print("no esta lleno")
        return False
    else:
        print("gano el Marta")
        return True

def hoppers(tablero, turno_jugador):
    Jugador_juega(tablero)
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
    turno_jugador = False
    valor, movimiento = minimax(tablero, 2, True)
    jugada_ia(tablero, movimiento)
    print(movimiento)
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
    turno_jugador = True
    while (ganador_jugador(tablero) != True and ganador_marta(tablero) != True):
        if (turno_jugador == True):
            Jugador_juega(tablero)
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
            turno_jugador = False
        else:
            valor, movimiento = minimax(tablero, 2, True)
            jugada_ia(tablero, movimiento)
            print(movimiento)
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
            turno_jugador = True

hoppers(tablero, turno_jugador)