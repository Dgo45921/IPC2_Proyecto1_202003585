from NodoCelda import NodoCelda


class ListaCelda:
    def __init__(self):
        self.primero = None

    def insertar(self, celda_ingresada):
        if self.primero is None:
            self.primero = NodoCelda(patron=celda_ingresada)
            return
        actual = self.primero
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = NodoCelda(patron=celda_ingresada)


    def recorrer(self):
        actual = self.primero
        while actual is not None:
            print("coordenada x: ", actual.x, "coordenada y: ", actual.y, "color es: ", actual.color)
            actual = actual.siguiente
