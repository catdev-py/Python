class CPU:
    def especificaciones(self):
        return "Procesador Intel i7 🇨🇱"

class Computadora:
    def __init__(self):
        self.cpu = CPU()

    def mostrar_info(self):
        return f"Computadora con {self.cpu.especificaciones()}"

pc = Computadora()
print(pc.mostrar_info())
