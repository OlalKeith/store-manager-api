from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from app.api.product_models import products_item, ProductModel


app = Flask(__name__)
api = Api(app)


class Product(Resource):
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
    parser.add_argument('Description',
                        type=str,
                        required=True,
                        help="This field is mandatory ")
    parser.add_argument('Quantity', type=int,
                        required=True,
                        help="This field is mandatory")
    parser.add_argument('Category', type=str,
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

        request_data = Product.parser.parse_args()
        # name = request_data['name']
        price = request_data['price']
        product_id = request_data['product_id']
        Category = request_data['Category']
        Quantity = request_data['Quantity']
        Description = request_data['Description']

        # import pdb; pdb.set_trace()
        product = ProductModel(name,
                               price, Category, Quantity, Description,
                               product_id)

        results = dict(name=name, price=price, product_id=product_id,
                       Category=Category, Quantity=Quantity,
                       Description=Description)
        # import pdb; pdb.set_trace()
        product.add_product()
        # import pdb; pdb.set_trace()
        return results, 201
