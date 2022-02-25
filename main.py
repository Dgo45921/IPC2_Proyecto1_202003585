import FuncionCelda
import ManejoXml
from ManejoXml import Leer
from Costeo import InicioCosteo



def MostrarMenuPrincipal():
    print("Escribe el número de la opción a la que quieras acceder y presiona ENTER")
    while True:
        print(
            "---------Bienvenido---------\n1.Cargar XML\n2.Información de los pisos\n3.Salir\n----------------------------")
        try:
            option = int(input())
            if option == 1:
                print("Ingrese la ruta absoluta de su archivo .xml")
                Ruta = input()
                Leer(Ruta)
            elif option == 2:
                MostrarMenu2()
            elif option == 3:
                break
        except:
            print("Asegurese que su archivo sea válido")


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
                    if opc == "r":
                        MostrarMenu2()
                    else:
                        opc = int(opc)
                        if opc == 1:
                            MostrarMenu3(piso_buscado)
                        elif opc == 2:
                            Costeo_pisos(piso_buscado)

                        else:
                            print("seleccione una opción válida")
                            MostrarMenu2()

                else:
                    print("Piso no existente. Seleccione únicamente los pisos mostrados")
                    MostrarMenu2()

        else:
            print("Cargue primero el xml")
    except:
        print("ha ocurrido un error, ingrese únicamente números o la letra r")
        MostrarMenu2()



def MostrarMenu3(piso_encontrado):
    try:
        datospatrones = piso_encontrado.piso.patrones.Mostrar()
        print(datospatrones)
        print(
            "si desea visualizar el patron ingrese el número que está al lado de este. Si desea regresar ingrese la letra 'r' ")
        opcion = input()
        if opcion == "r":
            MostrarMenu2()
        else:
            opcion = int(opcion)
            patron_encontrado = piso_encontrado.piso.patrones.Buscar(opcion)
            if patron_encontrado is not None:
                FuncionCelda.MostrarCeldas(patron_encontrado, piso_encontrado)
                MostrarMenu3(piso_encontrado)
            else:
                print("patron no encontrado, ingrese solamente los que están disponibles")
                MostrarMenu3(piso_encontrado)



    except Exception as e:
        print("Ingrese únicamente los números mostrados anteriormente o la letra 'r'", e)



def Costeo_pisos(piso_encontrado):
    try:
        print("ingrese el número al lado del patrón del que quiere partir, de lo contrario ingrese la letra r para regresar")
        datospatrones = piso_encontrado.piso.patrones.Mostrar()
        print(datospatrones)
        opcion = input()
        if opcion == "r":
            MostrarMenu2()
        else:
            opcion = int(opcion)
            patron_encontrado1 = piso_encontrado.piso.patrones.Buscar(opcion)
            if patron_encontrado1 is not None:
                print("Patron válido, ingrese el número del patron destino")
                opcion2 = int(input())
                patron_encontrado2 = piso_encontrado.piso.patrones.Buscar(opcion2)
                if patron_encontrado1 == patron_encontrado2:
                    print("ingrese patrones distintos")
                    Costeo_pisos(piso_encontrado)
                elif patron_encontrado2 is None:
                    print("ingrese un patron válido")
                    Costeo_pisos(piso_encontrado)
                else:
                    InicioCosteo(piso_encontrado, patron_encontrado1, patron_encontrado2)


            else:
                print("ingrese un patron valido")
                Costeo_pisos(piso_encontrado)






    except Exception as e:
        print("Ingrese únicamente los números mostrados anteriormente o la letra 'r'", e)





MostrarMenuPrincipal()
