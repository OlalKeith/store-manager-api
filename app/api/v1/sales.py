from flask import Flask, request
from flask_restful import Resource, Api
from datetime import datetime

app = Flask(__name__)
api = Api(app)

my_date = datetime.now().replace(microsecond=0)

sales = []  # using in memory , just a python list


class Sales(Resource):
    """Class to handle post sales"""

    def post(self, name):
        """Method to add/create a new product"""
        if next(filter(lambda x: x['product'] == name, sales), None):
            return {'message':
                    "A product with name '{}' already exists."
                    .format(name)}, 400

        data = request.get_json()
        sale = {'sales_id': len(sales) + 1,
                'product': name,
                'Quantity': data['Quantity'],
                'price': data['price'],
                'Date': my_date.isoformat()
                }
        sales.append(sale)
        return sale, 201

    def put(self, name):
        """Method to update/create a single sale"""

        data = request.get_json()
        sale = next(filter(lambda x: x['name'] == name, sales), None)

        if sale is None:  # if there is no item, create one
            sale = {'sales_id': len(sales) + 1,
                    'product': name,
                    'Quantity': data['Quantity'],
                    'price': data['price'],
                    'Date': my_date.isoformat()
                    }
            sales.append(sale)

        # if it already exists
        else:
            sale.update(data)
        return sale, 200
