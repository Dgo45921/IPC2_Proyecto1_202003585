from NodoPatron import NodoPatron


class ListaPatron:
    def __init__(self):
        self.primero = None

    def insertar(self, patron_ingresado):
        if self.primero is None:
            self.primero = NodoPatron(patron=patron_ingresado)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = NodoPatron(patron=patron_ingresado)

    def recorrer(self):
        actual = self.primero
        while actual is not None:
            print("codigo del patron: ", actual.patron.codigo, "el string del patron es: ", actual.patron.string_patron)
            actual = actual.siguiente


    def Mostrar(self):
        actual = self.primero
        contador = 1
        cadena = "--------------------Patrones disponibles-------------------------\n"

        while actual is not None:
            actual.patron.num = contador
            subcadena = str(actual.patron.num) + "." + "codigo del patron: " + actual.patron.codigo + "  cadena ingresada para el patron:  " + actual.patron.string_patron + "\n"
            actual = actual.siguiente
            cadena += subcadena
            contador += 1

        return cadena

    def Buscar(self, num):
        actual = self.primero
        while actual and actual.patron.num != num:
            actual = actual.siguiente

        if actual is not None:
            return actual
        else:
            return None

    def ordenar(self):
        if self.primero is None:
            return
        cambio = True
        actual = self.primero
        while cambio:
            cambio = False
            while actual is not None and actual.siguiente is not None:
                if actual.patron.codigo > actual.siguiente.patron.codigo:
                    aux = actual.patron
                    actual.patron = actual.siguiente.patron
                    actual.siguiente.patron = aux
                    cambio = True
                actual = actual.siguiente