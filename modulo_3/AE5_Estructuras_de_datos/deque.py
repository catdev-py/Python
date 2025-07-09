from collections import deque

historial_atras = deque()
historial_adelante = deque()

# Ir a una página nueva
def visitar(pagina):
    historial_atras.append(pagina)
    historial_adelante.clear()
    print(f"Visitas: {pagina}")

# Retroceder
def atras():
    if len(historial_atras) > 1:
        historial_adelante.appendleft(historial_atras.pop())
        print(f"Regresas a: {historial_atras[-1]}")
    else:
        print("No hay más páginas hacia atrás.")

# Adelantar
def adelante():
    if historial_adelante:
        pagina = historial_adelante.popleft()
        historial_atras.append(pagina)
        print(f"Avanzas a: {pagina}")
    else:
        print("No hay más páginas hacia adelante.")

# Simulación
visitar("google.com")
visitar("github.com")
visitar("chat.openai.com")
atras()
atras()
adelante()
