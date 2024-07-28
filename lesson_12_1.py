class Product:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, description={self.description}, dimensions={self.dimensions})"

class Customer:
    def __init__(self, last_name, first_name, middle_name, phone):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.phone = phone

    def __str__(self):
        return f"Customer(last_name={self.last_name}, first_name={self.first_name}, middle_name={self.middle_name}, phone={self.phone})"

class Order:
    def __init__(self, customer):
        self.customer = customer
        self.products = {}

    def add_product(self, product, quantity):
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

    def total_price(self):
        return sum(product.price * quantity for product, quantity in self.products.items())

    def __str__(self):
        products_str = '\n'.join([f"{product.name}: {quantity} pcs at ${product.price} each" for product, quantity in self.products.items()])
        return f"Order for {self.customer.first_name} {self.customer.last_name}:\n{products_str}\nTotal price: ${self.total_price()}"

product1 = Product("Laptop", 1200, "High-performance laptop", "30x20x5 cm")
product2 = Product("Smartphone", 800, "Latest model smartphone", "15x7x1 cm")

customer1 = Customer("Ivanenko", "Petro", "Mykolaiovych", "+380501234567")

order1 = Order(customer1)
order1.add_product(product1, 1)
order1.add_product(product2, 2)

print(product1)
print(product2)
print(customer1)
print(order1)
