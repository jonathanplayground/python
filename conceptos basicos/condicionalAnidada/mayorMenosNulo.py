#Se ingresa por teclado un valor entero, mostrar una leyenda que 
# indique si el número es positivo, negativo o nulo (es decir cero)

num = int(input("Digitar un numero: "))

if num != 0:
    if num > 0:
        print("Numero positivo")
    else:
        print("Numero negativo")
else:
    print("Numero nulo")