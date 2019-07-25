edad=int(input("Ingrese su edad: "))
genero=input("Seleccione su sexo"+"\n"+"H para Hombre"+"\n"+"M para Mujer"+"\n"+"O para Otros:"+"\n")

if edad>=18:
    if genero in 'Hh' :
        print("Señor, usted es mayor de edad")
    elif genero in 'Mm':
        print("Señora, usted es mayor de edad")
    elif genero in 'Oo':
        print("Usted es mayor de edad")
    else:
        print("Ingrese una de las opciones que esta en el menu")
else:
       if genero in 'Hh':
            print("Joven, usted es menor de edad")
       elif genero in 'Mm':
            print("Señorita usted es menor de edad")
       elif genero in 'Oo':
            print("Usted es menor de edad")
       else:
            print("Ingrese una de las opciones que esta en el menu")
