""" def operaciones(x, y):
    suma = x + y
    producto = x * y
    return (suma, producto)
    
resultado = operaciones(5, 3)
print("Suma:", resultado[0])
print("Producto:", resultado[1]) """

# ACTIVIDAD:
# Crea una función que reciba 3 notas y retorne (promedio, nota más alta, nota más baja)

# Felipe
""" def calcular_notas(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    nota_mas_alta = max(nota1, nota2, nota3)
    nota_mas_baja = min(nota1, nota2, nota3)
    return (promedio, nota_mas_alta, nota_mas_baja)

resultado = calcular_notas(5, 7, 9)
print(f"Promedio: {resultado[0]}, Nota mas alta: {resultado[1]}, Nota mas baja: {resultado[2]}") """

# Gerald
""" def nota(x,y,z):
    promedio = (x+y+z)/3
    nota_alta = max(x,y,z)
    nota_baja = min(x,y,z)
    return promedio,nota_alta,nota_baja
x = float(input("Ingrese la primera nota: "))
y = float(input("Ingrese la segunda nota: "))
z = float(input("Ingrese la tercera nota: "))
promedio,nota_alta,nota_baja = nota(x,y,z)
print(f"El promedio es: {promedio}")
print(f"La nota mas alta es: {nota_alta}")
print(f"La nota mas baja es: {nota_baja}") """

# Gerald 2
def nota(x,y,z):
    promedio = (float(x) + float(y) + float(z))/3
    nota_alta = max(x,y,z)
    nota_baja = min(x,y,z)
    return promedio,nota_alta,nota_baja
def val_num(n1, n2, n3):
    try:
        n1 = float(n1)
        n2 = float(n2)
        n3 = float(n3)
        if n1 < 0 or n2 < 0 or n3 < 0:
            print("Por favor, ingrese valores positivos.")
            return False
        else:
            return True
    except ValueError:
        print("Por favor, ingrese solo numeros.")
while True:
    x = input("Ingrese la primera nota: ")
    y = input("Ingrese la segunda nota: ")
    z = input("Ingrese la tercera nota: ")
    if val_num(x,y,z):
        break
promedio,nota_alta,nota_baja = nota(x,y,z)
print(f"El promedio es: {int(promedio)}")
print(f"La nota mas alta es: {nota_alta}")
print(f"La nota mas baja es: {nota_baja}")

# Jorge
""" N = []
a= int(input('ingrese primer N'))
N.append(a)
b = int(input('ingrese segundo  N'))
N.append(b)
c = int(input('ingrese tercerer N'))
N.append(c)
 
print(sum(N) / len(N))
print(max(N))
print(min(N)) """