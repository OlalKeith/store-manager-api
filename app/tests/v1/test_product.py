import unittest
import json
from app import create_app


class ProductTestCase(unittest.TestCase):
    """This is the class for product test cases"""

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client
        # self.my_product = {
        #     'price': '50',
        #     'name': 'pencil',
        #     'category': 'stationery'
        # }

    def test_to_add_product(self):
        """Test method to add product"""
        add_product = self.client().post('/api/v1/product/pencil',
                                         data=json.dumps(
                                             dict(category='category',
                                                  price='price')),
                                         content_type='application/json')
        self.assertEqual(add_product.status_code, 201)
