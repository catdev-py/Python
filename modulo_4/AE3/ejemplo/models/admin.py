from .usuario import Usuario
from .pelicula import Pelicula
from .funcion import Funcion
from datetime import datetime

class Admin(Usuario):
    def __init__(self, nombre, email, password):
        super().__init__(nombre, email, password)
        self.peliculas = []
        self.funciones = []
    
    def agregar_pelicula(self):
        titulo = input("Ingrese el título de la película: ")
        genero = input("Ingrese el género: ")
        duracion = input("Ingrese la duración en minutos: ")
        nueva_pelicula = Pelicula(titulo, genero, duracion)
        self.peliculas.append(nueva_pelicula)
        print(f"Se ha agregado la pelicula '{titulo}'.")
        return nueva_pelicula
    
    def agregar_funcion(self):        
        titulo = input("Ingrese el título de la película: ")
        pelicula = next((p for p in self.peliculas if p.titulo == titulo), None)
        
        if not pelicula:
            print("La pelicula '{titulo}' no existe.")
            return
        
        fecha_str = input("Ingrese la fecha (ej: 2025-08-01): ")
        hora_str = input("Ingrese la hora (ej: 19:30): ")
        sala = input("Ingrese el número de sala: ")
        asientos = input("Ingrese la cantidad de asientos disponibles: ")

            # Convertir cadenas a objetos datetime.date y datetime.time
        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
            hora = datetime.strptime(hora_str, "%H:%M").time()
        except ValueError:
            print("Formato de fecha u hora inválido.")
            return
        
        # Crear una nueva función
        nueva_funcion = Funcion(pelicula, fecha, hora, sala, asientos)

        # Agregar a la lista global
        self.funciones.append(nueva_funcion)

        print(f"Se ha agregado la función '{titulo}', el día {fecha_str}, a las {hora_str}, en la sala {sala}, con {asientos} asientos.")
        return nueva_funcion
        