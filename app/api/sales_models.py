from datetime import datetime

sales = []

my_date = datetime.now().replace(microsecond=0)


class Sales():
    """Class for for SalesModel"""

    def __init__(self, name, quantity, price, sales_id, date_created):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.sales_id = sales_id
        self.date_created = my_date.isoformat()

    def add_sales(self):
        sale = {
            'product': self.name,
            'quantity': self.quantity,
            'price': self.price,
            'sales_id': self.sales_id,
            'date_created': self.date_created
        }

        sales.append(sale)
