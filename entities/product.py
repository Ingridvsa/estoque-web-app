class Product:
    def __init__(self, name="", price=0.0, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value_in_stock(self):
        return self.price * self.quantity

    def add_products(self, quantity):
        self.quantity += quantity

    def remove_products(self, quantity):
        self.quantity -= quantity

    def update_name(self, new_name):
        self.name = new_name

    def update_price(self, new_price):
        self.price = new_price
