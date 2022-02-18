from graphviz import render
from PIL import Image


def MostrarCeldas(Patron, Piso):
    filas = Piso.piso.rows
    columnas = Piso.piso.columns

    contador_filas = 0
    contador_columnas = 0

    texto_patron = Patron.patron.string_patron
    cadena = '''  
digraph html {
 tabla [shape=none, margin=0, label=<
 <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="10">
    '''
    cadena += "<TR>\n"

    for letra in texto_patron:

        if letra == "W":
            cadena += " <TD> </TD>\n"
            contador_columnas += 1
        elif letra == "B":
            cadena += ' <TD BGCOLOR="black"> </TD>\n'
            contador_columnas += 1

        if contador_columnas == columnas:
            contador_filas += 1
            cadena += "</TR>\n"
            if contador_filas < filas:
                cadena += "<TR>\n"
            contador_columnas = 0

    cadena += '</TABLE>>];}  '

    archivo_nuevo = open("grafica.dot", "w")
    archivo_nuevo.write(cadena)
    archivo_nuevo.close()

    render("dot", "png", "grafica.dot")

    im = Image.open(r"grafica.dot.png")

    im.show()
