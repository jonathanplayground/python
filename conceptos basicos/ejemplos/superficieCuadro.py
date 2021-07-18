#Hallar la superficie de un cuadrado conociendo el valor de un lado

lado =input("Ingrese el valor de un aldo del cuadrado: ")
lado2 = int(lado)       #se guarda enuna nueva variable, que puede tener el mismo nombre el onjeto almacenado (lado)
                        #La funcion int representa que el valor guardado es un valore entero
                        # tambien se puede escribir como lado=int(input("Ingrese la medida del lado del cuadrado:"))
superficie = lado2*lado2
print("la superficie del cuadrado es: ")
print(superficie)
