peso=float(input("Ingrese su peso (Kg): "))
altura = float(input("Ingrese su altura (m): "))

imc = (peso)/(altura**2)

if imc <18.5:
    print("Su IMC es de: ", imc)
    print("Detalle: Bajo peso")
elif imc >=18.5 and imc <24.9:
    print("Su IMC es de: ", imc)
    print("Detalle: Normal")
elif imc >=25 and imc <29.9:
    print("Su IMC es de: ", imc)
    print("Detalle: Sobrepeso")
elif imc >=30 and imc <34.7:
    print("Su IMC es de: ", imc)
    print("Detalle: Obesidad I")
elif imc >=35 and imc <39.9:
    print("Su IMC es de: ", imc)
    print("Detalle: Obesidad II")
elif imc >=40 and imc <49.9:
    print("Su IMC es de: ", imc)
    print("Detalle: Obesidad III")
elif imc >=50:
    print("Su IMC es de: ", imc)
    print("Detalle: Obesidad IV")    
