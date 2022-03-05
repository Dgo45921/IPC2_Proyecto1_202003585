from Tablero_Lineal import Tablero_Lineal
from Celda import Celda
from Tablero import Tablero

costo_final = 0
texto_solucion = ""


def InicioCosteo(nodo_piso, nodo_patron_origen, nodo_patron_destino):
    if nodo_piso.piso.rows == 1 and nodo_piso.piso.columns > 1:
        contador_filas = 0
        contador_columnas = 0
        lista_celdas_origen = Tablero_Lineal()
        # crear lista de celdas patron origen
        for letra in nodo_patron_origen.patron.string_patron:
            if letra == "W":
                nueva_celda = Celda(contador_filas, contador_columnas, True)
                lista_celdas_origen.insertar(nueva_celda)
                contador_columnas += 1
                if contador_columnas == nodo_piso.piso.columns:
                    contador_columnas = 0
                    contador_filas += 1

            elif letra == "B":
                nueva_celda = Celda(contador_filas, contador_columnas, False)
                lista_celdas_origen.insertar(nueva_celda)
                contador_columnas += 1
                if contador_columnas == nodo_piso.piso.columns:
                    contador_columnas = 0
                    contador_filas += 1

        contador_columnas = contador_filas = 0

        lista_celdas_destino = Tablero_Lineal()
        # crear lista de celdas patron destino
        for letra in nodo_patron_destino.patron.string_patron:
            if letra == "W":
                nueva_celda = Celda(contador_filas, contador_columnas, True)
                lista_celdas_destino.insertar(nueva_celda)
                contador_columnas += 1
                if contador_columnas == nodo_piso.piso.columns:
                    contador_columnas = 0
                    contador_filas += 1

            elif letra == "B":
                nueva_celda = Celda(contador_filas, contador_columnas, False)
                lista_celdas_destino.insertar(nueva_celda)
                contador_columnas += 1
                if contador_columnas == nodo_piso.piso.columns:
                    contador_columnas = 0
                    contador_filas += 1

        Lista_lineal(nodo_piso.piso.rows, nodo_piso.piso.columns, lista_celdas_origen, lista_celdas_destino,
                     nodo_piso.piso.costo_flip, nodo_piso.piso.costo_switch)

    if nodo_piso.piso.rows > 1 and nodo_piso.piso.columns > 1 or nodo_piso.piso.rows > 1 and nodo_piso.piso.columns == 1:

        tablero_nuevo = Tablero()
        tablero_nuevo2 = Tablero()
        contador_filas = 0
        contador_columnas = 0

        for letra in nodo_patron_origen.patron.string_patron:

            if contador_columnas == 0:
                nueva_fila = Tablero_Lineal()

            if letra == "W":
                nueva_celda = Celda(contador_filas, contador_columnas, True)
                nueva_fila.insertar(nueva_celda)
                contador_columnas += 1
                if contador_columnas == nodo_piso.piso.columns:
                    tablero_nuevo.insertar(nueva_fila, contador_filas)
                    contador_columnas = 0
                    contador_filas += 1

            elif letra == "B":
                nueva_celda = Celda(contador_filas, contador_columnas, False)
                nueva_fila.insertar(nueva_celda)
                contador_columnas += 1
                if contador_columnas == nodo_piso.piso.columns:
                    tablero_nuevo.insertar(nueva_fila, contador_filas)
                    contador_columnas = 0
                    contador_filas += 1

        contador_filas = 0
        contador_columnas = 0

        for letra in nodo_patron_destino.patron.string_patron:

            if contador_columnas == 0:
                nueva_fila = Tablero_Lineal()

            if letra == "W":
                nueva_celda = Celda(contador_filas, contador_columnas, True)
                nueva_fila.insertar(nueva_celda)
                contador_columnas += 1
                if contador_columnas == nodo_piso.piso.columns:
                    tablero_nuevo2.insertar(nueva_fila, contador_filas)
                    contador_columnas = 0
                    contador_filas += 1

            elif letra == "B":
                nueva_celda = Celda(contador_filas, contador_columnas, False)
                nueva_fila.insertar(nueva_celda)
                contador_columnas += 1
                if contador_columnas == nodo_piso.piso.columns:
                    tablero_nuevo2.insertar(nueva_fila, contador_filas)
                    contador_columnas = 0
                    contador_filas += 1

        Matriz(tablero_nuevo, tablero_nuevo2, nodo_piso.piso.rows, nodo_piso.piso.costo_flip,
               nodo_piso.piso.costo_switch)


def Lista_lineal(filas, columnas, lista_celdas_origen, lista_celdas_destino, costo_flip, costo_switch):
    if filas == 1 and columnas > filas:
        print("matriz lineal")
        lista_celdas_origen.resolver_lineal(lista_celdas_destino, costo_flip, costo_switch)

    elif columnas == 1 and filas > 1:
        print("matriz vertical")


def Matriz(matriz_origen, matriz_destino, filas, costo_flip, costo_switch):
    matriz_origen.Resolver(matriz_destino, filas, costo_flip, costo_switch)
