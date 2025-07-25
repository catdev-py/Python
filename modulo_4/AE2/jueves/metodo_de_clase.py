class Producto: # Se define la clase producto
    def __init__(self, nombre, precio): # constructor que recibe parametros nombre y precio
        self.nombre = nombre # atributos
        self.precio = precio

    @classmethod # @classmethod, lo que significa que se refiere a la clase (cls) y no a un objeto
    def desde_string(cls, cadena): # Se define un método de clase llamado desde_string
        nombre, precio = cadena.split("-") # Aquí se separa la cadena usando - como separador.
        return cls(nombre, float(precio)) # Se retorna una nueva instancia de Producto utilizando cls, que representa la clase.
    
                                          # nombre queda como cadena ("Pera"). precio se convierte a número decimal usando float("2.99").
p1 = Producto("Manzana", 1.99) # Se crea un objeto Producto de forma normal usando el constructor.

p2 = Producto.desde_string("Pera-2.99") #  Se crea otro objeto Producto pero usando el método de clase.

print(p1.nombre, p1.precio) # Imprime los atributos del producto p1
print(p2.nombre, p2.precio) # Imprime los atributos del producto p2