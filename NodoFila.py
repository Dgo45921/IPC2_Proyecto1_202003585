class NodoFila:
    def __init__(self, indice,  contenido_fila, siguiente=None, anterior=None):
        self.indice = indice
        self.siguiente = siguiente
        self.anterior = anterior
        self.contenido_fila = contenido_fila
