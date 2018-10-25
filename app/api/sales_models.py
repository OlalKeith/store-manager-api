from datetime import datetime

sales = []

my_date = datetime.now().replace(microsecond=0)


class SalesModel():
    """Class for for SalesModel"""

    def __init__(self, name, Quantity, price, sales_id, date_created):
        self.name = name
        self.Quantity = Quantity
        self.price = price
        self.sales_id = sales_id
        self.date_created = my_date.isoformat()

    def add_sales(self):
        sale = {
            'product': self.name,
            'Quantity': self.Quantity,
            'price': self.price,
            'sales_id': self.sales_id,
            'date_created': self.date_created
        }

        sales.append(sale)
