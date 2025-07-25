from persona import Persona
from telefono import Telefono

if __name__ == "__main__":
    p1 = Persona("Ana", 30) # Llama al constructor __init__ de Persona, pasando "Ana" y 30.
                            # Python crea un nuevo objeto en memoria y lo inicializa con esos valores.
                            # La variable p1 referencia ese objeto.
    p1.saludar()            # Invoca el método saludar sobre el objeto p1
                            # Dentro de saludar, Python sustituye self.nombre por "Ana" y self.edad por 30.
                            # Se imprime en pantalla: ¡Hola! Soy Ana y tengo 30 años.
                            
    p2 = Persona("Carlos", 25)
    p2.saludar()
    
    t1 = Telefono("Huawei", "Y7", "Negro", "12345678")
        
    t2 = Telefono("Xiaomi", "Mi 9", "Negro", "87654321")
    t2.llamar(t1.numero)