from tkinter import filedialog
from ManejoXml import Leer
def MostrarMenu():
    print("Escribe el número de la opción a la que quieras acceder y presiona ENTER")

    while True:
        print(
            "---------Bienvenido---------\n1.Cargar XML\n2.Información de los pisos\n3.Salir\n----------------------------")
        try:
            option = int(input())
            if option == 1:
                print("Cargar xml")
                Ruta = filedialog.askopenfilename(title="Selecciona un archivo", initialdir="/",filetypes=(("xml files", "*.xml"), ("", "")))
                Leer(Ruta)

            elif option == 2:
                print("informacion pisos")
            elif option == 3:

                break
        except Exception as e:
            print(e)


MostrarMenu()
