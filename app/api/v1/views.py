from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

products = []  # using in memory , just a python list


class Product(Resource):
    """Class to handle post and get for product"""

    def post(self, name):
        """Method to add/create a new product"""
        if next(filter(lambda x: x['name'] == name, products), None):
            return {'message':
                    "A product with name '{}' already exists."
                    .format(name)}, 400
            # accessing price and category key from the data dic
            # getting the json payload from a request

        data = request.get_json()
        product = {'id': len(products) + 1,
                   'name': name,
                   'category': data['category'],
                   'price': data['price']
                   }
        products.append(product)
        return product, 201

    def delete(self, name):
        """Method to delete a single product"""
        # the products variable in this block is the outer 'products =[]'
        # variable
        global products
        # list after the result of filtering
        # looking for all the elements except the one that is going to be
        # delated
        products = list(filter(lambda x: x['name'] != name, products))
        return {'message': 'item deleted'}
