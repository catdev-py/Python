class Pelicula:
    def __init__(self, titulo, genero, duracion):
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion
        
    def __str__(self):
        return self.titulo
    
    def obtener_info(self):
        return f"--- Película: {self.titulo} ---\nGénero: {self.genero}\nDuración: {self.duracion} minutos"