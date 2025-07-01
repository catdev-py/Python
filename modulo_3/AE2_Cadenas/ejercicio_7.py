""" 
Ejercicio Práctico: Juntando todo
Vamos a crear un programa donde el usuario escribe su nombre, edad y ciudad, 
y mostramos un mensaje usando diferentes técnicas:
"""
nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))
ciudad = input("¿De qué ciudad eres? ")

# Usando f-string
print(f"Hola {nombre}, tienes {edad} años y eres de {ciudad}")

# Usando .format()
print("Hola {}, tienes {} años y eres de {}".format(nombre, edad, ciudad))

# Usando %
print("Hola %s, tienes %d años y eres de %s" % (nombre, edad, ciudad))

