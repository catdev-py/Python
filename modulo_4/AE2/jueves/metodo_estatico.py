class Util:
    @staticmethod
    def es_par(numero):
        return numero % 2 == 0

numero = int(input("Ingrese un número: "))
print(Util.es_par(numero))
