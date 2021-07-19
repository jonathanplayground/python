#Confeccionar un programa que permita cargar un número entero positivo de 
# hasta tres cifras y muestre un mensaje indicando si tiene 1, 2, o 3 cifras. 
# Mostrar un mensaje de error si el número de cifras es mayor.

num = int(input("Digitar un numero no mayor de tres cifras: "))

if num < 999:
    if num >99:
        print("Numero de tres cifras")
    else:
        if num >9:
            print("Numero de dos cifras")
        else:
            print("Numero de una cifra")
else:
    print("El numero es mayor a tres cifras")