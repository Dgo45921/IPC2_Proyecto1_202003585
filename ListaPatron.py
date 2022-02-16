from NodoPatron import NodoPatron


class ListaPatron:
    def __init__(self):
        self.primero = None

    def insertar(self, patron_ingresado):
        if self.primero is None:
            self.primero = NodoPatron(patron=patron_ingresado)
            return
        aux = NodoPatron(patron=patron_ingresado)
        if aux.patron.codigo < self.primero.patron.codigo:
            aux.siguiente = self.primero
            self.primero = aux
            return
        else:
            actual = self.primero
            while actual.siguiente:
                if actual.siguiente.patron.codigo > aux.patron.codigo > actual.patron.codigo:
                    aux.siguiente = actual.siguiente
                    actual.siguiente = aux
                    break
                actual = actual.siguiente
            actual.siguiente = NodoPatron(patron=patron_ingresado)

    def recorrer(self):
        actual = self.primero
        while actual is not None:
            print("codigo del patron: ", actual.patron.codigo, "el string del patron es: ", actual.patron.string_patron)
            actual = actual.siguiente


    def Mostrar(self):
        actual = self.primero
        contador = 0
        cadena = ""
        while actual is not None:
            subcadena = "                                          " + str(contador) + "." + "codigo del patron:   " + actual.patron.codigo  + "\n"
            actual = actual.siguiente
            cadena += subcadena
            contador += 1

        return cadena
