from Persona import Persona
class Empleado (Persona):
    
    def __init__(self):
        super().__init__('tipoDoc', 'documento', 'nombre', 'apellido', 'peso', 'estatura', 'edad','sexo')
        self.cargo = ""
        self.valorhora = 0
        self.horastrabajadas = 0
        self.departamento = ""
        
    def registrarPersona(self):
        super().registrarPersona()
        self.cargo=input("Ingrese su cargo ")
        self.valorHora=int(input("Ingrese el valor por hora trabajada "))
        self.horasTrabajadas=int(input("Ingrese las horas trabajadas "))
        self.departamento=input("Ingrese el departamento en que trabaja ")
        
        
    def calcularHonorarios(self):
        totalPagar= self.valorHora * self.horasTrabajadas
        reteica = totalPagar * 0.00966
        honorario = totalPagar - reteica
        return honorario
    
    def imprimirEmpleado(self):
        print(f"\nsus datos ingresados son\nTipo de documento {self.documento} \nNombre {self.nombre} \nApellido {self.apellido} \nCargo {self.cargo} \nHoras Trabajadas {self.horasTrabajadas} \nValor por hora {self.valorHora} \nTotal a pagar {self.calcularHonorarios()}")
        
Empleado1=Empleado()
Empleado1.registrarPersona()
Empleado1.imprimirEmpleado()
Empleado1.calcularHonorarios()