from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import date, time

# Para evitar importación circular
if TYPE_CHECKING:
    from .funcion import Funcion
    from .boleto import Boleto
    from .pelicula import Pelicula

class Usuario:
    def __init__(self, nombre: str, email: str, password: str):
        self.nombre = nombre
        self.email = email
        self._password = password # Usamos _ para indicar que es "protegido"
        self.boletos: list[Boleto] = []
      
    def registrarse(self, password: str) -> None:
        self._password = password
        print(f"{self.nombre} se ha registrado.")

    def comprar_boleto(self, funcion: Funcion, cantidad: int = 1) -> list[Boleto] | None:
        """
        Intenta comprar uno o más boletos para una función.
        Devuelve una lista de boletos si la compra es exitosa, sino None.
        """
        from .boleto import Boleto # Importación local para evitar importación circular

        print(f"\n{self.nombre} intenta comprar {cantidad} boleto(s) para: {funcion}")
        
        if funcion.reservar_asiento(cantidad):
            nuevos_boletos = []
            for i in range(cantidad):
                asiento = f"{chr(65 + len(funcion.boletos_vendidos) // 8)}-{len(funcion.boletos_vendidos) % 8 + 1}"
                nuevo_boleto = Boleto(usuario=self, funcion=funcion, asiento=asiento)
                self.boletos.append(nuevo_boleto)
                funcion.boletos_vendidos.append(nuevo_boleto)
                nuevos_boletos.append(nuevo_boleto)
            
            print(f"¡Compra realizada! {self.nombre} ha adquirido {len(nuevos_boletos)} boleto(s).")
            return nuevos_boletos
        else:
            print(f"Compra fallida para {self.nombre}.")
            return None

    def __str__(self) -> str:
        return f"Usuario: {self.nombre} ({self.email})"
    
class Administrador(Usuario):
    """La clase Administrador hereda de Usuario y tiene permisos adicionales."""
    
    def __init__(self, nombre: str, email: str, password: str):
        # Llama al constructor de la clase padre (Usuario)
        super().__init__(nombre, email, password)

    def agregar_pelicula(self, titulo: str, genero: str, duracion: int, sinopsis: str) -> Pelicula:
        """Crea y devuelve un nuevo objeto Pelicula."""
        from .pelicula import Pelicula # Importación local
        print(f"Admin '{self.nombre}' está agregando la película: {titulo}")
        nueva_pelicula = Pelicula(titulo, genero, duracion, sinopsis)
        return nueva_pelicula

    def agregar_funcion(self, pelicula: Pelicula, fecha: date, hora: time, sala: int, asientos: int) -> Funcion:
        """Crea y devuelve un nuevo objeto Funcion para una película."""
        from .funcion import Funcion # Importación local
        print(f"Admin '{self.nombre}' está agregando una función para '{pelicula.titulo}'")
        nueva_funcion = Funcion(pelicula, fecha, hora, sala, asientos)
        return nueva_funcion
        
    def __str__(self) -> str:
        return f"Administrador: {self.nombre} ({self.email})"