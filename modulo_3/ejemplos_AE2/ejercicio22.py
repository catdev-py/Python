# === EJERCICIO 22: Crear y Manipular Objetos (Concepto básico de POO)
print("\n--- EJERCICIO 22 ---")
class Estudiante:
    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso

    def presentarse(self):
        print(f"Hola, soy {self.nombre} del curso {self.curso}")

alumno1 = Estudiante("Javiera", "2° Medio")
alumno1.presentarse()

# __init__	Método constructor, inicializa datos
# self	Representa al propio objeto
# self.nombre	Crea un atributo nombre
# self.curso	Crea un atributo curso