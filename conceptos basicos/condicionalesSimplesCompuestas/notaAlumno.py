#Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete 
# mostrar un mensaje "Promocionado".


nota1 = int(input("Digitar la primer nota: "))
nota2 = int(input("Digitar la segunda nota: "))
nota3 = int(input("Digitar la tercer nota: "))

suma = nota1 + nota2 + nota3
promedio = suma / 3
print("El promedio es: ", promedio)
if promedio >= 7:
    print("Promocionado")
else:
    print("Promedio inferior a 7")