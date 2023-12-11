from modules.Statuses import ProductStatuses
from validation.Validations import product_data_validated


class Product:

    STATUSES = ProductStatuses.STATUSES

    def __init__(self):
        self.status = ''
        self.name = ''
        self.code = 0

    def set_product_data(self, name, code, status):
        if product_data_validated(name, code) and status in self.STATUSES:
            self.name = name
            self.code = code
            self.status = status

    def get_status(self):
        return self.status

    def get_code(self):
        return self.code
