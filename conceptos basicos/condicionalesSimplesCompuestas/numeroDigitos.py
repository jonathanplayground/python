#Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) 
# mostrar un mensaje indicando si el número tiene uno o dos dígitos.
#(Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)

num = int(input("Digitar el numero: "))

if num <100:
    if num >= 10:
        print("El valor tiene mas de dos digitos")
    else: 
        print("El valor tiene un digito")
else:
    print("numero mayor a 99")