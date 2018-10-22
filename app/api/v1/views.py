from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

products = []  # using in memory , just a python list


class Product(Resource):
    """Class to handle post"""

    def post(self, name):
        """Method to add/create a new product"""
        if next(filter(lambda x: x['name'] == name, products), None):
            return {'message':
                    "A product with name '{}' already exists."
                    .format(name)}, 400
            # accessing price and category key from the data dic
            # getting the json payload from a request

        data = request.get_json()
        product = {'product_id': len(products) + 1,
                   'name': name,
                   'category': data['category'],
                   'price': data['price'],
                   'Quantity': data['Quantity'],
                   'Description': data['Description']
                   }
        products.append(product)
        return product, 201

    def put(self, name):
        """Method to update/create a single product"""
        # getting data from the request
        data = request.get_json()
        product = next(filter(lambda x: x['name'] == name, products), None)

        if product is None:  # if there is no item, create one
            product = {'product_id': len(products) + 1,
                       'name': name,
                       'category': data['category'],
                       'price': data['price'],
                       'Quantity': data['Quantity'],
                       'Description': data['Description']
                       }
            products.append(product)

        # if it already exists
        else:
            product.update(data)
        return product, 200
