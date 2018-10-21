import unittest
import json
import base64
from app import create_app


class ProductTestCase(unittest.TestCase):
    """This is the class for product test cases"""

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client
        self.valid_credentials = base64.b64encode(
            b'admin:NotSoSecret').decode('utf-8')
        self.invalid_credentials = base64.b64encode(
            b'adm:NotSoSecret').decode('utf-8')

    def test_to_add_product(self):
        """Test method to add product(POST request)"""
        add_product = self.client().post(
            '/api/v1/product/pencil',
            data=json.dumps(
                dict(category='category',
                     Quantity='Quantity',
                     Description='Description',
                     price='price')),
            content_type='application/json',
            headers={'Authorization': 'Basic ' + self.valid_credentials})
        self.assertEqual(add_product.status_code, 201)

    def test_to_get_single_item(self):
        """Test method to get a single product(GET request)"""
        get_product = self.client().get('/api/v1/product/1',
                                        data=json.dumps(
                                            dict(category='category',
                                                 Quantity='Quantity',
                                                 Description='Description',
                                                 price='price')),
                                        content_type='application/json')
        self.assertEqual(get_product.status_code, 200)
