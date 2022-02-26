from NodoFila import NodoFila


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

    def Resolver(self, matriz_destino, filas, columnas, costo_flip, costo_switch):
        casillas_blancas_origen = self.count_white()
        casillas_negras_origen = self.count_black()
        casillas_blancas_destino = matriz_destino.count_white()
        casillas_negras_destino = matriz_destino.count_black()

        if casillas_negras_destino == casillas_negras_origen and casillas_blancas_destino == casillas_blancas_origen:
            print("no hay necesidad de hacer cambios")
            self.intercambios_arriba_abajo(matriz_destino, filas)


        else:
            print("se necesitan voltear casillas")


    def intercambios_arriba_abajo(self, matriz_destino, filas):
        fila_actual = self.primero
        fila_actual_destino = matriz_destino.primero
        cantidad_celdas_blancas_fila_actual = fila_actual.contenido_fila.count_white()
        cantidad_celdas_negras_fila_actual = fila_actual.contenido_fila.count_black()

        cantidad_celdas_blancas_fila_destino = fila_actual_destino.contenido_fila.count_white()
        cantidad_celdas_negras_fila_destino = fila_actual_destino.contenido_fila.count_black()

        while fila_actual.siguiente is not None:
            actual_celda1 = fila_actual.contenido_fila.primero # se comienza por la primera fila
            actual_celda2 = fila_actual.siguiente.contenido_fila.primero # se comienza la segunda fila
            actual_celda_correcta = fila_actual_destino.contenido_fila.primero # se comienza la primera fila de la matriz destino
            while actual_celda1 and actual_celda2:
                #recorriendo celdas de la matriz origen y destino


                if cantidad_celdas_blancas_fila_actual < cantidad_celdas_blancas_fila_destino:
                    print("se necesitan celdas blancas en la fila actual de la fila siguiente")

                    if actual_celda2.celda.color and not actual_celda1.celda.color:
                        actual_celda1.celda.color = not actual_celda1.celda.color
                        actual_celda2.celda.color = not actual_celda2.celda.color


                        print("la celda en la fila: ", actual_celda1.celda.x, " y columna: ", actual_celda1.celda.y,
                              " se ha intercambiado con la celda en la fila: "
                              , actual_celda2.celda.x, " y en la columna: ", actual_celda2.celda.y)

                        cantidad_celdas_blancas_fila_actual = fila_actual.contenido_fila.count_white()
                        cantidad_celdas_negras_fila_actual = fila_actual.contenido_fila.count_black()


                        actual_celda1 = actual_celda1.siguiente
                        actual_celda2 = actual_celda2.siguiente
                        actual_celda_correcta = actual_celda_correcta.siguiente

                        continue

                if cantidad_celdas_blancas_fila_actual > cantidad_celdas_blancas_fila_destino:

                    if not actual_celda2.celda.color and actual_celda1.celda.color:
                        actual_celda1.celda.color = not actual_celda1.celda.color
                        actual_celda2.celda.color = not actual_celda2.celda.color


                        print("la celda en la fila: ", actual_celda1.celda.x, " y columna: ", actual_celda1.celda.y,
                              " se ha intercambiado con la celda en la fila: "
                              , actual_celda2.celda.x, " y en la columna: ", actual_celda2.celda.y)

                        cantidad_celdas_blancas_fila_actual = fila_actual.contenido_fila.count_white()
                        cantidad_celdas_negras_fila_actual = fila_actual.contenido_fila.count_black()


                        actual_celda1 = actual_celda1.siguiente
                        actual_celda2 = actual_celda2.siguiente
                        actual_celda_correcta = actual_celda_correcta.siguiente
                        continue





                if cantidad_celdas_negras_fila_actual < cantidad_celdas_negras_fila_destino:
                    print("se necesitan celdas negras en la fila actual")

                    if not actual_celda2.celda.color and actual_celda1.celda.color:
                        actual_celda1.celda.color = not actual_celda1.celda.color
                        actual_celda2.celda.color = not actual_celda2.celda.color

                        print("la celda en la fila: ", actual_celda1.celda.x, " y columna: ", actual_celda1.celda.y,
                              " se ha intercambiado con la celda en la fila: "
                              , actual_celda2.celda.x, " y en la columna: ", actual_celda2.celda.y)

                        cantidad_celdas_blancas_fila_actual = fila_actual.contenido_fila.count_white()
                        cantidad_celdas_negras_fila_actual = fila_actual.contenido_fila.count_black()


                        actual_celda1 = actual_celda1.siguiente
                        actual_celda2 = actual_celda2.siguiente
                        actual_celda_correcta = actual_celda_correcta.siguiente
                        continue

                if cantidad_celdas_negras_fila_actual > cantidad_celdas_negras_fila_destino:
                    if actual_celda2.celda.color and not actual_celda1.celda.color:
                        actual_celda1.celda.color = not actual_celda1.celda.color
                        actual_celda2.celda.color = not actual_celda2.celda.color

                        print("la celda en la fila: ", actual_celda1.celda.x, " y columna: ", actual_celda1.celda.y,
                              " se ha intercambiado con la celda en la fila: "
                              , actual_celda2.celda.x, " y en la columna: ", actual_celda2.celda.y)

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
