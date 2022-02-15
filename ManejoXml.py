import xml.etree.ElementTree as ET


def Leer(ruta):
    arbol = ET.parse(ruta)
    raiz = arbol.getroot()

    for piso in raiz.findall("piso"):
        print("El nombre del piso: ", piso.get("nombre"))
        print("La cantidad de filas son: ", piso.find("R").text)
        print("La cantidad de columnas son: ", piso.find("C").text)
        print("La cantidad a pagar por flip es: ", piso.find("F").text)
        print("La cantidad a pagar por switch es: ", piso.find("S").text)

        for patrones in raiz.findall("piso/patrones"):
            print("El código del patrón es: ",  patrones.find("patron").get("codigo"))
            print("El string que describe las casillas es: ", patrones.find("patron").text)

