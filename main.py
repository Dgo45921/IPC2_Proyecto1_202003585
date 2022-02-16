from tkinter import filedialog
import ManejoXml
from ManejoXml import Leer





def MostrarMenuPrincipal():
    print("Escribe el número de la opción a la que quieras acceder y presiona ENTER")
    while True:
        print(
            "---------Bienvenido---------\n1.Cargar XML\n2.Información de los pisos\n3.Salir\n----------------------------")
        try:
            option = int(input())
            if option == 1:
                print("Cargar xml")
                Ruta = filedialog.askopenfilename(title="Selecciona un archivo", initialdir="/",
                                                  filetypes=(("xml files", "*.xml"), ("", "")))
                Leer(Ruta)
            elif option == 2:
                MostrarMenu2()
            elif option == 3:
                break
        except Exception as e:
            print(e)


def MostrarMenu2():
    try:
        if ManejoXml.datos_cargados:
            print("Estos son los pisos cargados, si desea más información ingrese el número al lado de ellos. Si desea regresar ingrese la letra r")
            ManejoXml.lista_pisos.Mostrar()
            numpiso = input()
            if numpiso == "r":
                MostrarMenuPrincipal()
            else:
                num = int(numpiso)
                piso_buscado = ManejoXml.lista_pisos.buscar(num)
                if piso_buscado is not None:
                    print("-----------Nombre del piso---------------------Filas---------------------Columnas-------------------precio por voltear azulejo--------------precio por intercambiar azulejos-----")
                    print(str(piso_buscado.piso.num) + ". " + piso_buscado.piso.nombre + "                                          " + str(piso_buscado.piso.rows) + "                           " + str(piso_buscado.piso.columns) + "                              " + str(piso_buscado.piso.costo_flip) + "                                      " + str(piso_buscado.piso.costo_switch))
                    print("\n")
                    print("Ingrese el número al lado de cada opción para usar las funciones para este piso. Si desea regresar ingrese la letra 'r' ")
                    print("1. Ver patrones disponibles para este piso\n 2. Costeo para pasar de un patrón a otro para este piso en específico")
                    opc = input()
                    MostrarMenu3(opc, piso_buscado)
                else:
                    print("Piso no existente. Seleccione únicamente los pisos mostrados")
                    MostrarMenu2()

        else:
            print("Cargue primero el xml")
    except:
        print("ha ocurrido un error, ingrese únicamente números o la letra r")
        MostrarMenu2()



def MostrarMenu3(opc, piso_encontrado):
    try:
        if opc == "r":
            MostrarMenu2()
        else:
            opc = int(opc)
            if opc == 1:
                datospatrones = piso_encontrado.piso.patrones.Mostrar()
                print(datospatrones)
                print("si desea visualizar el patron ingrese el número que está al lado de este. Si desea regresar ingrese la letra 'r' ")
                opcion = input()
                if opcion == "r":
                    MostrarMenu2()
                else:
                    opcion = int(opcion)

            elif opc == 2:
                print("costeo")
    except:
        print("Ingrese únicamente los números mostrados anteriormente o la letra 'r'")







MostrarMenuPrincipal()
