instructores = {}

while True:
    
    opcion = input("Que deseas realizar \n 1 Agregar/modificar instructor \n 2 Buscar instructor \n 3 Borrar instructor \n 4 Listar instructores \n 5 Salir")

    if opcion == "1":
        nombre = input("Ingrese el nombre del instructor: ")
        if nombre in instructores:
            print("El instructor", nombre, "ya está registrado")
            print("Materia ", {instructores[nombre][materia]})
            telefono = input("Ingrese el nuevo numero de telefono o  presione enter para dejarlo igual")
            if telefono != "":
                instructores[nombre][telefono] = telefono
        else:
            materia = input("Ingrese la materia que dicta: ")
            telefono = input("Ingrese el número de teléfono: ")
            instructores[nombre] = {materia: materia, telefono: telefono}
            print("El instructor",nombre, "ha sido registrado")

    elif opcion == "2":
        busqueda = input("Ingrese el nombre del instructor que desea buscar ")
        resultados = []
        for nombre, datos in instructores.items():
            if nombre.startswith(busqueda):
                resultados.append(nombre)
        print("Resultados de la consulta ")
        for nombre in resultados:
            print("Nombre", nombre, "Materia" ,instructores[nombre][materia], "Telefono",instructores[nombre][telefono])

    elif opcion == "3":
        nombre = input("Ingrese el nombre del instructor que desea eliminar ")
        if nombre in instructores:
            confirmacion = input("Está seguro que desea borrar al instructor",nombre, "(si/no)")
            if confirmacion.lower() == "si" or "Si" or "SI":
                del instructores[nombre]
                print("El instructor" ,nombre, "ha sido borrado")
        else:
            print("No se encontró al instructor", nombre, "en la agenda")

    elif opcion == "4":
        print("Instructores registrados ")
        for nombre, datos in instructores.items():
            print("Nombre", nombre, "Materia" ,instructores[nombre][materia], "Telefono",instructores[nombre][telefono])

    elif opcion == "5":
        print("Gracias por utilizarnos")
        break

    else:
        print("Opcion incorrecta")