notas = []
materia = int(input("Por favor ingrese la cantidad de notas a evaluar: "))

for i in range(materia):
    nota = int(input("Ingrese la nota "))
    while nota < 1 or nota > 5:
        nota = int(input("Ingrese una nota válida entre 1 y 5 para mostar el promedio"))
    notas.append(nota)

promedio = sum(notas) / materia

if promedio < 3:
    print("Reprobobaste tu nota final es de",promedio)
    
elif promedio >= 3 and promedio < 4:
    print("Pasaste raspando tu nota final es de",promedio)

else:
    print("Aprobobaste con buenos resultados tu nota final es de",promedio)
