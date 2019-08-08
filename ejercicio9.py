class Empleado:
    def __init__ (self):
        self.Codigo=""
        self.Nombres=""
        self.Apellidos=""
        self.Salario_base=""

    def Calcular_retencion(self):
     
        total=(self.Salario_base*0.1)
        return total

     
            
    def Mostarar_NombreCompleto(self):
        Completo=self.Nombres+" "+self.Apellidos
        return Completo


    def Calcular_salario_neto(self):
 
        if(((self.Salario_base)-(self.Salario_base*0.1))<=828116):
            return ((self.Salario_base)-(self.Salario_base*0.1))+97032
        else:
            return ((self.Salario_base)-(self.Salario_base*0.1))
    

emp=Empleado()
Codigo=input("Ingrese Su codig: ")
nombre=input("Ingrese Nombres: ")
Apellidos=input("Ingrese Apellidos: ")
Salario_base=float(input("Ingrese su Salario: "))

emp.Codigo=Codigo
emp.Nombres=nombre
emp.Apellidos=Apellidos
emp.Salario_base=Salario_base


print(emp.Calcular_retencion())
print(emp.Calcular_salario_neto())
print(emp.Mostarar_NombreCompleto())
    

    