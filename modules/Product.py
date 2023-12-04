from Conditions import ProductConditions
from validation.Validations import product_data_validated


class Product:

    def __init__(self, name, code, condition):
        conditions = ProductConditions
        self.condition = ''
        self.name = ''
        self.code = -1
        if product_data_validated(name, code) and condition in conditions.get_conditions():
            self.name = name
            self.code = code
            self.condition = condition
        return

    def get_condition(self):
        return self.condition

    def get_code(self):
        return self.code
