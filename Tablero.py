from NodoFila import NodoFila
import Tablero_Lineal

solucion_intercambios_simples = ""
solucion_volteando_celdas = ""


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


    def Resolver(self, matriz_destino, filas, columnas, costo_flip, costo_switch):
        global solucion_intercambios_simples
        casillas_blancas_origen = self.count_white()
        casillas_negras_origen = self.count_black()
        casillas_blancas_destino = matriz_destino.count_white()
        casillas_negras_destino = matriz_destino.count_black()

        if casillas_negras_destino == casillas_negras_origen and casillas_blancas_destino == casillas_blancas_origen:
            print("no hay necesidad de hacer cambios")
            solucion_intercambios_simples += self.intercambios_arriba_abajo_estricto(matriz_destino, costo_switch)
            solucion_intercambios_simples += self.intercambios_arriba_abajo_no_estricto(matriz_destino, costo_switch)
            #solucion_intercambios_simples += self.intercambios_derecha_izquierda(matriz_destino, costo_switch)
            print(solucion_intercambios_simples)





        else:
            print("se necesitan voltear casillas")


    def intercambios_arriba_abajo_no_estricto(self, matriz_destino, costo_switch):

        cadena_solucion = ""
        fila_actual = self.primero
        fila_actual_destino = matriz_destino.primero


        while fila_actual.siguiente is not None:
            cantidad_celdas_blancas_fila_actual = fila_actual.contenido_fila.count_white()
            cantidad_celdas_negras_fila_actual = fila_actual.contenido_fila.count_black()

            cantidad_celdas_blancas_fila_destino = fila_actual_destino.contenido_fila.count_white()
            cantidad_celdas_negras_fila_destino = fila_actual_destino.contenido_fila.count_black()

            actual_celda1 = fila_actual.contenido_fila.primero # se comienza por la primera fila
            actual_celda2 = fila_actual.siguiente.contenido_fila.primero # se comienza la segunda fila
            actual_celda_correcta = fila_actual_destino.contenido_fila.primero # se comienza la primera fila de la matriz destino
            while actual_celda1 and actual_celda2:
                #recorriendo celdas de la matriz origen y destino


                if cantidad_celdas_blancas_fila_actual < cantidad_celdas_blancas_fila_destino:
                    print("se necesitan celdas blancas, exceso de celdas negras")

                    if actual_celda2.celda.color and not actual_celda1.celda.color:
                        actual_celda1.celda.color = not actual_celda1.celda.color
                        actual_celda2.celda.color = not actual_celda2.celda.color

                        Tablero_Lineal.coste_intercambios_simples += costo_switch

                        cadena_solucion += "la celda en la fila: " + str(actual_celda1.celda.x) + " y columna: "+ str(
                            actual_celda1.celda.y) + " se ha intercambiado con la celda en la fila: " + str(
                            actual_celda2.celda.x) + " y en la columna: " + str(actual_celda2.celda.y) + " el coste es de: " +str(Tablero_Lineal.coste_intercambios_simples) +"\n"


                        #print("la celda en la fila: ", actual_celda1.celda.x, " y columna: ", actual_celda1.celda.y,
                             # " se ha intercambiado con la celda en la fila: "
                             # , actual_celda2.celda.x, " y en la columna: ", actual_celda2.celda.y)

                        cantidad_celdas_blancas_fila_actual = fila_actual.contenido_fila.count_white()
                        cantidad_celdas_negras_fila_actual = fila_actual.contenido_fila.count_black()


                        actual_celda1 = actual_celda1.siguiente
                        actual_celda2 = actual_celda2.siguiente
                        actual_celda_correcta = actual_celda_correcta.siguiente

                        continue

                if cantidad_celdas_blancas_fila_actual > cantidad_celdas_blancas_fila_destino:
                    print("se necesitan celdas negras, exceso de celdas blancas")

                    if not actual_celda2.celda.color and actual_celda1.celda.color:
                        actual_celda1.celda.color = not actual_celda1.celda.color
                        actual_celda2.celda.color = not actual_celda2.celda.color
                        Tablero_Lineal.coste_intercambios_simples += costo_switch

                        cadena_solucion += "la celda en la fila: " + str(actual_celda1.celda.x) + " y columna: " + str(
                            actual_celda1.celda.y) + " se ha intercambiado con la celda en la fila: " + str(
                            actual_celda2.celda.x) + " y en la columna: " + str(
                            actual_celda2.celda.y) + " el coste es de: " + str(Tablero_Lineal.coste_intercambios_simples) + "\n"


                       # print("la celda en la fila: ", actual_celda1.celda.x, " y columna: ", actual_celda1.celda.y,
                              #" se ha intercambiado con la celda en la fila: "
                              #, actual_celda2.celda.x, " y en la columna: ", actual_celda2.celda.y)

                        cantidad_celdas_blancas_fila_actual = fila_actual.contenido_fila.count_white()
                        cantidad_celdas_negras_fila_actual = fila_actual.contenido_fila.count_black()


                        actual_celda1 = actual_celda1.siguiente
                        actual_celda2 = actual_celda2.siguiente
                        actual_celda_correcta = actual_celda_correcta.siguiente
                        continue


                if cantidad_celdas_negras_fila_actual < cantidad_celdas_negras_fila_destino:
                    print("se necesitan celdas negras, exceso de blancas")

                    if not actual_celda2.celda.color and actual_celda1.celda.color:
                        actual_celda1.celda.color = not actual_celda1.celda.color
                        actual_celda2.celda.color = not actual_celda2.celda.color

                        Tablero_Lineal.coste_intercambios_simples += costo_switch

                        cadena_solucion += "la celda en la fila: " + str(actual_celda1.celda.x) + " y columna: " + str(
                            actual_celda1.celda.y) + " se ha intercambiado con la celda en la fila: " + str(
                            actual_celda2.celda.x) + " y en la columna: " + str(
                            actual_celda2.celda.y) + " el coste es de: " + str(Tablero_Lineal.coste_intercambios_simples) + "\n"

                        #print("la celda en la fila: ", actual_celda1.celda.x, " y columna: ", actual_celda1.celda.y,
                              #" se ha intercambiado con la celda en la fila: "
                              #, actual_celda2.celda.x, " y en la columna: ", actual_celda2.celda.y)

                        cantidad_celdas_blancas_fila_actual = fila_actual.contenido_fila.count_white()
                        cantidad_celdas_negras_fila_actual = fila_actual.contenido_fila.count_black()


                        actual_celda1 = actual_celda1.siguiente
                        actual_celda2 = actual_celda2.siguiente
                        actual_celda_correcta = actual_celda_correcta.siguiente
                        continue

                if cantidad_celdas_negras_fila_actual > cantidad_celdas_negras_fila_destino:
                    print("se necesitan celdas blancas, exceso de negras")
                    if actual_celda2.celda.color and not actual_celda1.celda.color:
                        actual_celda1.celda.color = not actual_celda1.celda.color
                        actual_celda2.celda.color = not actual_celda2.celda.color

                        Tablero_Lineal.coste_intercambios_simples += costo_switch

                        cadena_solucion += "la celda en la fila: " + str(actual_celda1.celda.x) + " y columna: " + str(
                            actual_celda1.celda.y) + " se ha intercambiado con la celda en la fila: " + str(
                            actual_celda2.celda.x) + " y en la columna: " + str(
                            actual_celda2.celda.y) + " el coste es de: " + str(Tablero_Lineal.coste_intercambios_simples) + "\n"

                       # print("la celda en la fila: ", actual_celda1.celda.x, " y columna: ", actual_celda1.celda.y,
                              #" se ha intercambiado con la celda en la fila: "
                             # , actual_celda2.celda.x, " y en la columna: ", actual_celda2.celda.y)

                        cantidad_celdas_blancas_fila_actual = fila_actual.contenido_fila.count_white()
                        cantidad_celdas_negras_fila_actual = fila_actual.contenido_fila.count_black()

                        actual_celda1 = actual_celda1.siguiente
                        actual_celda2 = actual_celda2.siguiente
                        actual_celda_correcta = actual_celda_correcta.siguiente
                        continue




                actual_celda1 = actual_celda1.siguiente
                actual_celda2 = actual_celda2.siguiente
                actual_celda_correcta = actual_celda_correcta.siguiente

            fila_actual = fila_actual.siguiente
            fila_actual_destino = fila_actual_destino.siguiente


        print("matriz origen")
        self.recorrer()
        print("matriz destino")
        matriz_destino.recorrer()
        return cadena_solucion

    def intercambios_arriba_abajo_estricto(self, matriz_destino, costo_switch):

        cadena_solucion = ""
        fila_actual = self.primero
        fila_actual_destino = matriz_destino.primero


        while fila_actual.siguiente is not None:

            actual_celda1 = fila_actual.contenido_fila.primero # se comienza por la primera fila
            actual_celda2 = fila_actual.siguiente.contenido_fila.primero # se comienza la segunda fila
            actual_celda_correcta = fila_actual_destino.contenido_fila.primero # se comienza la primera fila de la matriz destino
            actual_celda_correcta2 = fila_actual_destino.siguiente.contenido_fila.primero  # se comienza la primera fila de la matriz destino
            while actual_celda1 and actual_celda2:
                #recorriendo celdas de la matriz origen y destino

                if actual_celda1.celda.color != actual_celda2.celda.color and actual_celda_correcta2.celda.color == actual_celda1.celda.color and actual_celda_correcta.celda.color == actual_celda2.celda.color:
                    actual_celda1.celda.color = not actual_celda1.celda.color
                    actual_celda2.celda.color = not actual_celda2.celda.color

                    Tablero_Lineal.coste_intercambios_simples += costo_switch

                    cadena_solucion += "la celda en la fila: " + str(actual_celda1.celda.x) + " y columna: " + str(
                        actual_celda1.celda.y) + " se ha intercambiado con la celda en la fila: " + str(
                        actual_celda2.celda.x) + " y en la columna: " + str(
                        actual_celda2.celda.y) + " el coste es de: " + str(
                        Tablero_Lineal.coste_intercambios_simples) + "\n"



                actual_celda1 = actual_celda1.siguiente
                actual_celda2 = actual_celda2.siguiente
                actual_celda_correcta = actual_celda_correcta.siguiente
                actual_celda_correcta2 = actual_celda_correcta2.siguiente


            fila_actual = fila_actual.siguiente
            fila_actual_destino = fila_actual_destino.siguiente


        print("matriz origen")
        self.recorrer()
        print("matriz destino")
        matriz_destino.recorrer()
        return cadena_solucion



    def intercambios_derecha_izquierda(self, matriz_destino, costo_switch):
        cadena_solucion = ""
        fila_actual = self.primero
        fila_actual_destino = matriz_destino.primero

        while fila_actual:
            actual_celda1 = fila_actual.contenido_fila  # se obtiene la priemra fila
            actual_celda_correcta = fila_actual_destino.contenido_fila  # se obtiene la fila correcta

            cadena_solucion += actual_celda1.hacer_intercambios_lineales_derecha(actual_celda_correcta, costo_switch)
            cadena_solucion += actual_celda1.hacer_intercambios_lineales_izquierda(actual_celda_correcta, costo_switch)




            fila_actual = fila_actual.siguiente
            fila_actual_destino = fila_actual_destino.siguiente

        return cadena_solucion

    def cambio_especial_filas(self, matriz_destino, costo_switch):
        cadena_solucion = ""
        fila_actual = self.primero
        fila_actual_destino = matriz_destino.primero

        while fila_actual:
            actual_celda1 = fila_actual.contenido_fila  # se obtiene la priemra fila
            actual_celda_correcta = fila_actual_destino.contenido_fila  # se obtiene la fila correcta
            estado = actual_celda1.comparar_listas(actual_celda_correcta)
            if not estado:
                cadena_solucion += actual_celda1.cambio_minimo(actual_celda_correcta, costo_switch)

            fila_actual = fila_actual.siguiente
            fila_actual_destino = fila_actual_destino.siguiente

        return cadena_solucion

    def chequear_resuelta(self, matriz_destino):

        fila_actual = self.primero
        fila_actual_destino = matriz_destino.primero
        while fila_actual and fila_actual_destino:
            lista_celdas = fila_actual.contenido_fila
            lista_celdas_destino = fila_actual_destino.contenido_fila
            estado = lista_celdas.comparar_listas(lista_celdas_destino)

            if not estado:
                break

            fila_actual = fila_actual.siguiente
            fila_actual_destino = fila_actual_destino.siguiente
        return estado



