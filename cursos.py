
employees = []

empleado1 = {'legajo': '15877', 'cursos': [], 'meses_antiguedad': 16, "nombre": "Juan Perez"}
empleado2 = {'legajo': '88894', 'cursos': [], 'meses_antiguedad': 12, "nombre": "Martina Sanchez"}
nuevo_empleado = {}

employees.append(empleado1)
employees.append(empleado2)

def registrar_empleado():
    nuevo_legajo = str(input("Ingrese un nuevo numero de legajo para el empleado"))
    nuevo_nombre = str(input("Ingrese el nombre del empleado"))
    nueva_antiguedad= int(input("Ingrese la cantidad de meses de antiguedad del empleado"))
    nuevo_empleado = {
        'legajo': nuevo_legajo,
        'nombre': nuevo_nombre,
        'meses_antiguedad': nueva_antiguedad,
        'cant_cursos': 0,
        'cursos': [] 
    }

    employees.append(nuevo_empleado)

    print("Datos del empleado nuevo:")
    print("Legajo:", nuevo_empleado['legajo'])
    print("Nombre:", nuevo_empleado['nombre'])
    print("Meses de antiguedad:", nuevo_empleado['meses_antiguedad'])
    print("Cursos realizados:", nuevo_empleado['cursos'])
            
    return nuevo_empleado

def seleccionar_curso():
    legajo = input("Escriba el legajo del empleado: ")
    encontrado = False
    for empleado in employees:
        if empleado["legajo"] == legajo:
            encontrado = True
            while True:
                print("Elija el curso a agregar:")
                print("1. PHP")
                print("2. Python")
                print("3. C#")
                print("4. HTML y CSS")
                print("5. Java")
                print("6. JS")
                print("7. Ruby")
                print("8. Git")
                print("9. Salir")

                opcion = input("Escriba el número del curso o 'Salir' para salir: ")

                if opcion == '9' or opcion.lower() == 'salir':
                    break
                elif opcion.isdigit() and 1 <= int(opcion) <= 8:
                    curso = agregar_curso(int(opcion))
                    empleado["cursos"].append(curso)
                else:
                    print("Opción inválida.")
        if not encontrado:
            print("El legajo es inexistente")

def agregar_curso(curso_id):
    cursos = ["PHP", "Python", "C#", "HTML y CSS", "Java", "JS", "Ruby", "Git"]
    print(f"Agregando curso: {cursos[curso_id - 1]}")
    return cursos[curso_id - 1]

def mostrar_resumen():
    sorted_employees = sorted(employees, key=lambda x: len(x['cant_cursos']), reverse=True)
    
    print("\nResumen de Empleados (Ordenados por cantidad de cursos realizados):\n")
    print(f"Total de empleados: {len(sorted_employees)}\n")
    
    for empleado in sorted_employees:
        print("Nombre:", empleado["nombre"])
        print("Legajo:", empleado["legajo"])
        print("Antigüedad (meses):", empleado["meses_antiguedad"])
        print("Cursos realizados:")
        for curso in empleado["cant_cursos"]:
            print("-", curso)
        print("\n")