import Costeo
from NodoCelda import NodoCelda


class Tablero:
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


    def resolver_lineal(self, lista_celdas_destino, costo_flip, costo_switch, filas, columnas):
        contador_celdas_blancas_lista_origen = 0
        contador_celdas_negras_lista_origen = 0
        contador_celdas_blancas_lista_destino = 0
        contador_celdas_negras_lista_destino = 0

        actual = self.primero #recorrerá la lista de celdas origen
        actual2 = lista_celdas_destino.primero #recorrerá la lista destino
        #se contarán si existen el mismo número de cuadros del mismo color en ambas listas
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

                #se considera si debemos girar más de alguna celda
        if contador_celdas_negras_lista_origen == contador_celdas_negras_lista_destino and contador_celdas_blancas_lista_origen and contador_celdas_blancas_lista_destino:
            print("no hay que volear celdas")
            #se prioriza hacer los intercambios
            #esta funcion debe de retornar el coste total de resolver la matriz lineal con solo intercambios
            costo_intercambio_simple = self.hacer_intercambios_lineales(lista_celdas_destino, costo_switch)
            #posteriormente se van a comparar si solamente giramos todas las celdas

        else:
            print("se necesitan voltear celdas")


    def hacer_intercambios_lineales(self, lista_celdas_destino, costo_switch):
        costo = 0
        cadena_solucion = ""
        actual = self.primero
        actual2 = lista_celdas_destino.primero
        while actual is not None and actual2 is not None:

            if actual.celda.color != actual2.celda.color: #aqui se va a verificar que las celdas estén en una mala posición
                #aqui irá la lógica cuando una celda está mal
                if actual.siguiente is not None and actual2.siguiente is not None and actual.anterior is not None and actual2.anterior is not None: #aqui nos aseguramos de no solicitar atributo nulo al final de la lista lineal y que no sea una celda al borde de la matriz
                    if actual.celda.color == actual2.siguiente.celda.color and actual.siguiente.celda.color == actual2.anterior.celda.color:
                        costo += costo_switch
                        cadena_solucion += "la celda con fila: " + str(actual.celda.x) + " y columna: " + str(
                            actual.celda.y) + " ha sido intercambiada con la celda con fila: " + str(
                            actual.siguiente.celda.x) + " y columna: " + str(actual.siguiente.celda.y) + " se llevan: " + str(Costeo.costo_final)
                        actual.celda.color = not actual.celda.color
                        actual.siguiente.celda.color = not actual.siguiente.celda.color
                #es la celda inicial
                elif actual.anterior is None and actual2.anterior is None:
                    if actual.celda.color != actual2.celda.color and actual2.siguiente.celda.color == actual.celda.color and actual.siguiente.celda.color == actual2.celda.color:
                        costo += costo_switch
                        cadena_solucion += "la celda con fila: " + str(actual.celda.x) + " y columna: " + str(
                            actual.celda.y) + " ha sido intercambiada con la celda con fila: " + str(
                            actual.siguiente.celda.x) + " y columna: " + str(
                            actual.siguiente.celda.y) + " se llevan: " + str(Costeo.costo_final)
                        actual.celda.color = not actual.celda.color
                        actual.siguiente.celda.color = not actual.siguiente.celda.color
            else:
                #si la casilla está bien se procede a avanzar
                actual = actual.siguiente
                actual2 = actual2.siguiente
                continue


            actual = actual.siguiente
            actual2 = actual2.siguiente
        print("matriz origen\n")
        self.recorrer()
        print("matriz destino\n")
        lista_celdas_destino.recorrer()

        print(cadena_solucion)
        return costo
