products_item = []


class ProductModel():
    """Class for  Product models"""

    def __init__(self, name, price, product_id, Category, Quantity, Description):

        self.name = name
        self.price = price
        self.Category = Category
        self.Quantity = Quantity
        self.Description = Description
        self.product_id = product_id

    def add_product(self):
        product = {

            'name': self.name,
            'Category': self.Category,
            'price': self.price,
            'Quantity': self.Quantity,
            'Description': self.Description,
            'product_id': self.product_id
        }

        products_item.append(product)
