import os;
import cursos;

selection = ""

def menu():
    print("1- Registrar empleado")
    print("2- Agregar nuevo curso")
    print("3- Mostrar resumen")
    print("4- Salir")

while selection != "salir":
    menu()
    option = input("Seleccione una opción")
    os.system ("cls")

    if option.isnumeric():
        if int(option) == 1:
            cursos.registrar_empleado()
            print()
        elif int(option) == 2:
            cursos.seleccionar_curso()
            print()
        elif int(option) == 3:
            cursos.mostrar_resumen()
            print()
        elif int(option) == 4:
            selection = "salir"
        else:
            print("Ingrese una opción válida")
    else:
        print("Seleccione una opción utilizando un número")


