class Calculadora:
    def __init__(self, valor=0):
        self.valor = valor

    def sumar(self, numero):
        self.valor += numero
        return self

    def multiplicar(self, numero):
        self.valor *= numero
        return self

    def mostrar(self):
        print(f"Resultado: {self.valor}")
        return self

calc = Calculadora()
calc.sumar(10).multiplicar(7).mostrar()