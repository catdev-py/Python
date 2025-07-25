class Perro: # Define la clase Perro
    
    # Atributo de Clase, pertenece a la clase (no a un perro en particular).
    # Contará cuántos perros se han creado con esta clase.
    perritos = 0
    
    def __init__(self, nombre, edad, raza): # Constructor
        self.nombre = nombre # Atributos de instancia
        self.edad = edad
        self.raza = raza
        Perro.perritos += 1 # Incrementamos la cantidad de perritos
        
    def cumpleanios(self): # método que simula que el perro cumple un año.
        self.edad += 1
        
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Raza: {self.raza}")
       
    @classmethod # Definimos un método de clase
    def cantidad_perritos(cls): # Parámetro cls hace referencia a la clase
        print(f"Hay {cls.perritos} en el programa!") # Muestra cuántos perros se han creado en total
                                                    # Usa cls.perritos para acceder al atributo de clase.
    @staticmethod # Definimos un método estático, no necesita self ni cls.
    def muchos_perritos(cantidad):   # No usa ni la clase ni la instancia.
        if cantidad > 30:            # Solo recibe un número y devuelve True si es mayor a 30.
            return True              # Sirve como herramienta auxiliar.
        else:
            return False
        
fido = Perro("Fido", 3, "Pastor aleman") # Objetos
bono = Perro("Bono", 5, "Pastor Belga")    
arthur = Perro("Arthur", 2, "Doberman") 
mia = Perro("Mia", 1, "Salchicha")

# Llamamos al método de clase para mostrar cuántos perros hay en total.
Perro.cantidad_perritos() # Imprime la cantidad de perritos

# Estamos probando el método estático muchos_perritos desde diferentes formas:
# Desde la clase directamente
print(Perro.muchos_perritos(50)) # Imprime True porque hay 50 perritos
# Desde cada objeto (aunque no es lo ideal, ¡funciona!)
print(fido.muchos_perritos(50))
print(bono.muchos_perritos(50))
print(arthur.muchos_perritos(50))
print(mia.muchos_perritos(29)) # Imprime False porque hay 29 perritos

fido.mostrar_info()
bono.mostrar_info()
arthur.mostrar_info()
mia.mostrar_info()

# Resumen Final    
""" perritos → cuenta total de perros creados (atributo de clase)

self → se refiere a un objeto individual (cada perro)

cls → se refiere a la clase Perro

@classmethod → método que trabaja con la clase

@staticmethod → método que no necesita ni clase ni objeto

__init__ → constructor que inicializa cada nuevo perro """