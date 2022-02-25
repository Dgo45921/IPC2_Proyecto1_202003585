from os import startfile, system


def MostrarCeldas(Patron, Piso):
    filas = Piso.piso.rows
    columnas = Piso.piso.columns

    contador_filas = 0
    contador_columnas = 0

    texto_patron = Patron.patron.string_patron
    cadena = '''  
digraph html {
 tabla [shape=none, margin=0, label=<
 <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="2.5" CELLPADDING="20">
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

    system("dot -Tpng " + "grafica.dot" + " -o " + "grafica.png")
    startfile("grafica.png")


def Imprimir_lineales(lista_origen, lista_destino):
    filas = 1
    columnas1 = lista_origen.size
    columnas2 = lista_destino.size

    contador_filas1 = 0
    contador_columnas1 = 0

    contador_filas2 = 0
    contador_columnas2 = 0



    actual = lista_origen.primero
    actual2 = lista_destino.primero
    texto_patron1 = ""
    texto_patron2 = ""

    while actual and actual2:
        if actual.celda.color:
            texto_patron1 += "W"
        else:
            texto_patron1 += "B"
        if actual2.celda.color:
            texto_patron2 += "W"
        else:
            texto_patron2 += "B"

        actual = actual.siguiente
        actual2 = actual2.siguiente







    cadena1 = '''  
    digraph html {
    labelloc="t";
    label="Patron origen";
     tabla [shape=none, margin=0, label=<
     <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="2.5" CELLPADDING="20">
        '''
    cadena1 += "<TR>\n"

    for letra in texto_patron1:

        if letra == "W":
            cadena1 += " <TD> </TD>\n"
            contador_columnas1 += 1
        elif letra == "B":
            cadena1 += ' <TD BGCOLOR="black"> </TD>\n'
            contador_columnas1 += 1

        if contador_columnas1 == columnas1:
            contador_filas1 += 1
            cadena1 += "</TR>\n"
            if contador_filas1 < filas:
                cadena1 += "<TR>\n"
            contador_columnas1 = 0

    cadena1 += '</TABLE>>];}  '

    archivo_nuevo = open("grafica_origen.dot", "w")
    archivo_nuevo.write(cadena1)
    archivo_nuevo.close()

    system("dot -Tpng " + "grafica_origen.dot" + " -o " + "grafica_origen.png")
    startfile("grafica_origen.png")








    cadena2 = '''  
        digraph html {
        labelloc="t";
    label="Patron destino";
         tabla [shape=none, margin=0, label=<
         <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="2.5" CELLPADDING="20">
            '''
    cadena2 += "<TR>\n"

    for letra in texto_patron2:

        if letra == "W":
            cadena2 += " <TD> </TD>\n"
            contador_columnas2 += 1
        elif letra == "B":
            cadena2 += ' <TD BGCOLOR="black"> </TD>\n'
            contador_columnas2 += 1

        if contador_columnas2 == columnas2:
            contador_filas2 += 1
            cadena2 += "</TR>\n"
            if contador_filas2 < filas:
                cadena2 += "<TR>\n"
            contador_columnas2 = 0

    cadena2 += '</TABLE>>];}  '

    archivo_nuevo = open("grafica_destino.dot", "w")
    archivo_nuevo.write(cadena2)
    archivo_nuevo.close()

    system("dot -Tpng " + "grafica_destino.dot" + " -o " + "grafica_destino.png")
    startfile("grafica_destino.png")



