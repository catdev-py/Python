class Arriendo:
    def __init__(self, id_arriendo, cliente, horas, valor_hora, kayak):
        self.id_arriendo = id_arriendo
        self.cliente = cliente
        self.horas = horas
        self.valor_hora = valor_hora
        self.kayak = kayak
        self.validar_horas()

    def validar_horas(self):
        if self.horas <= 0:
            raise ValueError("Las horas deben ser mayores a cero")

    def calcular_valor(self):
        return self.horas * self.valor_hora

    def mostrar_resumen(self):
        return (f"Arriendo {self.id_arriendo}\n"
                f"Cliente: {self.cliente}\n"
                f"Kayak: {self.kayak.codigo} - {self.kayak.color} "
                f"(Capacidad: {self.kayak.capacidad} personas)\n"
                f"Horas: {self.horas}\n"
                f"Total a pagar: ${self.calcular_valor():,.0f}")