class Product:
    def __init__(self, description, quantity, price):
        self.description = description
        self.quantity = quantity  # Stock disponible
        self.price = price


class Client:
    def __init__(self, name, purchase_number, buy_day):
        self.name = name
        self.purchase_number = purchase_number
        self.buy_day = buy_day


# Lista de productos disponibles
products = [
    Product("Manzana", 20, 500),
    Product("Durazno", 15, 1000),
    Product("Naranja", 10, 750),
    Product("Piña", 8, 1500),
    Product("Sandía", 5, 2500)
]

# Simulación cliente
client_name = input("Ingrese el nombre del cliente: ")
purchase_number = int(input("Ingrese la cantidad de compras previas del cliente: "))
buy_day = input("Ingrese el día de la compra: ")

client = Client(client_name, purchase_number, buy_day)

# Carrito de compras
cart = []
total_purchase_amount = 0
total_products = 0

# Mostrar productos disponibles
print("\nProductos disponibles:")
for index, product in enumerate(products):
    print(f"{index + 1}. {product.description} - Stock: {product.quantity} - Precio: ${product.price}")

# Proceso de compra
while True:
    option = input("\nIngrese el número del producto que desea comprar (o 'fin' para terminar): ")

    if option.lower() == "fin":
        break

    try:
        product_index = int(option) - 1
        if product_index < 0 or product_index >= len(products):
            print("Producto no válido.")
            continue

        selected_product = products[product_index]

        quantity = int(input(f"Ingrese la cantidad de {selected_product.description} que desea comprar: "))

        if quantity <= 0:
            print("Cantidad no válida.")
            continue

        if quantity > selected_product.quantity:
            print("No hay suficiente stock disponible.")
            continue

        # Agregar al carrito
        cart.append((selected_product, quantity))
        selected_product.quantity -= quantity
        total_products += quantity
        total_purchase_amount += selected_product.price * quantity

        print(f"Agregado {quantity} {selected_product.description}(s) al carrito.")

    except ValueError:
        print("Entrada no válida, intente nuevamente.")


# Función que calcula el porcentaje total de descuento
def calculate_total_discount(total_products, client, total_purchase_amount):
    discount_percentage = 0

    if total_products > 10:
        discount_percentage += 10

    if client.purchase_number > 5:
        discount_percentage += 5

    if total_purchase_amount > 500:
        discount_percentage += 7

    if client.buy_day.lower() == "viernes":
        discount_percentage += 15

    if discount_percentage > 30:
        discount_percentage = 30

    return discount_percentage


# Resumen de la compra
print("\nResumen de la compra:")
for item in cart:
    product, quantity = item
    print(f"{quantity} x {product.description} - ${product.price} c/u = ${product.price * quantity}")

print(f"\nTotal sin descuentos: ${total_purchase_amount}")

# Calcular descuento
discount_percentage = calculate_total_discount(total_products, client, total_purchase_amount)
discount_amount = total_purchase_amount * (discount_percentage / 100)
total_final = total_purchase_amount - discount_amount

# Mostrar resultados
print(f"Descuento aplicado: {discount_percentage}%")
print(f"Total a pagar con descuento: ${total_final:.2f}")
