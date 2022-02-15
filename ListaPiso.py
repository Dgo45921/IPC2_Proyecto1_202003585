from NodoPiso import NodoPiso


class ListaPiso:
    def __init__(self):
        self.primero = None

    def insertar(self, piso_ingresado):
        if self.primero is None:
            self.primero = NodoPiso(piso=piso_ingresado)
            return
        aux = NodoPiso(piso=piso_ingresado)
        if aux.piso.nombre < self.primero.piso.nombre:
            aux.siguiente = self.primero
            self.primero = aux
            return
        else:
            actual = self.primero
            while actual.siguiente:
                if actual.siguiente.piso.nombre > aux.piso.nombre > actual.piso.nombre:
                    aux.siguiente = actual.siguiente
                    actual.siguiente = aux
                    break
                actual = actual.siguiente
            actual.siguiente = NodoPiso(piso=piso_ingresado)



    def recorrer(self):
        actual = self.primero
        while actual is not None:
            print("nombre del piso : ", actual.piso.nombre, "las filas del piso son : ", actual.piso.rows, "las columnas son: ", actual.piso.columns
                  , "el costo por voltear es: ", actual.piso.costo_flip, "el costo por cambio es: ", actual.piso.costo_switch)
            print("los patrones pertenecientes son: ")
            actual.piso.patrones.recorrer()
            actual = actual.siguiente