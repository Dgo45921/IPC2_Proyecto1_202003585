import Manejo_archivos
from NodoCelda import NodoCelda
from copy import deepcopy
import FuncionCelda

coste_intercambios_simples = 0
solucion_intercambios_simples = ""
solucion_volteando_celdas = ""
coste_volteando_celdas = 0
lista_origen = None
voltear_necesario = False


class Tablero_Lineal:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def insertar(self, celda_ingresada):
        nuevo_nodo = NodoCelda(celda=celda_ingresada)
        if self.primero is None:
            self.primero = self.ultimo = NodoCelda(celda=celda_ingresada)
        else:
            nuevo_nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
        self.size += 1

    def recorrer(self):
        actual = self.primero
        while actual is not None:
            print("coordenada x: ", actual.celda.x, "coordenada y: ", actual.celda.y, "color es: ", actual.celda.color)
            actual = actual.siguiente

    def resolver_lineal(self, lista_celdas_destino, costo_flip, costo_switch):
        global solucion_intercambios_simples, coste_intercambios_simples, coste_volteando_celdas, solucion_volteando_celdas, lista_origen
        lista_origen = deepcopy(self)
        lista_origen2 = deepcopy(self)
        contador_celdas_blancas_lista_origen = 0
        contador_celdas_negras_lista_origen = 0
        contador_celdas_blancas_lista_destino = 0
        contador_celdas_negras_lista_destino = 0
        actual = self.primero  # recorrerá la lista de celdas origen
        actual2 = lista_celdas_destino.primero  # recorrerá la lista destino
        # se contarán si existen el mismo número de cuadros del mismo color en ambas listas

        solucion_intercambios_simples = ""
        solucion_volteando_celdas = ""

        coste_volteando_celdas = 0
        coste_intercambios_simples = 0

        while actual is not None and actual2 is not None:
            if actual.celda.color:
                contador_celdas_blancas_lista_origen += 1
            else:
                contador_celdas_negras_lista_origen += 1

            if actual2.celda.color:
                contador_celdas_blancas_lista_destino += 1
            else:
                contador_celdas_negras_lista_destino += 1

            actual = actual.siguiente
            actual2 = actual2.siguiente

            # se considera si debemos girar más de alguna celda
        if contador_celdas_negras_lista_origen == contador_celdas_negras_lista_destino and contador_celdas_blancas_lista_origen and contador_celdas_blancas_lista_destino:
            #print("no hay necesidad de voltear celdas")
            self.solucionar(lista_celdas_destino, costo_switch)
            solucion_volteando_celdas = lista_origen.voltear_todas(lista_celdas_destino, costo_flip)
            if coste_volteando_celdas < coste_intercambios_simples or coste_volteando_celdas == coste_intercambios_simples:
                print("Para visualizar los pasos para resolver la matriz usted debe de escoger una opción:")
                print(
                    "Si desea ver la solución paso a paso en consola ingrese la letra 'c', si desea verla en un archivo.txt ingrese la letra 't' ")
                opcion = input()

                if opcion == "c":
                    print(solucion_volteando_celdas)
                    FuncionCelda.Imprimir_lineales(lista_origen2, lista_celdas_destino)
                elif opcion == "t":
                    Manejo_archivos.Crear_Instrucciones(solucion_volteando_celdas)
                    FuncionCelda.Imprimir_lineales(lista_origen2, lista_celdas_destino)

            elif coste_volteando_celdas > coste_intercambios_simples:
                print("Para visualizar los pasos para resolver la matriz usted debe de escoger una opción:")
                print(
                    "Si desea ver la solución paso a paso en consola ingrese la letra 'c', si desea verla en un archivo.txt ingrese la letra 't' ")
                opcion = input()

                if opcion == "c":
                    print(solucion_intercambios_simples)
                    FuncionCelda.Imprimir_lineales(lista_origen2, lista_celdas_destino)
                elif opcion == "t":
                    Manejo_archivos.Crear_Instrucciones(solucion_intercambios_simples)
                    FuncionCelda.Imprimir_lineales(lista_origen2, lista_celdas_destino)



        else:
            #print("se necesitan voltear celdas")
            self.solucionar(lista_celdas_destino, costo_switch)
            solucion_volteando_celdas = self.voltear_todas(lista_celdas_destino, costo_flip)
            solucion_combinada = solucion_intercambios_simples + solucion_volteando_celdas
            coste_combinado = coste_volteando_celdas + coste_intercambios_simples
            coste_volteando_celdas = 0
            solucion_volteando_celdas = ""
            lista_origen.voltear_todas(lista_celdas_destino, costo_flip)
            if coste_combinado < coste_volteando_celdas or coste_combinado == coste_volteando_celdas:
                print("Para visualizar los pasos para resolver la matriz usted debe de escoger una opción:")
                print(
                    "Si desea ver la solución paso a paso en consola ingrese la letra 'c', si desea verla en un archivo.txt ingrese la letra 't' ")
                opcion = input()

                if opcion == "c":
                    print(solucion_combinada)
                    FuncionCelda.Imprimir_lineales(lista_origen2, lista_celdas_destino)
                elif opcion == "t":
                    Manejo_archivos.Crear_Instrucciones(solucion_combinada)
                    FuncionCelda.Imprimir_lineales(lista_origen2, lista_celdas_destino)


            elif coste_combinado > coste_volteando_celdas:
                print("Para visualizar los pasos para resolver la matriz usted debe de escoger una opción:")
                print(
                    "Si desea ver la solución paso a paso en consola ingrese la letra 'c', si desea verla en un archivo.txt ingrese la letra 't' ")
                opcion = input()

                if opcion == "c":
                    print(solucion_volteando_celdas)
                    FuncionCelda.Imprimir_lineales(lista_origen2, lista_celdas_destino)
                elif opcion == "t":
                    Manejo_archivos.Crear_Instrucciones(solucion_volteando_celdas)
                    FuncionCelda.Imprimir_lineales(lista_origen2, lista_celdas_destino)

    def solucionar(self, lista_celdas_destino, costo_switch):
        global coste_intercambios_simples, solucion_intercambios_simples, voltear_necesario
        cantidad_cambios = 0
        actual = self.primero
        actual2 = lista_celdas_destino.primero
        primer_celda_erronea = None
        segunda_celda_erronea = None
        while actual and actual2:

            if actual.celda.color != actual2.celda.color:
                if primer_celda_erronea is None:
                    primer_celda_erronea = actual
                else:
                    if actual.celda.color != primer_celda_erronea.celda.color:
                        segunda_celda_erronea = actual
                        break
            actual = actual.siguiente
            actual2 = actual2.siguiente

        if segunda_celda_erronea is None or primer_celda_erronea is None:
            voltear_necesario = True
            return

            # al tratarse de filas sabemos que la distancia entre ellas es ydestino - yinicio

        if segunda_celda_erronea.celda.y - primer_celda_erronea.celda.y == 1:
            segunda_celda_erronea.celda.color = not segunda_celda_erronea.celda.color
            primer_celda_erronea.celda.color = not primer_celda_erronea.celda.color
            coste_intercambios_simples += costo_switch
            solucion_intercambios_simples += "La celda en la fila: " + str(
                primer_celda_erronea.celda.x) + " y columna: " + str(
                primer_celda_erronea.celda.y) + " ha sido intercambiada por la celda en la fila: " + str(
                segunda_celda_erronea.celda.x) + " y columna: " + str(
                segunda_celda_erronea.celda.y) + " el coste acumulado es de: " + str(coste_intercambios_simples) + "\n"
            cantidad_cambios += 1
        else:
            camino_entre_celdas = Tablero_Lineal()
            while primer_celda_erronea.celda.y <= segunda_celda_erronea.celda.y:
                camino_entre_celdas.insertar(primer_celda_erronea.celda)
                primer_celda_erronea = primer_celda_erronea.siguiente
                if primer_celda_erronea is None:
                    break
            # Analizamos el camino que se ha formado

            actual_camino = camino_entre_celdas.primero.siguiente
            camino_de_un_mismo_color = False
            color_actual = actual_camino.celda.color
            while actual_camino:
                if actual_camino.celda.y == camino_entre_celdas.ultimo.celda.y:
                    break
                if actual_camino.celda.color != color_actual:
                    camino_de_un_mismo_color = False
                    break
                else:
                    camino_de_un_mismo_color = True

                actual_camino = actual_camino.siguiente

                if actual_camino.celda.y == camino_entre_celdas.ultimo.celda.y:
                    break

            if camino_de_un_mismo_color:
                if color_actual:
                    #print("el color del camino es todo blanco")
                    if camino_entre_celdas.primero.celda.color != color_actual:
                        #print("recorrer todo el camino de izquierda a derecha. Moviendo la celda origen a la celda destino")
                        Nodo_izquierda_derecha = camino_entre_celdas.primero
                        while Nodo_izquierda_derecha:
                            coste_intercambios_simples += costo_switch
                            solucion_intercambios_simples += "La celda en la fila: " + str(
                                Nodo_izquierda_derecha.celda.x) + " y columna: " + str(
                                Nodo_izquierda_derecha.celda.y) + " ha sido intercambiada por la celda en la fila: " + str(
                                Nodo_izquierda_derecha.siguiente.celda.x) + " y columna: " + str(
                                Nodo_izquierda_derecha.siguiente.celda.y) + " el coste acumulado es de: " + str(
                                coste_intercambios_simples) + "\n"
                            cantidad_cambios += 1
                            Nodo_izquierda_derecha = Nodo_izquierda_derecha.siguiente
                            if Nodo_izquierda_derecha.siguiente is None:
                                break
                        camino_entre_celdas.primero.celda.color = not camino_entre_celdas.primero.celda.color
                        camino_entre_celdas.ultimo.celda.color = not camino_entre_celdas.ultimo.celda.color

                    else:
                        #print("recorrer el camino de derecha a izquierda. Moviendo la celda destino a la celda origen")
                        Nodo_derecha_izquierda = camino_entre_celdas.ultimo
                        while Nodo_derecha_izquierda:
                            coste_intercambios_simples += costo_switch
                            solucion_intercambios_simples += "La celda en la fila: " + str(
                                Nodo_derecha_izquierda.celda.x) + " y columna: " + str(
                                Nodo_derecha_izquierda.celda.y) + " ha sido intercambiada por la celda en la fila: " + str(
                                Nodo_derecha_izquierda.anterior.celda.x) + " y columna: " + str(
                                Nodo_derecha_izquierda.anterior.celda.y) + " el coste acumulado es de: " + str(
                                coste_intercambios_simples) + "\n"
                            cantidad_cambios += 1
                            Nodo_derecha_izquierda = Nodo_derecha_izquierda.anterior
                            if Nodo_derecha_izquierda.anterior is None:
                                break
                        camino_entre_celdas.primero.celda.color = not camino_entre_celdas.primero.celda.color
                        camino_entre_celdas.ultimo.celda.color = not camino_entre_celdas.ultimo.celda.color


                else:
                    #print("el color del camino es todo negro")
                    if camino_entre_celdas.primero.celda.color != color_actual:
                        #print( "recorrer todo el camino de izquierda a derecha. Moviendo la celda origen a la celda destino")
                        Nodo_izquierda_derecha = camino_entre_celdas.primero
                        while Nodo_izquierda_derecha:
                            coste_intercambios_simples += costo_switch
                            solucion_intercambios_simples += "La celda en la fila: " + str(
                                Nodo_izquierda_derecha.celda.x) + " y columna: " + str(
                                Nodo_izquierda_derecha.celda.y) + " ha sido intercambiada por la celda en la fila: " + str(
                                Nodo_izquierda_derecha.siguiente.celda.x) + " y columna: " + str(
                                Nodo_izquierda_derecha.siguiente.celda.y) + " el coste acumulado es de: " + str(
                                coste_intercambios_simples) + "\n"
                            cantidad_cambios += 1
                            Nodo_izquierda_derecha = Nodo_izquierda_derecha.siguiente
                            if Nodo_izquierda_derecha.siguiente is None:
                                break

                        camino_entre_celdas.primero.celda.color = not camino_entre_celdas.primero.celda.color
                        camino_entre_celdas.ultimo.celda.color = not camino_entre_celdas.ultimo.celda.color

                    else:
                        #print("recorrer el camino de derecha a izquierda. Moviendo la celda destino a la celda origen")
                        Nodo_derecha_izquierda = camino_entre_celdas.ultimo
                        while Nodo_derecha_izquierda:
                            coste_intercambios_simples += costo_switch
                            solucion_intercambios_simples += "La celda en la fila: " + str(
                                Nodo_derecha_izquierda.celda.x) + " y columna: " + str(
                                Nodo_derecha_izquierda.celda.y) + " ha sido intercambiada por la celda en la fila: " + str(
                                Nodo_derecha_izquierda.anterior.celda.x) + " y columna: " + str(
                                Nodo_derecha_izquierda.anterior.celda.y) + " el coste acumulado es de: " + str(
                                coste_intercambios_simples) + "\n"
                            cantidad_cambios += 1
                            Nodo_derecha_izquierda = Nodo_derecha_izquierda.anterior
                            if Nodo_derecha_izquierda.anterior is None:
                                break

                        camino_entre_celdas.primero.celda.color = not camino_entre_celdas.primero.celda.color
                        camino_entre_celdas.ultimo.celda.color = not camino_entre_celdas.ultimo.celda.color



            else:
                #print("el color del camino si cambia")
                celda_origen = camino_entre_celdas.primero
                celda_destino = None

                actual_nodo_camino_celdas = camino_entre_celdas.primero

                while actual_nodo_camino_celdas:
                    if actual_nodo_camino_celdas.celda.color != celda_origen.celda.color:
                        celda_destino = actual_nodo_camino_celdas
                        break
                    actual_nodo_camino_celdas = actual_nodo_camino_celdas.siguiente

                if celda_origen is None or celda_destino is None:
                    voltear_necesario = True
                    return
                # asegurarnos que la celda destino no sea none
                if celda_destino.celda.y - celda_origen.celda.y == 1:
                    celda_destino.celda.color = not celda_destino.celda.color
                    celda_origen.celda.color = not celda_origen.celda.color
                    coste_intercambios_simples += costo_switch
                    solucion_intercambios_simples += "La celda en la fila: " + str(
                        celda_origen.celda.x) + " y columna: " + str(
                        celda_origen.celda.y) + " ha sido intercambiada por la celda en la fila: " + str(
                        celda_destino.celda.x) + " y columna: " + str(
                        celda_destino.celda.y) + " el coste acumulado es de: " + str(
                        coste_intercambios_simples) + "\n"
                    cantidad_cambios += 1

                else:
                    subcamino = Tablero_Lineal()

                    while celda_origen.celda.y <= celda_destino.celda.y:
                        subcamino.insertar(celda_origen.celda)

                        celda_origen = celda_origen.siguiente

                    actual_sub_camino = camino_entre_celdas.primero.siguiente

                    camino_de_un_mismo_color2 = False
                    color_actual2 = actual_sub_camino.celda.color
                    while actual_sub_camino:
                        if actual_sub_camino.celda.y == subcamino.ultimo.celda.y:
                            break
                        if actual_sub_camino.celda.color != color_actual2:
                            camino_de_un_mismo_color2 = False
                            break
                        else:
                            camino_de_un_mismo_color2 = True

                        actual_sub_camino = actual_sub_camino.siguiente

                        if actual_sub_camino.celda.y == subcamino.ultimo.celda.y:
                            break

                    if camino_de_un_mismo_color2:
                        if color_actual2:
                            # print("el color del camino es todo blanco")
                            if subcamino.primero.celda.color != color_actual2:
                                # print(
                                #   "recorrer todo el camino de izquierda a derecha. Moviendo la celda origen a la celda destino")
                                Nodo_izq_der = subcamino.primero
                                while Nodo_izq_der:
                                    coste_intercambios_simples += costo_switch
                                    solucion_intercambios_simples += "La celda en la fila: " + str(
                                        Nodo_izq_der.celda.x) + " y columna: " + str(
                                        Nodo_izq_der.celda.y) + " ha sido intercambiada por la celda en la fila: " + str(
                                        Nodo_izq_der.siguiente.celda.x) + " y columna: " + str(
                                        Nodo_izq_der.siguiente.celda.y) + " el coste acumulado es de: " + str(
                                        coste_intercambios_simples) + "\n"
                                    cantidad_cambios += 1
                                    Nodo_izq_der = Nodo_izq_der.siguiente
                                    if Nodo_izq_der.siguiente is None:
                                        break
                                camino_entre_celdas.primero.celda.color = not camino_entre_celdas.primero.celda.color
                                camino_entre_celdas.ultimo.celda.color = not camino_entre_celdas.ultimo.celda.color

                            else:
                               # print("recorrer el camino de derecha a izquierda. Moviendo la celda destino a la celda origen")
                                Nodo_der_izq = subcamino.ultimo
                                while Nodo_der_izq:
                                    coste_intercambios_simples += costo_switch
                                    solucion_intercambios_simples += "La celda en la fila: " + str(
                                        Nodo_der_izq.celda.x) + " y columna: " + str(
                                        Nodo_der_izq.celda.y) + " ha sido intercambiada por la celda en la fila: " + str(
                                        Nodo_der_izq.anterior.celda.x) + " y columna: " + str(
                                        Nodo_der_izq.anterior.celda.y) + " el coste acumulado es de: " + str(
                                        coste_intercambios_simples) + "\n"
                                    cantidad_cambios += 1
                                    Nodo_der_izq = Nodo_der_izq.anterior
                                    if Nodo_der_izq.anterior is None:
                                        break
                                subcamino.primero.celda.color = not subcamino.primero.celda.color
                                subcamino.ultimo.celda.color = not subcamino.ultimo.celda.color


                        else:
                            #print("el color del camino es todo negro")
                            if subcamino.primero.celda.color != color_actual2:
                                #print("recorrer todo el camino de izquierda a derecha. Moviendo la celda origen a la celda destino")
                                Nodo_izq_der = subcamino.primero
                                while Nodo_izq_der:
                                    coste_intercambios_simples += costo_switch
                                    solucion_intercambios_simples += "La celda en la fila: " + str(
                                        Nodo_izq_der.celda.x) + " y columna: " + str(
                                        Nodo_izq_der.celda.y) + " ha sido intercambiada por la celda en la fila: " + str(
                                        Nodo_izq_der.siguiente.celda.x) + " y columna: " + str(
                                        Nodo_izq_der.siguiente.celda.y) + " el coste acumulado es de: " + str(
                                        coste_intercambios_simples) + "\n"
                                    cantidad_cambios += 1
                                    Nodo_izq_der = Nodo_izq_der.siguiente
                                    if Nodo_izq_der.siguiente is None:
                                        break

                                subcamino.primero.celda.color = not subcamino.primero.celda.color
                                subcamino.ultimo.celda.color = not subcamino.ultimo.celda.color

                            else:
                                #print("recorrer el camino de derecha a izquierda. Moviendo la celda destino a la celda origen")
                                Nodo_der_izq = subcamino.ultimo
                                while Nodo_der_izq:
                                    coste_intercambios_simples += costo_switch
                                    solucion_intercambios_simples += "La celda en la fila: " + str(
                                        Nodo_der_izq.celda.x) + " y columna: " + str(
                                        Nodo_der_izq.celda.y) + " ha sido intercambiada por la celda en la fila: " + str(
                                        Nodo_der_izq.anterior.celda.x) + " y columna: " + str(
                                        Nodo_der_izq.anterior.celda.y) + " el coste acumulado es de: " + str(
                                        coste_intercambios_simples) + "\n"
                                    cantidad_cambios += 1
                                    Nodo_der_izq = Nodo_der_izq.anterior
                                    if Nodo_der_izq.anterior is None:
                                        break

                                subcamino.primero.celda.color = not subcamino.primero.celda.color
                                subcamino.ultimo.celda.color = not subcamino.ultimo.celda.color

        if cantidad_cambios > 0:
            #print(solucion_intercambios_simples)
            self.solucionar(lista_celdas_destino, costo_switch)


        elif cantidad_cambios == 0:
            return

    def voltear_todas(self, lista_celdas_destino, costo_flip):
        global coste_volteando_celdas
        solucion_volteando_celdas = ""
        actual = self.primero
        actual2 = lista_celdas_destino.primero
        while actual and actual2:
            if actual.celda.color != actual2.celda.color:
                coste_volteando_celdas += costo_flip
                actual.celda.color = not actual.celda.color
                solucion_volteando_celdas += "Se ha volteado la celda con fila x: " + str(actual.celda.x
                                                                                          ) + " y columna: " + str(
                    actual.celda.y) + " el coste es: " + str(coste_volteando_celdas) + "\n"

            actual = actual.siguiente
            actual2 = actual2.siguiente

        return solucion_volteando_celdas

    def count_white(self):
        actual = self.primero
        contador = 0
        while actual:
            if actual.celda.color:
                contador += 1

            actual = actual.siguiente
        return contador

    def count_black(self):
        actual = self.primero
        contador = 0
        while actual:
            if not actual.celda.color:
                contador += 1

            actual = actual.siguiente
        return contador

    def comparar_listas(self, lista_celdas_destino):
        iguales = False
        actual = self.primero
        actual2 = lista_celdas_destino.primero
        while actual and actual2:
            if actual.celda.color == actual2.celda.color:
                iguales = True
            else:
                iguales = False
                break
            actual = actual.siguiente
            actual2 = actual2.siguiente
        return iguales
