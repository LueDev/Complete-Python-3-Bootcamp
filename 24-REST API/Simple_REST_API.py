
'''These lines import the Flask, jsonify, and request objects from the Flask library. 
The Flask object is the main object of the Flask web framework, and it is used to create 
and run a web server. The jsonify object is used to convert Python data structures to JSON 
format, and the request object is used to access the HTTP request data sent by the client.'''
from flask import Flask, jsonify, request

app = Flask(__name__)


'''This is a list of products, represented as dictionaries with 'name' and 'price' keys.'''
# A list of products
products = [
    {'name': 'Apple', 'price': 0.5},
    {'name': 'Banana', 'price': 0.25},
    {'name': 'Orange', 'price': 0.75}
]

'''This defines a route for the home page of the API. The @app.route decorator creates a URL 
route that maps to the decorated function. In this case, the route is '/', which is the root 
of the API. The function home() returns a welcome message when the home page is accessed.'''
# The home page
@app.route('/')
def home():
    return 'Welcome to the Product API!'


'''This defines a route for accessing a list of products. The @app.route decorator creates a 
URL route that maps to the decorated function. In this case, the route is '/products', which 
returns a JSON object with the list of products when accessed. The jsonify function converts 
the products list to JSON format and returns it as an HTTP response.'''
# A list of products
@app.route('/products')
def get_products():
    return jsonify(products)


'''This defines a route for accessing a single product by name. The @app.route decorator creates 
a URL route that maps to the decorated function. In this case, the route is '/products/<string:name>', 
where name is a URL parameter that specifies the name of the product. The function get_product(name) 
searches the products list for a product with the specified name and returns it as a JSON object if 
found. If no such product is found, it returns an error message and a 404 HTTP status code.'''
# A single product
@app.route('/products/<string:name>')
def get_product(name):
    for product in products:
        if product['name'] == name:
            return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404


'''This defines a route for creating a new product. The @app.route decorator creates a URL 
route that maps to the decorated function. In this case, the route is '/products', and the 
`methods'''
# Create a product
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    products.append(data)
    return jsonify(data), 201


'''This defines a route for updating an existing product. The @app.route decorator creates a 
URL route that maps to the decorated function. In this case, the route is '/products/<string:name>',
where name is a URL parameter that specifies the name of the product. The function update_product(name) 
searches the products list for a product with the specified name, and updates its data with the data 
sent in the HTTP request. If the product is found, it returns the updated product as a JSON object. 
If no such product is found, it returns an error message and a 404 HTTP status code.'''
# Update a product
@app.route('/products/<string:name>', methods=['PUT'])
def update_product(name):
    data = request.get_json()
    for product in products:
        if product['name'] == name:
            product.update(data)
            return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404


'''This defines a route for deleting an existing product. The @app.route decorator creates a URL route 
that maps to the decorated function. In this case, the route is '/products/<string:name>', where name 
is a URL parameter that specifies the name of the product. The function delete_product(name) searches 
the products list for a product with the specified name, and removes it from the list if found. If the 
product is found, it returns a message indicating that the product was deleted. If no such product is 
found, it returns an error message and a 404 HTTP status code.'''
# Delete a product
@app.route('/products/<string:name>', methods=['DELETE'])
def delete_product(name):
    for product in products:
        if product['name'] == name:
            products.remove(product)
            return jsonify({'message': 'Product deleted'})
    return jsonify({'error': 'Product not found'}), 404


'''This runs the Flask web server when the script is executed. The if __name__ == '__main__': block is 
a standard Python idiom that is used to specify that the code in the block should be executed only if 
the script is run directly, and not if it is imported as a module.'''
# Run the API
if __name__ == '__main__':
    app.run()
