from Tablero import Tablero
from Celda import Celda
costo_final = 0
texto_solucion = ""


def InicioCosteo(nodo_piso, nodo_patron_origen, nodo_patron_destino):
    contador_filas = 0
    contador_columnas = 0

    #print("nombre del piso: ", nodo_piso.piso.nombre)
    #print("columnas del piso: ", nodo_piso.piso.columns)
    #print("filas del piso: ", nodo_piso.piso.rows)
    #print("costo flip del piso: ", nodo_piso.piso.costo_flip)
    #print("costo switch del piso: ", nodo_piso.piso.costo_switch)
    #print("")
    #print("codigo del patron origen: ", nodo_patron_origen.patron.codigo)
    #print("string del patrón origen: ", nodo_patron_origen.patron.string_patron)
    #print("")
    #print("codigo del patron destino: ", nodo_patron_destino.patron.codigo)
    #print("string del patrón destino: ", nodo_patron_destino.patron.string_patron)

    lista_celdas_origen = Tablero()
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

    lista_celdas_destino = Tablero()
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

    ClasificarPiso(nodo_piso.piso.rows, nodo_piso.piso.columns, lista_celdas_origen, lista_celdas_destino, nodo_piso.piso.costo_flip, nodo_piso.piso.costo_switch)




def ClasificarPiso(filas, columnas, lista_celdas_origen, lista_celdas_destino, costo_flip, costo_switch):

    if filas == 1 and columnas>filas:
        print("matriz lineal")
        lista_celdas_origen.resolver_lineal(lista_celdas_destino, costo_flip, costo_switch, filas, columnas)

    elif filas > 1 and columnas > 1:
        print("matriz cuadrada")

    elif columnas == 1 and filas > 1:
        print("matriz vertical")

