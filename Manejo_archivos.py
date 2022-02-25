from os import startfile

def Crear_Instrucciones(texto_solucion):
    archivo = open("instrucciones.txt", "w")
    archivo.write(texto_solucion)
    archivo.close()
    startfile("instrucciones.txt")

