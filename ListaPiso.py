from NodoPiso import NodoPiso


class ListaPiso:
    def __init__(self):
        self.primero = None

    def insertar(self, piso_ingresado):
        if self.primero is None:
            self.primero = NodoPiso(piso=piso_ingresado)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = NodoPiso(piso=piso_ingresado)

    def recorrer(self):
        actual = self.primero
        while actual is not None:
            print("nombre del piso : ", actual.piso.nombre, "las filas del piso son : ", actual.piso.rows,
                  "las columnas son: ", actual.piso.columns
                  , "el costo por voltear es: ", actual.piso.costo_flip, "el costo por cambio es: ",
                  actual.piso.costo_switch)
            print("los patrones pertenecientes son: ")
            actual.piso.patrones.recorrer()
            actual = actual.siguiente

    def Mostrar(self):
        contador = 1
        actual = self.primero
        print(
            "-----------Nombre del piso---------------------Filas---------------------Columnas-------------------precio por voltear azulejo--------------precio por intercambiar azulejos-----")
        while actual is not None:
            actual.piso.num = contador
            print(str(actual.piso.num) + ". " + actual.piso.nombre + "                                          " + str(
                actual.piso.rows) + "                           " + str(
                actual.piso.columns) + "                              " + str(
                actual.piso.costo_flip) + "                                      " + str(actual.piso.costo_switch))
            actual = actual.siguiente
            contador += 1

    def buscar(self, num):
        actual = self.primero
        while actual and actual.piso.num != num:
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
                if actual.piso.nombre > actual.siguiente.piso.nombre:
                    aux = actual.piso
                    actual.piso = actual.siguiente.piso
                    actual.siguiente.piso = aux
                    cambio = True
                actual = actual.siguiente


