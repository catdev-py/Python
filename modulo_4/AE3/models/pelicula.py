import uuid

class Pelicula:
    def __init__(self, titulo: str, genero: str, duracion: int, sinopsis: str):
        self.id_pelicula = str(uuid.uuid4())
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion  
        self.sinopsis = sinopsis

    def obtener_info(self) -> str:
        """Devuelve una cadena con la información completa de la película."""
        return (
            f"--- Película: {self.titulo} ---\n"
            f"Género: {self.genero}\n"
            f"Duración: {self.duracion} minutos\n"
            f"Sinopsis: {self.sinopsis}"
        )

    def __str__(self) -> str:
        """Representación simple de la película."""
        return self.titulo