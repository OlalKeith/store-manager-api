from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from app.api.sales_models import sales, Sales
from datetime import datetime


app = Flask(__name__)
api = Api(app)

my_date = datetime.now().replace(microsecond=0)


class SalesView(Resource):
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
    parser.add_argument('quantity', type=int,
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

        request_data = SalesView.parser.parse_args()
        price = request_data['price']
        sales_id = request_data['sales_id']
        quantity = request_data['quantity']
        date_created = request_data['date_created']

        sale = Sales(name, price, quantity, sales_id, date_created)

        results = dict(name=name,
                       price=price,
                       quantity=quantity,
                       sales_id=sales_id, date_created=date_created)

        sale.add_sales()
        return results, 201

    def put(self, name):
        """Method to update/create a single sale"""

        data = request.get_json()
        sale = next(filter(lambda x: x['product'] == name, sales), None)

        if sale is None:  # if there is no item, create one
            sale = {'sales_id': len(sales) + 1,
                    'product': name,
                    'quantity': data['quantity'],
                    'price': data['price'],
                    'date_created': my_date.isoformat()
                    }
            sales.append(sale)

        # if it already exists update
        else:
            sale.update(data)
        return sale, 200


class SalesId(Resource):
    """Class to handle delete of a sale"""

    def delete(self, id):
        """Method to delete a single sale"""
        global sales
        sales = list(filter(lambda x: x['sales_id'] != id, sales))
        return {'message': 'sale deleted'}

    def get(self, sales_id):
        # import pdb; pdb.set_trace()
        sale = next(filter(lambda x: x['sales_id'] == sales_id, sales), None)
        # import pdb; pdb.set_trace()
        return{'sale': sale}, 200 if sale else 404


class SalesList(Resource):
    """Class to handle getting list of sales"""

    def get(self):
        return{'sales': sales}
