from NodoCelda import NodoCelda
from Manejo_archivos import Crear_Instrucciones
from copy import deepcopy
import FuncionCelda


coste_intercambios_simples = 0
solucion_intercambios_simples = ""
solucion_volteando_celdas = ""
coste_volteando_celdas = 0
lista_origen = None


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
        actual = self.primero #recorrerá la lista de celdas origen
        actual2 = lista_celdas_destino.primero #recorrerá la lista destino
        #se contarán si existen el mismo número de cuadros del mismo color en ambas listas

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

                #se considera si debemos girar más de alguna celda
        if contador_celdas_negras_lista_origen == contador_celdas_negras_lista_destino and contador_celdas_blancas_lista_origen and contador_celdas_blancas_lista_destino:
            #se prioriza hacer los intercambios
            #esta funcion debe de retornar el coste total de resolver la matriz lineal con solo intercambios

            solucion_intercambios_simples += self.hacer_intercambios_lineales_derecha(lista_celdas_destino, costo_switch)

            if not self.comparar_listas(lista_celdas_destino):
                solucion_intercambios_simples += self.hacer_intercambios_lineales_izquierda(lista_celdas_destino, costo_switch)

            if not self.comparar_listas(lista_celdas_destino):
                solucion_intercambios_simples += self.cambio_minimo(lista_celdas_destino, costo_switch)
                solucion_intercambios_simples += self.hacer_intercambios_lineales_derecha(lista_celdas_destino, costo_switch)
                solucion_intercambios_simples += self.hacer_intercambios_lineales_izquierda(lista_celdas_destino, costo_switch)


            solucion_volteando_celdas += lista_origen.voltear_todas(lista_celdas_destino, costo_flip)

            if coste_volteando_celdas < coste_intercambios_simples:
                print("¿desea ver las instrucciones para solucionar este problema en la consola o lo desea en un archivo .txt?\nSi desea ver las instrucciones en consola ingrese la letra 'c' , si deseas tenerlas en un archivo .txt ingrese la letra 't' ")
                print("si no desea ninguna de las opciones ingrese cualquier caracter")
                opcion = input()
                if opcion == "c":
                    print(solucion_volteando_celdas)
                    FuncionCelda.Imprimir_lineales(lista_origen2, lista_celdas_destino)
                elif opcion == "t":
                    Crear_Instrucciones(solucion_volteando_celdas)
                    FuncionCelda.Imprimir_lineales(lista_origen2, lista_celdas_destino)


            elif coste_volteando_celdas == coste_intercambios_simples:
                print("¿desea ver las instrucciones para solucionar este problema en la consola o lo desea en un archivo .txt?\nSi desea ver las instrucciones en consola ingrese la letra 'c' , si deseas tenerlas en un archivo .txt ingrese la letra 't' ")
                print("si no desea ninguna de las opciones ingrese cualquier caracter")
                opcion = input()
                if opcion == "c":
                    print(solucion_volteando_celdas)
                    FuncionCelda.Imprimir_lineales(lista_origen2, lista_celdas_destino)
                elif opcion == "t":
                    Crear_Instrucciones(solucion_volteando_celdas)
                    FuncionCelda.Imprimir_lineales(lista_origen2, lista_celdas_destino)
            elif coste_volteando_celdas > coste_intercambios_simples:
                print( "¿desea ver las instrucciones para solucionar este problema en la consola o lo desea en un archivo .txt?\nSi desea ver las instrucciones en consola ingrese la letra 'c' , si deseas tenerlas en un archivo .txt ingrese la letra 't' ")
                print("si no desea ninguna de las opciones ingrese cualquier caracter")
                opcion = input()
                if opcion == "c":
                    print(solucion_intercambios_simples)
                    FuncionCelda.Imprimir_lineales(lista_origen2, lista_celdas_destino)
                elif opcion == "t":
                    Crear_Instrucciones(solucion_intercambios_simples)
                    FuncionCelda.Imprimir_lineales(lista_origen2, lista_celdas_destino)



            #posteriormente se van a comparar si solamente giramos todas las celdas

        else:
            print("se necesitan voltear celdas")
            solucion_intercambios_simples += self.hacer_intercambios_lineales_derecha(lista_celdas_destino, costo_switch)
            solucion_intercambios_simples += self.hacer_intercambios_lineales_izquierda(lista_celdas_destino, costo_switch)
            solucion_volteando_celdas += self.voltear_todas(lista_celdas_destino, costo_flip)

            solucion_total = solucion_intercambios_simples + solucion_volteando_celdas
            costo_total = coste_volteando_celdas + coste_intercambios_simples

            coste_volteando_celdas = 0
            solucion_volteando_celdas = ""

            lista_origen.voltear_todas(lista_celdas_destino, costo_flip)

            if costo_total < coste_volteando_celdas:
                print("¿desea ver las instrucciones para solucionar este problema en la consola o lo desea en un archivo .txt?\nSi desea ver las instrucciones en consola ingrese la letra 'c' , si deseas tenerlas en un archivo .txt ingrese la letra 't' ")
                print("si no desea ninguna de las opciones ingrese cualquier caracter")
                opcion = input()
                if opcion == "c":
                    print(solucion_total)
                    FuncionCelda.Imprimir_lineales(lista_origen2, lista_celdas_destino)
                elif opcion == "t":
                    Crear_Instrucciones(solucion_total)
                    FuncionCelda.Imprimir_lineales(lista_origen2, lista_celdas_destino)

            elif costo_total > coste_volteando_celdas or costo_total == coste_volteando_celdas:
                print("¿desea ver las instrucciones para solucionar este problema en la consola o lo desea en un archivo .txt?\nSi desea ver las instrucciones en consola ingrese la letra 'c' , si deseas tenerlas en un archivo .txt ingrese la letra 't' ")
                print("si no desea ninguna de las opciones ingrese cualquier caracter")
                opcion = input()
                if opcion == "c":
                    print(solucion_volteando_celdas)
                    FuncionCelda.Imprimir_lineales(lista_origen2, lista_celdas_destino)
                elif opcion == "t":
                    Crear_Instrucciones(solucion_volteando_celdas)
                    FuncionCelda.Imprimir_lineales(lista_origen2, lista_celdas_destino)

    def hacer_intercambios_lineales_izquierda(self, lista_celdas_destino, costo_switch):
        global coste_intercambios_simples
        solucion_intercambios_simples = ""
        actual = self.ultimo
        actual2 = lista_celdas_destino.ultimo
        while actual is not None and actual2 is not None:

            if actual.celda.color != actual2.celda.color: #aqui se va a verificar que las celdas estén en una mala posición
                if actual.anterior is not None and actual2.anterior is not None and actual.siguiente is not None and actual2.siguiente is not None: #aqui nos aseguramos de no solicitar atributo nulo al final de la lista lineal y que no sea una celda al borde de la matriz
                    if actual.celda.color != actual.anterior.celda.color:
                        coste_intercambios_simples += costo_switch
                        solucion_intercambios_simples += "la celda con fila: " + str(actual.celda.x) + " y columna: " + str(
                            actual.celda.y) + " ha sido intercambiada con la celda con fila: " + str(
                            actual.anterior.celda.x) + " y columna: " + str(actual.anterior.celda.y) + " el coste es: " + str(coste_intercambios_simples) + "\n"

                        actual.celda.color = not actual.celda.color
                        actual.anterior.celda.color = not actual.anterior.celda.color
                        #ultima celda
                elif actual.siguiente is None and actual2.siguiente is None:
                    if actual.celda.color != actual.anterior.celda.color:
                        coste_intercambios_simples += costo_switch
                        solucion_intercambios_simples += "la celda con fila: " + str(actual.celda.x) + " y columna: " + str(
                            actual.celda.y) + " ha sido intercambiada con la celda con fila: " + str(
                            actual.anterior.celda.x) + " y columna: " + str(
                            actual.anterior.celda.y) + " el coste es: " + str(coste_intercambios_simples) + "\n"
                        actual.celda.color = not actual.celda.color
                        actual.anterior.celda.color = not actual.anterior.celda.color
            else:
                #si la casilla está bien se procede a avanzar
                actual = actual.anterior
                actual2 = actual2.anterior
                continue


            actual = actual.anterior
            actual2 = actual2.anterior

        #print("matriz origen\n")
        #self.recorrer()
        #print("matriz destino\n")
        #lista_celdas_destino.recorrer()

        #print(solucion_intercambios_simples)

        return solucion_intercambios_simples

    def hacer_intercambios_lineales_derecha(self, lista_celdas_destino, costo_switch):
        global coste_intercambios_simples
        solucion_intercambios_simples = ""
        actual = self.primero
        actual2 = lista_celdas_destino.primero
        while actual is not None and actual2 is not None:

            if actual.celda.color != actual2.celda.color:  # aqui se va a verificar que las celdas estén en una mala posición
                # aqui irá la lógica cuando una celda está mal
                if actual.siguiente is not None and actual2.siguiente is not None and actual.anterior is not None and actual2.anterior is not None:  # aqui nos aseguramos de no solicitar atributo nulo al final de la lista lineal y que no sea una celda al borde de la matriz
                    if actual.celda.color != actual.siguiente.celda.color:
                        coste_intercambios_simples += costo_switch
                        solucion_intercambios_simples += "la celda con fila: " + str(
                            actual.celda.x) + " y columna: " + str(
                            actual.celda.y) + " ha sido intercambiada con la celda con fila: " + str(
                            actual.siguiente.celda.x) + " y columna: " + str(
                            actual.siguiente.celda.y) + " el coste es: " + str(coste_intercambios_simples) + "\n"

                        actual.celda.color = not actual.celda.color
                        actual.siguiente.celda.color = not actual.siguiente.celda.color
                # es la celda inicial
                elif actual.anterior is None and actual2.anterior is None:
                    if actual.celda.color != actual.siguiente.celda.color:
                        coste_intercambios_simples += costo_switch
                        solucion_intercambios_simples += "la celda con fila: " + str(
                            actual.celda.x) + " y columna: " + str(
                            actual.celda.y) + " ha sido intercambiada con la celda con fila: " + str(
                            actual.siguiente.celda.x) + " y columna: " + str(
                            actual.siguiente.celda.y) + " el coste es: " + str(coste_intercambios_simples) + "\n"
                        actual.celda.color = not actual.celda.color
                        actual.siguiente.celda.color = not actual.siguiente.celda.color
            else:
                # si la casilla está bien se procede a avanzar
                actual = actual.siguiente
                actual2 = actual2.siguiente
                continue

            actual = actual.siguiente
            actual2 = actual2.siguiente
        #print("matriz origen\n")
        #self.recorrer()
        #print("matriz destino\n")
        #lista_celdas_destino.recorrer()

        #print(solucion_intercambios_simples)

        return solucion_intercambios_simples

    def cambio_minimo(self, lista_celdas_destino, costo_switch):
        global coste_intercambios_simples
        solucion_intercambios_simples = ""
        actual = self.primero
        actual2 = lista_celdas_destino.primero
        while actual and actual2:
            if actual.celda.color == actual2.celda.color and actual.celda.y == 0 and actual.celda.color != actual.siguiente.celda.color: #se encuentra en un inicio
                coste_intercambios_simples += costo_switch
                solucion_intercambios_simples += "la celda con fila: " + str(
                    actual.celda.x) + " y columna: " + str(
                    actual.celda.y) + " ha sido intercambiada con la celda con fila: " + str(
                    actual.siguiente.celda.x) + " y columna: " + str(
                    actual.siguiente.celda.y) + " el coste es: " + str(coste_intercambios_simples) + "\n"
                actual.celda.color = not actual.celda.color
                actual.siguiente.celda.color = not actual.siguiente.celda.color
            elif actual.celda.color == actual2.celda.color and actual.celda.y == self.size and actual.celda.color != actual.anterior.celda.color:  # se encuentra en un inicio
                coste_intercambios_simples += costo_switch
                solucion_intercambios_simples += "la celda con fila: " + str(actual.celda.x) + " y columna: " + str(
                    actual.celda.y) + " ha sido intercambiada con la celda con fila: " + str(
                    actual.anterior.celda.x) + " y columna: " + str(
                    actual.anterior.celda.y) + " el coste es: " + str(coste_intercambios_simples) + "\n"
                actual.celda.color = not actual.celda.color
                actual.anterior.celda.color = not actual.anterior.celda.color

            elif actual.celda.color == actual2.celda.color and actual.celda.y != self.size and actual.celda.y != 0 and actual.celda.color != actual.siguiente.celda.color:
                coste_intercambios_simples += costo_switch
                solucion_intercambios_simples += "la celda con fila: " + str(
                    actual.celda.x) + " y columna: " + str(
                    actual.celda.y) + " ha sido intercambiada con la celda con fila: " + str(
                    actual.siguiente.celda.x) + " y columna: " + str(
                    actual.siguiente.celda.y) + " el coste es: " + str(coste_intercambios_simples) + "\n"
                actual.celda.color = not actual.celda.color
                actual.siguiente.celda.color = not actual.siguiente.celda.color



            actual = actual.siguiente
            actual2 = actual2.siguiente

        #print("matriz origen\n")
        #self.recorrer()
        #print("matriz destino\n")
        #print(solucion_intercambios_simples)
        return solucion_intercambios_simples

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
                ) + " y columna: " + str(actual.celda.y) + " el coste es: " + str(coste_volteando_celdas) + "\n"


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


