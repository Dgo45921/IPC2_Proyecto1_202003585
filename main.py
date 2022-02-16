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
    if ManejoXml.datos_cargados:
        print("Estos son los pisos cargados, si desea más información ingrese el número al lado de ellos")
        ManejoXml.lista_pisos.Mostrar()
        numpiso = input()
    else:
        print("Cargue primero el xml")


MostrarMenuPrincipal()
