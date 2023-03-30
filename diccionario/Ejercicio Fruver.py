Fruver = {}

while True:
    
    opcion = input("Seleccione una opcion: \n 1. Agregar/modificar \n 2. Buscar \n 3. Borrar \n 4. Listar \n 5. Salir \n ")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre de la fruta: ")
        precio = float(input("Ingrese el precio de la fruta: "))
        if nombre in Fruver:
            print("La fruta", nombre, " ya se encuentra registrada con un precio de",Fruver[nombre])
        else:
            Fruver[nombre] = precio
            print("La fruta ", nombre ," ha sido agregada con un precio de ", precio)
            
    elif opcion == "2":
        busqueda = input("Ingrese un texto de búsqueda: ")
        resultados = [nombre for nombre in Fruver if nombre.startswith(busqueda)]
        if resultados:
            print("Resultados de la búsqueda",busqueda )
            for nombre in resultados:
                print(nombre, Fruver[nombre])
        else:
            print("No se encontraron frutas que comiencen con", busqueda)
            
    elif opcion == "3":
        nombre = input("Ingrese el nombre de la fruta a borrar: ")
        if nombre in Fruver:
            confirmacion = input ("seguro que desea borrar ", nombre , "(si/no)" )
            if confirmacion.lower() == "si" or "Si" or "SI" :
                del Fruver[nombre]
                print("La fruta",nombre, "ha sido borrada")
            else:
                print("No se ha borrado la fruta",nombre)
        else:
            print("La fruta ", nombre ,"no se encuentra ")
            
    elif opcion == "4":
        if Fruver:
            print("Lista de frutas:")
            for nombre, precio in Fruver.items():
                print(nombre , precio)
        else:
            print("No hay frutas registradas")
            
    elif opcion == "5":
        print("Saliste del programa")
        break
        
    else:
        print("Opción no válida, seleccione nuevamente")