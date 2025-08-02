class Persona:
    def bailar(self):
        raise NotImplementedError("Este método debe ser implementado.")

class Cuequero(Persona):
    def bailar(self):
        print("Baila la cueca con pañuelo en mano.")

class Huaso(Persona):
    def bailar(self):
        print("Zapatea fuerte y gira con su pareja.")

class Ciudadano(Persona):
    def bailar(self):
        print("Se mueve al ritmo de la música popular.")

# Lista de personajes
personas = [Cuequero(), Huaso(), Ciudadano()]

for persona in personas:
    persona.bailar()

""" Polimorfismo en acción: todas las clases responden a bailar(), 
pero con respuestas únicas.

Desafío: “¿Y cómo bailaría un extranjero en Fiestas Patrias?” """