class Kayak:
    def __init__(self, codigo, capacidad, color):
        self.codigo = codigo
        self.capacidad = capacidad
        self.color = color
        self.validar_capacidad()

    def validar_capacidad(self):
        if self.capacidad < 1:
            raise ValueError("La capacidad debe ser al menos 1 persona")