#Realizar un programa que lea cuatro valores numéricos e informar su suma y promedio

num1 = int(input("Digitar el primer numero: "))
num2 = int(input("Digitar el segundo numero: "))
num3 = int(input("Digitar el tercero numero: "))
num4 = int(input("Digitar el cuarto numero: "))

suma = num1 + num2 + num3 + num4
promedio = suma / 4

print("La suma de los valores es: ")
print(suma)

print("El promedio de los valores es: ")
print(promedio)