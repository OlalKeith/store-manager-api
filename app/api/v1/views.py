from flask import Flask, request
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'super-secret'
api = Api(app)
auth = HTTPBasicAuth()

USER_DATA = {
    "admin": "NotSoSecret"
}

products = []  # using in memory , just a python list


@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password


class Product(Resource):
    """Class to handle post for product"""
    @auth.login_required
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


class ProductId(Resource):
    """Class to handle get request to get a single order"""

    def get(self, id):
        product = next(
            filter(lambda x: x['product_id'] == id, products), None)
        return{'product': product}, 200 if product else 404
