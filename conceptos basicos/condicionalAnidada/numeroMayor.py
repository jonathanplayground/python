#Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos.

num1 = int(input("Digitar el primer numero: "))
num2 = int(input("Digitar el segundo numero: "))
num3 = int(input("Digitar el tercer numero: "))

if num1 > num2:
    if num3 < num1:
        print("Numero mayor: ", num1)
    else:
        print("Numero mayor 1: ", num3)
else:
    if num3 > num1:
        if num3 > num2:
            print("Numero mayor 2: ", num3)
        else:
            print("Numero mayor 3: ", num2)        
    else:
        print("Numero mayor 4: ", num2)