'''This code defines a Product class that represents a product with a name, price, and quantity in stock. 
It also defines an Inventory class that represents a collection of products. The Inventory class has 
methods for adding and removing products, and for getting a product by name.

The code creates an Inventory object and adds some Product objects to it. It then prints the inventory 
and gets a product by name. Finally, it removes a product from the inventory and prints it again.'''


'''The Product class represents a product with a name, price, and quantity in stock. It has an __init__ 
method that initializes these attributes when a Product object is created. It also has a __str__ method 
that returns a string representation of the product in the form 'name: $price (quantity in stock)'.'''
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        return f'{self.name}: ${self.price} ({self.quantity} in stock)'


'''The Inventory class represents a collection of products. It has an __init__ method that initializes an 
empty list of products. It has add_product and remove_product methods that add and remove products from 
the list, respectively. It has a get_product method that takes a product name as input and returns the 
product with that name, or None if no such product exists. It also has a __str__ method that returns a 
string representation of the inventory as a list of product strings, separated by newlines.'''
class Inventory:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
    
    def remove_product(self, product):
        self.products.remove(product)
    
    def get_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None
    
    def __str__(self):
        return '\n'.join(str(product) for product in self.products)


'''The code creates an Inventory object and adds three Product objects to it. It then prints the 
inventory, gets a product by name, and removes the product from the inventory. Finally, it prints 
the inventory again.'''
# Create the inventory
inventory = Inventory()

# Add some products
inventory.add_product(Product('Apple', 0.5, 10))
inventory.add_product(Product('Banana', 0.25, 20))
inventory.add_product(Product('Orange', 0.75, 5))

# Print the inventory
print(inventory, end="\n\n")

# Get a product
apple = inventory.get_product('Apple')
print(apple, end="\n\n")

# Remove a product
inventory.remove_product(apple)
print(inventory)
