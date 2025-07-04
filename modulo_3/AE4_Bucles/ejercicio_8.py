# Ejercicio 8: Recorrer un diccionario de regiones y capitales de Chile
regiones = {
    "Arica y Parinacota": "Arica",
    "Los Lagos": "Puerto Montt",
    "Araucanía": "Temuco"
}

for region, capital in regiones.items():
    print(f"La capital de {region} es {capital}")
