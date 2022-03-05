import FuncionCelda
import Manejo_archivos
from NodoFila import NodoFila
from Tablero_Lineal import Tablero_Lineal
from copy import deepcopy


solucion_intercambios_simples = ""
solucion_volteando_celdas = ""
coste_intercambios = 0
coste_volteos = 0
cambios_hechos = 0


class Tablero:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0  # se refiere a la cantidad de filas que hay

    def insertar(self, contenido_fila_ingresado, index):
        nuevo_nodo = NodoFila(contenido_fila=contenido_fila_ingresado, indice=index)
        if self.primero is None:
            self.primero = self.ultimo = NodoFila(contenido_fila=contenido_fila_ingresado, indice=index)
        else:
            nuevo_nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
        self.size += 1

    def recorrer(self):
        actual = self.primero

        while actual:
            print("esta es la fila numero: ", actual.indice)
            actual.contenido_fila.recorrer()

            actual = actual.siguiente

    def count_black(self):
        actual = self.primero
        contador = 0
        while actual:
            actual_fila = actual.contenido_fila.primero
            while actual_fila:
                if not actual_fila.celda.color:
                    contador += 1
                actual_fila = actual_fila.siguiente

            actual = actual.siguiente

        return contador

    def count_white(self):
        actual = self.primero
        contador = 0
        while actual:
            actual_fila = actual.contenido_fila.primero
            while actual_fila:
                if actual_fila.celda.color:
                    contador += 1
                actual_fila = actual_fila.siguiente

            actual = actual.siguiente

        return contador

    def Buscar_celda(self, x, y):
        actual_fila = self.primero
        while actual_fila:
            actual_celda_fila = actual_fila.contenido_fila.primero
            while actual_celda_fila:
                if actual_celda_fila.celda.x == x and actual_celda_fila.celda.y == y:
                    return actual_celda_fila.celda

                actual_celda_fila = actual_celda_fila.siguiente
            actual_fila = actual_fila.siguiente

    def Voltear_erroneas(self, matriz_destino, costo_flip):
        global solucion_volteando_celdas, coste_volteos
        fila_actual_origen = self.primero
        fila_actual_destino = matriz_destino.primero
        while fila_actual_origen and fila_actual_destino:
            celda_actual_origen = fila_actual_origen.contenido_fila.primero
            celda_actual_destino = fila_actual_destino.contenido_fila.primero
            while celda_actual_destino and celda_actual_origen:

                if celda_actual_origen.celda.color != celda_actual_destino.celda.color:
                    coste_volteos += costo_flip
                    solucion_volteando_celdas += "La celda en la fila: " + str(
                    celda_actual_origen.celda.x) + " y columna: " + str(
                    celda_actual_origen.celda.y) + " ha sido volteada el coste acumulado es de: " + str(coste_volteos) + "\n"
                    celda_actual_origen.celda.color = not celda_actual_origen.celda.color

                celda_actual_destino = celda_actual_destino.siguiente
                celda_actual_origen = celda_actual_origen.siguiente

            fila_actual_destino = fila_actual_destino.siguiente
            fila_actual_origen = fila_actual_origen.siguiente




    def comparar_matrices(self, matriz_destino):
        fila_actual_origen = self.primero
        fila_actual_destino = matriz_destino.primero
        while fila_actual_origen and fila_actual_destino:
            celda_actual_origen = fila_actual_origen.contenido_fila.primero
            celda_actual_destino = fila_actual_destino.contenido_fila.primero
            while celda_actual_destino and celda_actual_origen:

                if celda_actual_origen.celda.color != celda_actual_destino.celda.color:
                    return False

                celda_actual_destino = celda_actual_destino.siguiente
                celda_actual_origen = celda_actual_origen.siguiente

            fila_actual_destino = fila_actual_destino.siguiente
            fila_actual_origen = fila_actual_origen.siguiente
        return True

    def Resolver(self, matriz_destino, filas, costo_flip, costo_switch):
        global solucion_intercambios_simples, solucion_volteando_celdas, coste_intercambios, coste_volteos
        coste_intercambios = coste_volteos = 0
        solucion_volteando_celdas = solucion_intercambios_simples = ""
        casillas_blancas_origen = self.count_white()
        casillas_negras_origen = self.count_black()
        casillas_blancas_destino = matriz_destino.count_white()
        casillas_negras_destino = matriz_destino.count_black()
        matriz_para_voltear = deepcopy(self)
        matriz_para_imprimir = deepcopy(self)

        if casillas_negras_destino == casillas_negras_origen and casillas_blancas_destino == casillas_blancas_origen:
            #print("no hay necesidad de hacer cambios")
            while not self.comparar_matrices(matriz_destino):
                self.hallar_celdas_erroneas(matriz_destino, filas, costo_flip, costo_switch)
            matriz_para_voltear.Voltear_erroneas(matriz_destino, costo_flip)


            if coste_volteos < coste_intercambios or coste_intercambios == coste_volteos:
                #print("es mas barato voltear todas")
                print("Para visualizar los pasos para resolver la matriz usted debe de escoger una opción:")
                print("Si desea ver la solución paso a paso en consola ingrese la letra 'c', si desea verla en un archivo.txt ingrese la letra 't' ")
                opcion = input()

                if opcion == "c":
                    print(solucion_volteando_celdas)
                    FuncionCelda.Imprimir_matriciales(matriz_para_imprimir, matriz_destino)

                elif opcion == "t":
                    Manejo_archivos.Crear_Instrucciones(solucion_volteando_celdas)
                    FuncionCelda.Imprimir_matriciales(matriz_para_imprimir, matriz_destino)


            elif coste_volteos > coste_intercambios:
                #print("es mejor intercambiar")
                print("Para visualizar los pasos para resolver la matriz usted debe de escoger una opción:")
                print(
                    "Si desea ver la solución paso a paso en consola ingrese la letra 'c', si desea verla en un archivo.txt ingrese la letra 't' ")
                opcion = input()
                if opcion == "c":
                    print(solucion_intercambios_simples)
                    FuncionCelda.Imprimir_matriciales(matriz_para_imprimir, matriz_destino)
                elif opcion == "t":
                    Manejo_archivos.Crear_Instrucciones(solucion_intercambios_simples)
                    FuncionCelda.Imprimir_matriciales(matriz_para_imprimir, matriz_destino)


        else:
            #print("se necesitan voltear casillas")
            self.hallar_celdas_erroneas(matriz_destino, filas, costo_flip, costo_switch)
            while cambios_hechos > 0:
                self.hallar_celdas_erroneas(matriz_destino, filas, costo_flip, costo_switch)
            self.Voltear_erroneas(matriz_destino, costo_flip)

            costo_total = coste_volteos + coste_intercambios
            solucion_total = "----pasos intercambios----\n" + solucion_intercambios_simples +"\n ----pasos volteos----\n" + solucion_volteando_celdas + "\nEl coste final ha sido de: " + str(costo_total)

            coste_volteos = 0
            solucion_volteando_celdas = ""

            matriz_para_voltear.Voltear_erroneas(matriz_destino, costo_flip)

            if costo_total < coste_volteos or costo_total == coste_volteos:
                #print("es mejor voltear")
                print("Para visualizar los pasos para resolver la matriz usted debe de escoger una opción:")
                print(
                    "Si desea ver la solución paso a paso en consola ingrese la letra 'c', si desea verla en un archivo.txt ingrese la letra 't' ")
                opcion = input()

                if opcion == "c":
                    print(solucion_total)
                    FuncionCelda.Imprimir_matriciales(matriz_para_imprimir, matriz_destino)
                elif opcion == "t":
                    Manejo_archivos.Crear_Instrucciones(solucion_total)
                    FuncionCelda.Imprimir_matriciales(matriz_para_imprimir, matriz_destino)

            elif coste_volteos < costo_total:
                print("Para visualizar los pasos para resolver la matriz usted debe de escoger una opción:")
                print("Si desea ver la solución paso a paso en consola ingrese la letra 'c', si desea verla en un archivo.txt ingrese la letra 't' ")
                opcion = input()

                if opcion == "c":
                    print(solucion_volteando_celdas)
                    FuncionCelda.Imprimir_matriciales(matriz_para_imprimir, matriz_destino)
                elif opcion == "t":
                    Manejo_archivos.Crear_Instrucciones(solucion_volteando_celdas)
                    FuncionCelda.Imprimir_matriciales(matriz_para_imprimir, matriz_destino)


    def hallar_celdas_erroneas(self, matriz_destino, filas, costo_flip, costo_switch):
        global cambios_hechos
        primer_nodo_erroneo = None
        segundo_nodo_erroneo = None
        actual_fila_origen = self.primero
        actual_fila_destino = matriz_destino.primero
        distancia_entre_celdas_erroneas = 0
        while actual_fila_destino and actual_fila_origen:  # se comienza recorriendo las filas
            actual_lista_origen = actual_fila_origen.contenido_fila.primero
            actual_lista_destino = actual_fila_destino.contenido_fila.primero
            while actual_lista_destino and actual_lista_origen:  # se recorren las filas
                if actual_lista_origen.celda.color != actual_lista_destino.celda.color:
                    if primer_nodo_erroneo is None:
                        primer_nodo_erroneo = actual_lista_origen
                    if primer_nodo_erroneo is not None and actual_lista_origen.celda.color != primer_nodo_erroneo.celda.color:
                        if segundo_nodo_erroneo is None:
                            segundo_nodo_erroneo = actual_lista_origen
                            distancia_entre_celdas_erroneas = abs(
                                segundo_nodo_erroneo.celda.x - primer_nodo_erroneo.celda.x) + abs(
                                segundo_nodo_erroneo.celda.y - primer_nodo_erroneo.celda.y)
                        else:
                            nueva_distancia = abs(actual_lista_origen.celda.x - primer_nodo_erroneo.celda.x) + abs(
                                actual_lista_origen.celda.y - primer_nodo_erroneo.celda.y)
                            if nueva_distancia < distancia_entre_celdas_erroneas:
                                segundo_nodo_erroneo = actual_lista_origen

                actual_lista_origen = actual_lista_origen.siguiente
                actual_lista_destino = actual_lista_destino.siguiente

            actual_fila_origen = actual_fila_origen.siguiente
            actual_fila_destino = actual_fila_destino.siguiente


        if primer_nodo_erroneo is None or segundo_nodo_erroneo is None:
            cambios_hechos = 0
            return
        else:
            armar_camino(self, primer_nodo_erroneo, segundo_nodo_erroneo, costo_switch)



def armar_camino(matriz_origen, nodo_inicio, nodo_destino, costo_switch):
    camino_entre_celdas = Tablero_Lineal()
    columna_destino = nodo_destino.celda.y
    fila_destino = nodo_destino.celda.x
    fila_origen = nodo_inicio.celda.x
    columna_origen = nodo_inicio.celda.y
    if nodo_destino.celda.x == nodo_inicio.celda.x:
        #print("el nodo inicio está a la izquierda del nodo destino") #vamos a crear la lista para el caso más simple
        while nodo_inicio.celda.y <= nodo_destino.celda.y:
            if nodo_inicio.celda.y < nodo_destino.celda.y:
                camino_entre_celdas.insertar(nodo_inicio.celda)
                nodo_inicio = nodo_inicio.siguiente
                continue
            if nodo_inicio.celda.y == nodo_destino.celda.y:
                camino_entre_celdas.insertar(nodo_inicio.celda)
                break

        #print("")
    else:
       # print("el nodo destino está mas abajo que el nodo origen")
        if nodo_inicio.celda.y < nodo_destino.celda.y:

           # print("el nodo destino está abajo y a la derecha")
            # obtenemos las celdas hacia abajo
            while fila_origen <= fila_destino:
                if fila_origen < fila_destino:
                    camino_entre_celdas.insertar(matriz_origen.Buscar_celda(fila_origen, columna_origen))
                    fila_origen += 1
                    continue
                if fila_origen == fila_destino:
                    break




                    # obtenemos las celdas hacia la derecha
            while columna_origen <= columna_destino:
                if columna_origen < columna_destino:
                    camino_entre_celdas.insertar(matriz_origen.Buscar_celda(fila_origen, columna_origen))
                    columna_origen += 1
                    continue
                if columna_origen == columna_destino:
                    camino_entre_celdas.insertar(matriz_origen.Buscar_celda(fila_origen, fila_destino))
                    break


        elif nodo_inicio.celda.y > nodo_destino.celda.y:
            #print("el nodo destino está abajo y a la izquierda")
                # obtenemos las celdas hacia abajo
            while fila_origen <= fila_destino:
                if fila_origen < fila_destino:
                    camino_entre_celdas.insertar(matriz_origen.Buscar_celda(fila_origen, columna_origen))
                    fila_origen += 1
                    continue
                if fila_origen == fila_destino:
                    break


            # obtenemos las celdas hacia la izquierda
            while columna_origen >= columna_destino:
                if columna_origen > columna_destino:
                    camino_entre_celdas.insertar(matriz_origen.Buscar_celda(fila_origen, columna_origen))
                    columna_origen -= 1
                    continue
                if columna_origen == columna_destino:
                    camino_entre_celdas.insertar(matriz_origen.Buscar_celda(fila_origen, columna_origen))
                    break



        elif nodo_inicio.celda.y == nodo_destino.celda.y:
            #print("el nodo destino está abajo del nodo origen")
            # obtenemos las celdas hacia abajo
            while fila_origen <= fila_destino:
                if fila_origen < fila_destino:
                    camino_entre_celdas.insertar(matriz_origen.Buscar_celda(fila_origen, columna_origen))
                    fila_origen += 1
                    continue
                if fila_origen == fila_destino:
                    camino_entre_celdas.insertar(matriz_origen.Buscar_celda(fila_origen, columna_origen))
                    break

    check_camino(camino_entre_celdas, costo_switch)


def check_camino(camino_entre_celdas, coste_switch):
    global coste_intercambios, solucion_intercambios_simples, cambios_hechos
    nodo_origen = camino_entre_celdas.primero
    nodo_destino = camino_entre_celdas.ultimo
    if camino_entre_celdas.size == 2:
        coste_intercambios += coste_switch
        solucion_intercambios_simples += "La celda en la fila: " + str(
            nodo_origen.celda.x) + " y columna: " + str(
            nodo_origen.celda.y) + " ha sido intercambiada por la celda en la fila: " + str(
            nodo_destino.celda.x) + " y columna: " + str(
            nodo_destino.celda.y) + " el coste acumulado es de: " + str(coste_intercambios) + "\n"
        cambios_hechos += 1
        nodo_origen.celda.color = not nodo_origen.celda.color
        nodo_destino.celda.color = not nodo_destino.celda.color
        return

    else:
        actual_camino = camino_entre_celdas.primero.siguiente
        camino_de_un_mismo_color = True
        color_actual = camino_entre_celdas.primero.siguiente.celda.color
        while actual_camino.celda.x != nodo_destino.celda.x or actual_camino.celda.y != nodo_destino.celda.y:
            if actual_camino.celda.color != color_actual:
                camino_de_un_mismo_color = False
                break

            actual_camino = actual_camino.siguiente

        #print("el camino es de un mismo color? ", camino_de_un_mismo_color)
        if camino_de_un_mismo_color:
            soluciona_mismo_color(camino_entre_celdas, coste_switch, color_actual)
        else:
            soluciona_distinto_color(camino_entre_celdas, coste_switch)

def soluciona_mismo_color(camino_entre_celdas, costo_switch, color):
    global coste_intercambios, solucion_intercambios_simples, cambios_hechos
    if color:
        # print("el color del camino es todo blanco")
        if camino_entre_celdas.primero.celda.color != color:
            # print("recorrer todo el camino de izquierda a derecha. Moviendo la celda origen a la celda destino")
            Nodo_izquierda_derecha = camino_entre_celdas.primero
            while Nodo_izquierda_derecha:
                coste_intercambios += costo_switch
                solucion_intercambios_simples += "La celda en la fila: " + str(
                    Nodo_izquierda_derecha.celda.x) + " y columna: " + str(
                    Nodo_izquierda_derecha.celda.y) + " ha sido intercambiada por la celda en la fila: " + str(
                    Nodo_izquierda_derecha.siguiente.celda.x) + " y columna: " + str(
                    Nodo_izquierda_derecha.siguiente.celda.y) + " el coste acumulado es de: " + str(
                    coste_intercambios) + "\n"
                cambios_hechos += 1
                Nodo_izquierda_derecha = Nodo_izquierda_derecha.siguiente
                if Nodo_izquierda_derecha.siguiente is None:
                    break
            camino_entre_celdas.primero.celda.color = not camino_entre_celdas.primero.celda.color
            camino_entre_celdas.ultimo.celda.color = not camino_entre_celdas.ultimo.celda.color

        else:
            # print("recorrer el camino de derecha a izquierda. Moviendo la celda destino a la celda origen")
            Nodo_derecha_izquierda = camino_entre_celdas.ultimo
            while Nodo_derecha_izquierda:
                coste_intercambios += costo_switch
                solucion_intercambios_simples += "La celda en la fila: " + str(
                    Nodo_derecha_izquierda.celda.x) + " y columna: " + str(
                    Nodo_derecha_izquierda.celda.y) + " ha sido intercambiada por la celda en la fila: " + str(
                    Nodo_derecha_izquierda.anterior.celda.x) + " y columna: " + str(
                    Nodo_derecha_izquierda.anterior.celda.y) + " el coste acumulado es de: " + str(
                    coste_intercambios) + "\n"
                cambios_hechos += 1
                Nodo_derecha_izquierda = Nodo_derecha_izquierda.anterior
                if Nodo_derecha_izquierda.anterior is None:
                    break
            camino_entre_celdas.primero.celda.color = not camino_entre_celdas.primero.celda.color
            camino_entre_celdas.ultimo.celda.color = not camino_entre_celdas.ultimo.celda.color


    else:
        # print("el color del camino es todo negro")
        if camino_entre_celdas.primero.celda.color != color:
            # print( "recorrer todo el camino de izquierda a derecha. Moviendo la celda origen a la celda destino")
            Nodo_izquierda_derecha = camino_entre_celdas.primero
            while Nodo_izquierda_derecha:
                coste_intercambios += costo_switch
                solucion_intercambios_simples += "La celda en la fila: " + str(
                    Nodo_izquierda_derecha.celda.x) + " y columna: " + str(
                    Nodo_izquierda_derecha.celda.y) + " ha sido intercambiada por la celda en la fila: " + str(
                    Nodo_izquierda_derecha.siguiente.celda.x) + " y columna: " + str(
                    Nodo_izquierda_derecha.siguiente.celda.y) + " el coste acumulado es de: " + str(
                    coste_intercambios) + "\n"
                cambios_hechos += 1
                Nodo_izquierda_derecha = Nodo_izquierda_derecha.siguiente
                if Nodo_izquierda_derecha.siguiente is None:
                    break

            camino_entre_celdas.primero.celda.color = not camino_entre_celdas.primero.celda.color
            camino_entre_celdas.ultimo.celda.color = not camino_entre_celdas.ultimo.celda.color

        else:
            # print("recorrer el camino de derecha a izquierda. Moviendo la celda destino a la celda origen")
            Nodo_derecha_izquierda = camino_entre_celdas.ultimo
            while Nodo_derecha_izquierda:
                coste_intercambios += costo_switch
                solucion_intercambios_simples += "La celda en la fila: " + str(
                    Nodo_derecha_izquierda.celda.x) + " y columna: " + str(
                    Nodo_derecha_izquierda.celda.y) + " ha sido intercambiada por la celda en la fila: " + str(
                    Nodo_derecha_izquierda.anterior.celda.x) + " y columna: " + str(
                    Nodo_derecha_izquierda.anterior.celda.y) + " el coste acumulado es de: " + str(
                    coste_intercambios) + "\n"
                cambios_hechos += 1
                Nodo_derecha_izquierda = Nodo_derecha_izquierda.anterior
                if Nodo_derecha_izquierda.anterior is None:
                    break

            camino_entre_celdas.primero.celda.color = not camino_entre_celdas.primero.celda.color
            camino_entre_celdas.ultimo.celda.color = not camino_entre_celdas.ultimo.celda.color

def soluciona_distinto_color(camino_entre_celdas, coste_switch):
    global coste_intercambios, solucion_intercambios_simples, cambios_hechos
    nodo_origen = camino_entre_celdas.primero
    nodo_destino = None

    actual_nodo_camino_celdas = camino_entre_celdas.primero.siguiente

    while actual_nodo_camino_celdas:
        if actual_nodo_camino_celdas.celda.color != nodo_origen.celda.color:
            nodo_destino = actual_nodo_camino_celdas
            break
        actual_nodo_camino_celdas = actual_nodo_camino_celdas.siguiente

    distancia_entre_celdas_erroneas = abs(
        nodo_destino.celda.x - nodo_origen.celda.x) + abs(
        nodo_destino.celda.y - nodo_origen.celda.y)

    if distancia_entre_celdas_erroneas == 1:
        coste_intercambios += coste_switch
        solucion_intercambios_simples += "La celda en la fila: " + str(
            nodo_origen.celda.x) + " y columna: " + str(
            nodo_origen.celda.y) + " ha sido intercambiada por la celda en la fila: " + str(
            nodo_destino.celda.x) + " y columna: " + str(
            nodo_destino.celda.y) + " el coste acumulado es de: " + str(coste_intercambios) + "\n"
        cambios_hechos += 1
        nodo_origen.celda.color = not nodo_origen.celda.color
        nodo_destino.celda.color = not nodo_destino.celda.color
        return

    else:
        subcamino = Tablero_Lineal()
        while True:
            if nodo_origen.celda.y != nodo_destino.celda.y or nodo_origen.celda.x != nodo_destino.celda.x:
                subcamino.insertar(nodo_origen.celda)
                nodo_origen = nodo_origen.siguiente
                continue
            if nodo_origen.celda.y == nodo_destino.celda.y or nodo_origen.celda.x == nodo_destino.celda.x:
                subcamino.insertar(nodo_origen.celda)
                break

        check_camino(subcamino, coste_switch)

























