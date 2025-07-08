class Product:
    def __init__(self, description, quantity, price):
        self.description = description
        self.quantity = quantity
        self.price = price
        
class Client:
    def __init__(self, name, purchase_number, buy_day):
        self.name = name
        self.purchase_number = purchase_number
        self.buy_day = buy_day

# Create 10 products
products = [
    Product("Apple", 5, 200),
    Product("Peach", 15, 100),
    Product("Orange", 7, 150),
    Product("Pineapple", 12, 300),
    Product("Watermelon", 3, 250),
    Product("Kiwi", 20, 180),
    Product("Lemon", 8, 120),
    Product("Mango", 6, 220),
    Product("Grape", 9, 190),
    Product("Peach", 11, 160)
]

# Create a client
client = Client("Charlie Brown", 8, "Friday")

def calculate_total_discount(product, client, total_purchase_amount):
    discount_percentage = 0
    
    # more than 10 products
    if product.quantity > 10:
        discount_percentage += 5
    # frequent customer
    if client.purchase_number > 5:
        discount_percentage += 10
    # Total purchase greater than $500
    if total_purchase_amount > 500:
        discount_percentage += 7
    # Special promotion day (e.g. Friday)
    if client.buy_day.lower() == "friday":
        discount_percentage += 15
    # maximum discount allowed is 30%
    if discount_percentage > 30:
        discount_percentage = 30
    return discount_percentage

# Calculate the total
subtotal = sum(product.price for product in products)
total = 0

for product in products:
    discount_percentage = calculate_total_discount(product, client, subtotal)
    discount_amount = product.price * (discount_percentage / 100)
    final_price = product.price - discount_amount
    
    print(f"Producto: {product.description} - Precio Original: ${product.price} - Descuento aplicado: {discount_percentage}% - Precio Final: ${final_price:.2f}")
        
    total += final_price
    
print("\nSubtotal sin descuentos:", subtotal)
print("Total con descuentos aplicados:", total)