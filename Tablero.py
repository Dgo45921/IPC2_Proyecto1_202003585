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
            print("coordenada x: ", actual.celda.x, "coordenada y: ", actual.celda.y, "color es: ", actual.celda.color, "posicion correcta es: ", actual.celda.posicion_correcta)
            actual = actual.siguiente
