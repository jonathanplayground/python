#Realizar la carga del precio de un producto y la cantidad a llevar. 
#Mostrar cuanto se debe pagar (se ingresa un valor entero en el precio del producto)

producto = int(input("Ingresar el valor del producto: "))
cantidad = int(input("Digitar la cantidad de productos llevados: "))

pago = producto * cantidad

print("El total a pagar es: ")
print(pago)