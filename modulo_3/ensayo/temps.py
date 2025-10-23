def convertir_temperatura(valor, tipo):
    """
    Convierte grados Celsius a Fahrenheit o viceversa.
    tipo: 'C' para Celsius a Fahrenheit, 'F' para Fahrenheit a Celsius.
    """
    if tipo.upper() == 'C':
        resultado = (valor * 9/5) + 32
        return round(resultado, 2)
    elif tipo.upper() == 'F':
        resultado = (valor - 32) * 5/9
        return round(resultado, 2)
    else:
        return "Tipo inválido. Use 'C' o 'F'."

# Ejemplos de uso:
print(convertir_temperatura(20, 'C'))  # 68.0°F
print(convertir_temperatura(68, 'F'))  # 20.0°C
