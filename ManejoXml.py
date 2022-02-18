import xml.etree.ElementTree as ET
from ListaPiso import ListaPiso
from ListaPatron import ListaPatron
from Piso import Piso
from Patron import Patron
import re

lista_pisos = None
lista_patrones = None
datos_cargados = False


def Leer(ruta):
    global lista_patrones, lista_pisos, lista_celdas, datos_cargados
    lista_pisos = ListaPiso()
    try:
        arbol = ET.parse(ruta)
        raiz = arbol.getroot()

        for piso in raiz.findall("piso"):
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
                    texto = dato.text
                    texto = re.sub(r"[\n\t\s]*", "", texto)
                    if len(texto) == rows * columns:
                        new_patron = Patron(dato.get("codigo"), dato.text, 0)
                        lista_patrones.insertar(new_patron)

            new_piso = Piso(name, rows, columns, flip, switch, lista_patrones, 0)
            lista_pisos.insertar(new_piso)
        print("Datos cargados con éxito, regresando al menú principal")
        datos_cargados = True



    except Exception as e:
        print("Ha ocurrido un error, tenga más detalles: ", e)
