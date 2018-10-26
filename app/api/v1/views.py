from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from app.api.product_models import products_item, Product


app = Flask(__name__)
api = Api(app)


class ProductView(Resource):
    """Class to handle post for product"""
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field is mandatory")
    parser.add_argument('product_id',
                        type=int,
                        required=True,
                        help="This field is mandatory")
    # parser.add_argument('name', type=str)
    parser.add_argument('description',
                        type=str,
                        required=True,
                        help="This field is mandatory ")
    parser.add_argument('quantity', type=int,
                        required=True,
                        help="This field is mandatory")
    parser.add_argument('category', type=str,
                        required=True,
                        help="This field is mandatory")

    def post(self, name):
        """Method to add/create a new product"""
        product_results = list(
            filter(lambda x: x['name'] == name, products_item))
        if len(product_results):
            return {'message':
                    "A product with name '{}' already exists."
                    .format(name)}, 400

        request_data = ProductView.parser.parse_args()
        # name = request_data['name']
        price = request_data['price']
        product_id = request_data['product_id']
        category = request_data['category']
        quantity = request_data['quantity']
        description = request_data['description']

        # import pdb; pdb.set_trace()
        product = Product(name,
                          price, category, quantity, description,
                          product_id)

        results = dict(name=name, price=price, product_id=product_id,
                       category=category, quantity=quantity, description=description)

        # import pdb; pdb.set_trace()
        product.add_product()
        # import pdb; pdb.set_trace()
        return results, 201

    def put(self, name):
        """Method to update/create a single product"""
        # getting data from the request
        data = request.get_json()
        product_results = next(
            # getting the next available value of that filter
            # object, or we're getting none if there are none left
            filter(lambda x: x['name'] == name, products_item), None)

        if product_results is None:  # if there is no item, create one
            product_results = {'product_id': len(products_item) + 1,
                               'name': name,
                               'category': data['category'],
                               'price': data['price'],
                               'quantity': data['quantity'],
                               'description': data['description']
                               }
            products_item.append(product_results)

        # if it already exists
        else:
            product_results.update(data)
        return product_results, 200


class ProductId(Resource):
    """Class to handle the delete endpoint"""

    def delete(self, product_id):
        """Method to delete a single product"""
        # the products variable in this block is the outer 'products =[]'
        # variable
        global products_item
        # list after the result of filtering
        # looking for all the elements except the one that is going to be
        # delated
        products_item = list(
            filter(lambda x: x['product_id'] != product_id, products_item))
        return {'message': 'item deleted'}

    def get(self, product_id):
        product = next(
            filter(lambda x: x['product_id'] == product_id, products_item), None)
        return{'product': product}, 200 if product else 404

    # product_results = [
    # product_results for product_results in products_item if product_results['product_id'] == product_id]
    # if len(product_results) == 0:
    #     return {'Error': 'product not found'}, 404
    # data = (product_results)
    # return data, 200 


class ProductList(Resource):
    """Class to handle getting list of products"""

    def get(self):
        # returning a dic of products

        return {'products': products_item}
