#Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente información: 
# cantidad total de preguntas que se le realizaron y la cantidad de preguntas que contestó correctamente. 
# Se pide confeccionar un programa que ingrese los dos datos por teclado e informe el nivel del mismo 
# según el porcentaje de respuestas correctas que ha obtenido, y sabiendo que

#Nivel máximo:	Porcentaje>=90%.
#Nivel medio:	Porcentaje>=75% y <90%.
#Nivel regular:	Porcentaje>=50% y <75%.
#Fuera de nivel:	Porcentaje<50%.

preguntas = int(input("Digite el numero de preguntas realizadas: "))
correctas = float(input("Digite el numero de respuestas correctas: "))

nivel = (100*correctas)/preguntas
print("El porcentaje es de: ", nivel, "%")

if nivel <= 50:
    if nivel < 0:
        print("Verificar datos, porcentaje menor a cero.")
    else: 
        print("Fuera de nivel")
else:
    if nivel <75:
        print("Nivel regular")
    else:
        if nivel <90:
            print("NIvel medio")
        else:
            if nivel >100:
                print("Verificar datos, porcentaje mayor a 100 %")
            else:
                print("Nivel maximo")


    