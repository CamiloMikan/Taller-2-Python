baul = [] 

while True:
    opcion = int(input("Qué deseas realizar:\n 1. Agregar un articulo al baul \n 2. Ver los articulos en el baul \n 3. Borrar el ultimo articulo \n4. Borrar un articulo del baul \n5. Salir \n "))

    if opcion == 1:
        articulo = input("Ingrese el nombre del articulo: ")
        baul.append(articulo)
        print("El articulo", articulo, "ha sido agregado al baul")

    elif opcion == 2:
        if len(baul) == 0:
            print("El baul esta vacio.")
        else:
            for i in range(len(baul)):
                print("articulo en el baul",i+1, baul[i],)

    elif opcion == 3:
        if len(baul) == 0:
            print("El baul no contiene nada. \n")
        else:
            ultimoArticulo = baul.pop()
            print("El articulo", ultimoArticulo, "ha sido eliminado del baul ")

    elif opcion == 4:
        if len(baul) == 0:
            print("El baul no contiene nada ")
        else:
            print("Articulos en el baul ")
            for i in range(len(baul)):
                print(i+1, ".", baul[i])
            borrar = int(input("Ingrese el numero del articulo que desea borrar "))
            if borrar > 0 and borrar <= len(baul):
                articuloEliminado = baul.pop(borrar-1)
                print("El articulo", articuloEliminado, "ha sido eliminado del baul ")
            else:
                print("El numero de articulo ingresado es invalido. ")

    elif opcion == 5:
        print("Saliste del baul")
        break

    else:
        print("La opción ingresada no es valida. Por favor, intente nuevamente.")