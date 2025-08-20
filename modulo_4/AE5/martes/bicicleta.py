# clase bicicleta 

class Bicicleta:
    def __init__(self, id, marca, modelo, precio, disponible):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.disponible = disponible

    def __str__(self):
        return f"ID: {self.id}, Marca: {self.marca}, Modelo: {self.modelo}, Precio: {self.precio}, Disponible: {self.disponible}"
    
    def registrar_bicicleta(self):
        return f"ID: {self.id}, Marca: {self.marca}, Modelo: {self.modelo}, Precio: {self.precio}, Disponible: {self.disponible}"

    def cambiar_disponibilidad(self):
        self.disponible = not self.disponible
        
    def mostrar_info(self):
        print(f"ID: {self.id}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Precio: {self.precio}")
        print(f"Disponible: {self.disponible}")