import xml.etree.ElementTree as ET
from ListaPiso import ListaPiso
from ListaPatron import ListaPatron
from Piso import Piso
from Patron import Patron



lista_pisos = ListaPiso()
lista_patrones = None
datos_cargados = False



def Leer(ruta):
    global lista_patrones, lista_pisos, lista_celdas, datos_cargados
    try:
        arbol = ET.parse(ruta)
        raiz = arbol.getroot()

        for piso in raiz.findall("piso"):
            # print("El nombre del piso: ", piso.get("nombre"))
            # print("La cantidad de filas son: ", piso.find("R").text)
            # print("La cantidad de columnas son: ", piso.find("C").text)
            # print("La cantidad a pagar por flip es: ", piso.find("F").text)
            # print("La cantidad a pagar por switch es: ", piso.find("S").text)
            lista_patrones = ListaPatron()

            name = piso.get("nombre")
            rows = int(piso.find("R").text)
            columns = int(piso.find("C").text)
            flip = float(piso.find("F").text)
            switch = float(piso.find("S").text)

            xpath = "./piso" + "[@" + "nombre" + "=" + "'" + name + "'" + "]" + "/patrones"

            for patrones in raiz.findall(xpath):
                datos = patrones.findall("patron")
                for dato in datos:
                    new_patron = Patron(dato.get("codigo"), dato.text, 0)
                    lista_patrones.insertar(new_patron)

            new_piso = Piso(name, rows, columns, flip, switch, lista_patrones, 0)
            lista_pisos.insertar(new_piso)
        print("Datos cargados con éxito, regresando al menú principal")
        datos_cargados = True



    except Exception as e:
        print("Ha ocurrido un error, tenga más detalles: ", e)




