#Confeccionar un programa que pida por teclado tres notas de un alumno, 
#calcule el promedio e imprima alguno de estos mensajes:
#Si el promedio es >=7 mostrar "Promocionado".
#Si el promedio es >=4 y <7 mostrar "Regular".
#Si el promedio es <4 mostrar "Reprobado"

nota1 = int(input("Digitar la primer nota: "))
nota2 = int(input("Digitar la segunda nota: "))
nota3 = int(input("Digitar la tercera nota: "))

suma = nota1 + nota2 + nota3
promedio = suma / 3

print("El promedio es: ", promedio)
if promedio >= 7:
    print("Promocionado")
else:
    if promedio >= 4:
        print("Regular")
    else:
        print("Reprobado")