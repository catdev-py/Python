from datetime import date, time
from models import Administrador, Usuario, Pelicula, Funcion, Boleto

def run_simulation():
    print("===== INICIANDO SIMULACIÓN DE CINECLUB =====")

    # --- PASO 1: El Administrador configura el sistema ---
    print("\n--- [FASE DE ADMINISTRACIÓN] ---")
    admin = Administrador("Admin CINECLUB", "admin@cineclub.com", "admin123")
    
    # El admin agrega películas
    peli1 = admin.agregar_pelicula("Inception", "Ciencia Ficción", 148, "Un ladrón que roba secretos corporativos a través del uso de la tecnología de compartir los sueños.")
    peli2 = admin.agregar_pelicula("The Matrix", "Ciencia Ficción", 136, "Un hacker informático aprende de misteriosos rebeldes sobre la verdadera naturaleza de su realidad.")
    
    # Guardamos las películas en una "base de datos" simulada (una lista)
    peliculas_en_cartelera = [peli1, peli2]
    
    # El admin agrega funciones para esas películas
    funcion1 = admin.agregar_funcion(peli1, date(2023, 10, 28), time(20, 30), sala=1, asientos=50)
    funcion2 = admin.agregar_funcion(peli1, date(2023, 10, 28), time(22, 0), sala=2, asientos=30)
    funcion3 = admin.agregar_funcion(peli2, date(2023, 10, 29), time(19, 0), sala=1, asientos=50)
    
    funciones_disponibles = [funcion1, funcion2, funcion3]

    # --- PASO 2: Un Usuario interactúa con el sistema ---
    print("\n--- [FASE DE USUARIO] ---")
    usuario1 = Usuario("Ana", "ana@email.com", "ana_pass")
    
    print(f"\nBienvenida, {usuario1.nombre}. Estas son las funciones disponibles:")
    for i, f in enumerate(funciones_disponibles):
        print(f"{i+1}. {f} (Asientos: {f.obtener_disponibilidad()})")

    # Ana decide comprar boletos para la primera función de Inception
    boletos_comprados_ana = usuario1.comprar_boleto(funcion1, cantidad=2)
    
    # Verificamos si la compra fue exitosa
    if boletos_comprados_ana:
        print("\nDetalle de los boletos de Ana:")
        for boleto in boletos_comprados_ana:
            print(boleto)
            
    # --- PASO 3: Otro usuario interactúa ---
    usuario2 = Usuario("Luis", "luis@email.com", "luis_pass")
    
    # Luis intenta comprar boletos para la misma función
    boletos_comprados_luis = usuario2.comprar_boleto(funcion1, cantidad=1)

    # --- PASO 4: Verificación del estado del sistema ---
    print("\n--- [VERIFICACIÓN DE ESTADO] ---")
    print(f"Estado final de la función '{funcion1}':")
    print(f"Asientos disponibles ahora: {funcion1.obtener_disponibilidad()}")
    
    print("\nBoletos comprados por Ana:")
    print(f"Ana tiene {len(usuario1.boletos)} boleto(s).")
    
    print("\nBoletos comprados por Luis:")
    print(f"Luis tiene {len(usuario2.boletos)} boleto(s).")

    # Intento de compra fallido (no hay tantos asientos)
    usuario3 = Usuario("Carlos", "carlos@email.com", "carlos_pass")
    usuario3.comprar_boleto(funcion2, cantidad=40)

    print("\n===== SIMULACIÓN FINALIZADA =====")

if __name__ == "__main__":
    run_simulation()
