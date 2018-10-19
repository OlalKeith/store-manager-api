import unittest
import json
from app import create_app


class ProductTestCase(unittest.TestCase):
    """This is the class for product test cases"""

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client

    def test_to_add_product(self):
        """Test method to add product(POST request)"""
        add_product = self.client().post('/api/v1/product/pencil',
                                         data=json.dumps(
                                             dict(category='category',
                                                  Quantity='Quantity',
                                                  Description='Description',
                                                  price='price')),
                                         content_type='application/json')
        self.assertEqual(add_product.status_code, 201)

    # def test_to_delete_product(self):
    #     """Test method to delete a product"""
    #     delete_product = self.client().delete('/api/v1/product/1',
    #                                           data=json.dumps(
    #                                               dict(category='catgegory',
    #                                                    Quantity='Quantity',
    #                                                    Description='Description',
    #                                                    price='price')),
    #                                           content_type='application/json')
    #     self.assertEqual(delete_product.status_code, 200)

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
