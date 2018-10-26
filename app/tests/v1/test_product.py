import unittest
import json
from app import create_app

base_url = 'api/v1'


class Test_Product_Case(unittest.TestCase):
    """Class for product test cases"""

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.products = {
            'category': 'stationery',
            'product_id': 1,
            'quantity': 5,
            'description': 'I use to write with it',
            'price': 30.00
        }

    def test_to_create_product(self):
        """Test method to add product"""

        create_product = self.client.post(base_url + '/product/pencil',
                                          data=json.dumps(
                                              self.products),
                                          content_type='application/json')
        self.assertEqual(create_product.status_code, 201)

    def test_to_delete_product(self):
        """Test method to delete a product"""
        delete_product = self.client.delete(base_url + '/product/1',
                                            data=json.dumps(self.products),
                                            content_type='application/json')
        self.assertEqual(delete_product.status_code, 200)

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

    def test_to_get_all_products(self):
        """Test method to get all products"""
        get_all_products = self.client().get('/api/v1/products',
                                             data=json.dumps(
                                                 dict(
                                                     category='category',
                                                     Quantity='Quantity',
                                                     Description='Description',
                                                     price='price')),
                                             content_type='application/json')
        self.assertEqual(get_all_products.status_code, 200)

    def test_to_update_product(self):
        """Test method to update product"""
        update_product = self.client().put('/api/v1/product/pencil',
                                           data=json.dumps(
                                               dict(category='category',
                                                    Quantity='Quantity',
                                                    Description='Description',
                                                    price='price')),
                                           content_type='application/json')
        self.assertEqual(update_product.status_code, 200)
