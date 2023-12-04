from modules.Product import Product
from validation.Validations import list_products_validated


class ListProducts:

    def __init__(self, products_arr: list[Product]):
        self.arr = []
        for product in products_arr:
            if list_products_validated(product):
                self.arr.append(product)
        return

    def insert(self, product: Product):
        if self.validated(product):
            self.arr.append(product)
        return

    def get_list(self):
        return self.arr
