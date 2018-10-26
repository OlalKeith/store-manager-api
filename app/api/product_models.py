products_item = []


class Product():
    """Class for  Product models"""

    def __init__(self, name, price, product_id, category, quantity, description):

        self.name = name
        self.price = price
        self.category = category
        self.quantity = quantity
        self.description = description
        self.product_id = product_id

    def add_product(self):
        product = {

            'name': self.name,
            'category': self.category,
            'price': self.price,
            'quantity': self.quantity,
            'description': self.description,
            'product_id': self.product_id
        }

        products_item.append(product)
