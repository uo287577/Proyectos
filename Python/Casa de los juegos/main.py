import random

def inicio_juego():
    """ Imprime por pantalla un menú con los juegos disponibles e inicia el
    juego correspondiente """
    print("----- Elije un juego para jugar -----")
    print("1.Buscaminas")
    print()
    print("Introduce la tecla del número de juego que desees jugar")

    opcion = int(input("Escribe el número de juego: "))
    procesar_opcion(opcion)


def procesar_opcion(opcion):
    """ Recibe una opción, resultante de elegir un juego del menú, y en función
    de la opción pasada por parámetro, inicia un juego determinado """
    if(opcion == 1):
        jugar_buscaminas()


def jugar_buscaminas():
    """ Inicia una partida del juego del buscaminas pidiendo por teclado el
    número de filas y columnas del tablero de juego, la dificultad de juego
    e inicia la partida """
    presentacion_buscaminas()

    f = int(input("Dame número de filas para el tablero de juego (>0): "))
    c = int(input("Dame número de columnas para el tablero de juego (>0): "))

    while(f <= 0):
        f = int(input("Dame número de filas para el tablero de juego (>0): "))
    while(c <= 0):
        c = int(input("Dame número de columnas para el tablero de juego (>0): "))

    tablero = cargar_tablero_buscaminas(f,c)[0]
    tablero_con_minas_no_visibles = cargar_tablero_buscaminas(f,c)[1]

    tablero_con_banderas = crear_tablero(f,c,"0")

    mostrar_tablero(tablero,tablero_con_banderas)

    condicion1 = True
    condicion2 = True

    while (condicion1 and condicion2):
        condicion2 = movimiento_del_jugador(tablero,tablero_con_banderas,input("w,a,s,d para moverte; m para marcar, c para desmarcar, e para desactivar bomba: "))
        mostrar_tablero(tablero,tablero_con_banderas)
        condicion1 = not(comprobarFin(tablero_con_banderas, tablero_con_minas_no_visibles))

    print("#########################################################")
    print("#####################   GAME OVER   #####################")
    print("#########################################################")


def presentacion_buscaminas():
    """ Imprime por pantalla mensaje de bienvenida con los controles del
    buscaminas """
    print()
    print("#########################################################")
    print("######## BIENVENIDO AL JUEGO DEL BUSCAMINAS      ########")
    print("########                                         ########")
    print("######## Usa la tecla 'w' para ir arriba         ########")
    print("######## Usa la tecla 'a' para ir a la izquierda ########")
    print("######## Usa la tecla 's' para ir abajo          ########")
    print("######## Usa la tecla 'd' para ir a la derecha   ########")
    print("######## Usa la tecla 'm' para marcar            ########")
    print("######## Usa la tecla 'c' para desmarcar         ########")
    print("######## Usa la tecla 'e' para desactivar bomba  ########")
    print("########                                         ########")
    print("#########################################################")
    print()
    print()


def cargar_tablero_buscaminas(f,c):
    """ Recibe un número de filas y de columnas, y pide por teclado una
    dificultad de juego para la partida y en función de la dificultad se rellena
    de una cantidad u de otra el tablero de juego con minas. Al final retorna el
    tablero de juego resultante con las minas colocadas en función de la
    dificultad elegida. Y retorna otro tablero con solo las minas ocultadas """
    tablero = crear_tablero(f,c,0)

    diff = elegir_dificultad()

    if(diff == 1):
        buscaminas_facil(tablero)
    elif(diff == 2):
        buscaminas_normal(tablero)
    elif(diff == 3):
        buscaminas_dificil(tablero)

    ocultar_minas_tablero(tablero)
    tablero_con_minas_no_visibles = tablero
    pistas_sobre_minas(tablero)

    return tablero, tablero_con_minas_no_visibles


def crear_tablero(f,c,v):
    """ Recibe un número de filas, de columnas y un valor, y crea y retorna una
    matriz de dimensiones filas x columnas rellena con el valor recibido como
    parámetro """
    m = []
    for i in range(f):
        m.append(c * [v])
    return m


def elegir_dificultad():
    """ Imprime por pantalla un menú con las dificultades del juego disponibles
    y retorna el número de la dificultad elegida """
    print("---- Elije dificultad de juego ----")
    print("---- 1.Dificultad fácil        ----")
    print("---- 2.Dificultad normal       ----")
    print("---- 3.Dificultad difícil      ----")
    diff = int(input("Introduce el número de la dificultad: "))
    while((diff != 1) and (diff != 2) and (diff != 3)):
        diff = int(input("Dificultad no reconocida, inténtelo de nuevo. (1 = facil ; 2 = normal ; 3 = difícil): "))
    return diff


def buscaminas_facil(tablero):
    """ Recibe un tablero de juego del buscaminas y lo rellena con un número de
    minas tales que ocupen un 15% de todo el tablero de juego """
    numero_de_minas_15_por_ciento = calcular_numero_de_minas_en_tablero(tablero,15)
    for i in range(numero_de_minas_15_por_ciento):
        x = random.randint(0,len(tablero)-1)
        y = random.randint(0,len(tablero[0])-1)
        while(tablero[x][y] == '*'):
            x = random.randint(0,len(tablero)-1)
            y = random.randint(0,len(tablero[0])-1)
        tablero[x][y] = '*'


def buscaminas_normal(tablero):
    """ Recibe un tablero de juego del buscaminas y lo rellena con un número de
    minas tales que ocupen un 50% de todo el tablero de juego """
    numero_de_minas_50_por_ciento = calcular_numero_de_minas_en_tablero(tablero,50)
    for i in range(numero_de_minas_50_por_ciento):
        x = random.randint(0,len(tablero)-1)
        y = random.randint(0,len(tablero[0])-1)
        while(tablero[x][y] == '*'):
            x = random.randint(0,len(tablero)-1)
            y = random.randint(0,len(tablero[0])-1)
        tablero[x][y] = '*'


def buscaminas_dificil(tablero):
    """ Recibe un tablero de juego del buscaminas y lo rellena con un número de
    minas tales que ocupen un 75% de todo el tablero de juego """
    numero_de_minas_75_por_ciento = calcular_numero_de_minas_en_tablero(tablero,75)
    for i in range(numero_de_minas_75_por_ciento):
        x = random.randint(0,len(tablero)-1)
        y = random.randint(0,len(tablero[0])-1)
        while(tablero[x][y] == '*'):
            x = random.randint(0,len(tablero)-1)
            y = random.randint(0,len(tablero[0])-1)
        tablero[x][y] = '*'


def calcular_numero_de_minas_en_tablero(tablero,porc):
    """ Recibe un entero que será un tanto por ciento y calcula el número de
    casillas que componen el porcentaje pasado por parámetro en el tablero
    pasado por parámetro. Retorna el número de casillas calculadas """
    area_tablero = len(tablero) * len(tablero[0])
    return int(round(area_tablero * (porc / 100), 0))


def ocultar_minas_tablero(tablero):
    """ Recibe un tablero de juego del buscaminas y oculta las casillas marcadas
    como minas (marcadas con '*') """
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] != 0:
                tablero[i][j] = " "


def pistas_sobre_minas(tablero):
    """ Recibe un tablero de juego del buscaminas y cambia, en éste, los
    elementos que no sean minas (ocultadas por " ") y serán sustituidos por un
    número que significará cuántas minas hay en sus casillas vecinas """
    for i in range(len(tablero)):   # Recorrido por filas
        for j in range(len(tablero[i])):    # Recorrido por columnas
            if(tablero[i][j] != " "):  ## Si el elemento no es mina...

                # Si el elemento no mina está en la esquina superior izquierda...
                if(i == 0 and j == 0):
                    nuevoValor = 0
                    for a in range(i + 2): ## Recorrido de las filas
                        for b in range(j + 2):  ## Recorrido de las columnas
                            if (tablero[a][b] == " "):    ## Si el elemento seleccionado es mina...
                                nuevoValor = nuevoValor + 1
                                tablero[i][j] = nuevoValor

                # Si el elemento no mina está en la esquina superior derecha...
                if (i == 0 and j == len(tablero) - 1):
                    nuevoValor = 0
                    for a in range(i + 2):  ## Recorrido de las filas
                        for b in range(j - 1,len(tablero),1):  ## Recorrido de las columnas
                            if (tablero[a][b] == " "):   ## Si el elemento seleccionado es mina...
                                nuevoValor = nuevoValor + 1
                                tablero[i][j] = nuevoValor

                # Si el elemento no mina está en la primera fila...
                if i==0 and j!=0 and j!=len(tablero)-1:
                    nuevoValor=0
                    for a in range(i,i+2,1):  ## Recorrido de las filas
                        for b in range(j-1,j+2,1):  ## Recorrido de las columnas
                            if tablero[a][b]==" ":  ## Si el elemento seleccionado es mina...
                                nuevoValor=nuevoValor+1
                                tablero[i][j]=nuevoValor

                # Si el elemento no mina está en la última fila...
                if i==len(tablero)-1 and j!=0 and j!=len(tablero)-1:
                    nuevoValor=0
                    for a in range(i-1,i+1,1):  ## Recorrido de las filas
                        for b in range(j-1,j+2,1):  ## Recorrido de las columnas
                            if tablero[a][b]==" ":  ## Si el elemento seleccionado es mina...
                                nuevoValor=nuevoValor+1
                                tablero[i][j]=nuevoValor

                # Si el elemento no mina está en la esquina inferior izquierda...
                if i==len(tablero)-1 and j==0:
                    nuevoValor=0
                    for a in range(i-1,len(tablero),1): ## Recorrido de las filas
                        for b in range(j+2):  ## Recorrido de las columnas
                            if tablero[a][b]==" ":    ## Si el elemento seleccionado es mina...
                                nuevoValor=nuevoValor+1
                                tablero[i][j]=nuevoValor

                # Si el elemento no mina está en la primera columna...
                if i!=0 and i!=len(tablero)-1 and j==0:
                    nuevoValor=0
                    for a in range(i-1,i+2,1): ## Recorrido de las filas
                        for b in range(j+2):  ## Recorrido de las columnas
                            if tablero[a][b]==" ":    ## Si el elemento seleccionado es mina...
                                nuevoValor=nuevoValor+1
                                tablero[i][j]=nuevoValor

                # Si el elemento no mina está en la última columna...
                if i!=0 and i!=len(tablero)-1 and j==len(tablero)-1:
                    nuevoValor=0
                    for a in range(i-1,i+2,1): ## Recorrido de las filas
                        for b in range(j-1,len(tablero),1):  ## Recorrido de las columnas
                            if tablero[a][b]==" ":    ## Si el elemento seleccionado es mina...
                                nuevoValor=nuevoValor+1
                                tablero[i][j]=nuevoValor

                # Si el elemento no mina está en la esquina inferior derecha...
                if i==len(tablero)-1 and j==len(tablero)-1:
                    nuevoValor=0
                    for a in range(i-1,i+1,1): ## Recorrido de las filas
                        for b in range(j-1,j+1,1):  ## Recorrido de las columnas
                            if tablero[a][b]==" ":    ## Si el elemento seleccionado es mina...
                                nuevoValor=nuevoValor+1
                                tablero[i][j]=nuevoValor

                # Si el elemento no mina está en el interior del tablero...
                if i!=len(tablero)-1 and j!=len(tablero)-1 and i!=0 and j!=0:
                    nuevoValor=0
                    for a in range(i-1,i+2,1): ## Recorrido de las filas
                        for b in range(j-1,j+2,1):  ## Recorrido de las columnas
                            if tablero[a][b]==" ":    ## Si el elemento seleccionado es mina...
                                nuevoValor=nuevoValor+1
                                tablero[i][j]=nuevoValor


ubicacionJugador = [0,0]
def mostrar_tablero(tablero,tablero_con_banderas):
    """ Muestra por consola un tablero de juego recibido como parámetro junto
    con una leyenda explicando los controles del juego """
    # Salida por consola del tablero
    for i in range(len(tablero)): ## para cada fila del tablero...
        for j in range(len(tablero[i])): ## para cada elemento de cada fila del tablero...
           ## imprimir el elemento seleccionado
            if i == ubicacionJugador[0] and j == ubicacionJugador[1]:
                print ("X",end= " ")
            elif tablero_con_banderas[i][j]=="%":
                print("%",end=" ")
            else:
                print(tablero[i][j], end=" ")
        print() ## salto de línea para cada fila
    # Leyenda con los controles
    print()
    print()
    print("'w' para moverte hacia arriba")
    print("'a' para moverte hacia la izquierda")
    print("'s' para moverte hacia abajo")
    print("'d' para moverte hacia la derecha")
    print("'m' para marcar")
    print("'c' para desmarcar")
    print("'e' para desactivar bomba")
    print()
    print()


def movimiento_del_jugador(tablero,tableroBanderas,letra):
    """ A partir del parámetro de tipo carácter, el jugador se desplazará por el
    tablero de juego, dado como parámetro, mediante las letras "a" o "A"
    (movimiento hacia la izquierda), "d" o "D" (movimiento hacia la derecha),
    "s" o "S" (movimiento hacia abajo) y "w" o "W" (movimiento hacia arriba) """
    movimiento=letra
    if movimiento=='a' or movimiento=='A':
        if ubicacionJugador[1]-1 >= 0:
            ubicacionJugador[1] = ubicacionJugador[1] - 1
    elif movimiento=='d' or movimiento=='D':
        if ubicacionJugador[1]+1 < (len(tablero)):
            ubicacionJugador[1] = ubicacionJugador[1] + 1
    elif movimiento=='w' or movimiento=='W':
        if ubicacionJugador[0]-1 >= 0:
            ubicacionJugador[0] = ubicacionJugador[0] -1
    elif movimiento=='s' or movimiento=='S':
        if ubicacionJugador[0]+1 < (len(tablero)):
            ubicacionJugador[0] = ubicacionJugador[0] + 1

    elif movimiento=='m' or movimiento=='M':
        tableroBanderas[ubicacionJugador[0]][ubicacionJugador[1]]="%"
    elif movimiento=='c' or movimiento=='C':
        tableroBanderas[ubicacionJugador[0]][ubicacionJugador[1]]="0"

    elif movimiento=='e' or movimiento=='E':
        if tablero[ubicacionJugador[0]][ubicacionJugador[1]]==" ":
            return False
    return True


def comprobarFin(tableroDeBanderas,tableroDeMinasNoVisibles):
    """Recibe un tablero de banderas y un tablero de minas no visibles, y si en
    una posición hay bandera y no hay bomba, devuelve False porque el juego no
    termimó, y si hay bomba y no está marcada, tampoco termina"""
    for i in range(len(tableroDeBanderas)):
        for j in range(len(tableroDeBanderas[i])):
            if not(tableroDeBanderas[i][j]=="%" and tableroDeMinasNoVisibles[i][j]==" "):
                return False
    return True

def imprimirPresentacion():
    print("\t==============================================================")
    print("\tBienvenido a la casa de los juegos!")
    print("\tAutor: Miguel Fernández Huerta")
    print("\t==============================================================")

def main():
    imprimirPresentacion()
    inicio_juego()

main()