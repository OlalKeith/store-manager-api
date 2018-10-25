from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from app.api.sales_models import sales, SalesModel

app = Flask(__name__)
api = Api(app)


class Sales(Resource):
    """Class to handle post and get for product"""
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field is mandatory")
    parser.add_argument('sales_id',
                        type=int,
                        required=True,
                        help="This field is mandatory")
    parser.add_argument('Quantity', type=int,
                        required=True,
                        help="This field is mandatory")

    parser.add_argument('date_created', type=int)

    def post(self, name):
        """Method to add/create a new product"""
        sale_results = list(
            filter(lambda x: x['product'] == name, sales))
        if len(sale_results):
            return {'message':
                    "A product with name '{}' already exists."
                    .format(name)}, 400

        request_data = Sales.parser.parse_args()
        price = request_data['price']
        sales_id = request_data['sales_id']
        Quantity = request_data['Quantity']
        date_created = request_data['date_created']

        sale = SalesModel(name, price, Quantity, sales_id, date_created)

        results = dict(name=name,
                       price=price,
                       Quantity=Quantity,
                       sales_id=sales_id, date_created=date_created)

        sale.add_sales()
        return results, 201
