from flask import Flask, request
from flask_restful import Resource, Api
from datetime import datetime

app = Flask(__name__)
api = Api(app)

my_date = datetime.now().replace(microsecond=0)

sales = []  # using in memory , just a python list


class Sales(Resource):
    """Class to handle post request , to create a sale"""

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


class SalesId(Resource):
    """Class to handle delete of a sale"""

    def delete(self, id):
        """Method to delete a single sale"""
        global sales
        sales = list(filter(lambda x: x['sales_id'] != id, sales))
        return {'message': 'sale deleted'}

    def get(self, id):
        """Method to get a single sale"""
        sale = next(filter(lambda x: x['sales_id'] == id, sales), None)
        return{'sale': sale}, 200 if sale else 404


class SalesList(Resource):
    """Class to handle getting list of sales"""

    def get(self):
        return{'sales': sales}
