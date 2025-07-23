class Operacion:
    def calcular(self, a, b):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

class Suma(Operacion):
    def calcular(self, a, b):
        return a + b

class Resta(Operacion):
    def calcular(self, a, b):
        return a - b

class Multiplicacion(Operacion):
    def calcular(self, a, b):
        return a * b

class Division(Operacion):
    def calcular(self, a, b):
        if b == 0:
            return "Error: división por cero"
        return a / b

# Función que aplica polimorfismo
def operar(operacion, a, b):
    return operacion.calcular(a, b)

# Uso
op1 = Suma()
op2 = Resta()
op3 = Multiplicacion()
op4 = Division()

print("Suma:", operar(op1, 10, 5))
print("Resta:", operar(op2, 10, 5))
print("Multiplicación:", operar(op3, 10, 5))
print("División:", operar(op4, 10, 5))
