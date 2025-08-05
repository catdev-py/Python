class RutInvalido(Exception):
    pass

def leer_rut(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                rut = linea.strip()
                if not rut.isdigit() or len(rut) < 7:
                    raise RutInvalido(f"RUT inválido encontrado: {rut}")
                print(f"RUT válido: {rut}")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
    except RutInvalido as e:
        print(e)

leer_rut("ruts.txt")