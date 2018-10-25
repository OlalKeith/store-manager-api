import unittest
import json
from app import create_app

base_url = 'api/v1'


class SalesTestCase(unittest.TestCase):
    """This is the class for product test cases"""

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.sales = {'Quantity': 5,
                      'price': 30.00,
                      'sales_id': 1,
                      }

    def test_create_sale(self):
        """Test method to create a sale"""
        create_sale = self.client.post(base_url + '/sale/pencil',
                                       data=json.dumps(self.sales),
                                       content_type='application/json')
        self.assertEqual(create_sale.status_code, 201)

    def test_to_delete_sale(self):
        """Test method to delete a sale"""
        delete_sale = self.client.delete(base_url + '/sale/1',
                                         data=json.dumps(self.sales),
                                         content_type='application/json')
        self.assertEqual(delete_sale.status_code, 200)
