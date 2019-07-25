
num1=int(input("Digite un numero: "))
num2=int(input("Digite un numero: "))

opcion=int(input("Operaciones Aritmetica"+"\n"+"[1] Suma"+"\n"+ "[2] Resta"+"\n"+ "[3] Multipicar"+"\n"+ "[4] Dividir"+"\n"+ "Seleccione una opcion:"))



if opcion==1:
    print("La suma: ", (num1+num2))
elif opcion==2:
    print("La resta: ", (num1-num2))
elif opcion==3:
    print("La Multiplicar: ", (num1*num2))
elif opcion==4:
    print("La Dividir: ", (num1/num2))
else:
    print("No se puede encontrar esa opcion")
