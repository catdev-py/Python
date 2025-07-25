class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.paginas_leidas = 0

    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Páginas: {self.paginas}")
        print(f"Páginas leídas: {self.paginas_leidas}")

    def leer(self, paginas):
        if self.paginas_leidas + paginas <= self.paginas:
            self.paginas_leidas += paginas
        else:
            self.paginas_leidas = self.paginas
        print(f"Has leído {paginas} páginas.")
        return self  # Permite el encadenamiento

    def progreso(self):
        porcentaje = (self.paginas_leidas / self.paginas) * 100
        print(f"Llevas leído el {porcentaje:.2f}% del libro.")
        return self  # Permite el encadenamiento

    @classmethod
    def cargar_desde_string(cls, cadena):
        # Ejemplo de cadena: "1984|George Orwell|328"
        partes = cadena.split("|")
        titulo = partes[0]
        autor = partes[1]
        paginas = int(partes[2])
        return cls(titulo, autor, paginas)

    @staticmethod
    def es_libro_grande(paginas):
        if paginas > 500:
            print("Es un libro grande.")    
        else:
            print("No es un libro grande.")
        return paginas
    
libro_1 = Libro("1984", "George Orwell", 328)
libro_2 = Libro("El seno de la libertad", "Federico Garciá", 400)
libro_3 = Libro.cargar_desde_string("El Principito|Antoine de Saint-Exupery|200")
libro_4 = Libro.cargar_desde_string("La Odisea|Homero|800")

libro_1.leer(100).progreso()
libro_2.leer(100).progreso()
libro_3.leer(100).progreso()
libro_4.leer(100).progreso()
libro_4.es_libro_grande(800)