import unittest
import json
from app import create_app


class SalesTestCase(unittest.TestCase):
    """This is the class for sales test cases"""

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client

    def test_create_sale(self):
        """Test method to create a sale"""
        create_sale = self.client().post('/api/v1/sale/pencil',
                                         data=json.dumps(
                                             dict(
                                                 Quantity='Quantity',
                                                 price='price')),
                                         content_type='application/json')
        self.assertEqual(create_sale.status_code, 201)

    def test_to_delete_sale(self):
        """Test method to delete a sale"""
        delete_sale = self.client().delete('/api/v1/sale/1',
                                           data=json.dumps(
                                               dict(
                                                   Quantity='Quantity',
                                                   price='price')),
                                           content_type='application/json')
        self.assertEqual(delete_sale.status_code, 200)

    def test_get_single_sale(self):
        """Test method to get a single sale"""
        get_single_sale = self.client().get('/api/v1/sale/1',
                                            data=json.dumps(
                                                dict(
                                                    Quantity='Quantity',
                                                    price='price')),
                                            content_type='application/json')
        self.assertEqual(get_single_sale.status_code, 200)

    def test_to_get_all_sales(self):

        get_all_sales = self.client().get('/api/v1/sales',
                                          data=json.dumps(
                                              dict(
                                                  Quantity='Quantity',
                                                  price='price')),
                                          content_type='application/json')
        self.assertEqual(get_all_sales.status_code, 200)
