from modules.Conditions import VendingConditions
from validation.Validations import conditions_validated, vending_product_validated
from modules.Product import Product
from etc.PriceList import price_list
from modules.Logs import Logs


class VendingMachine:

    def __init__(self, name: str, empty_slots: int, condition: VendingConditions, money: int):
        self.name = name
        self.empty_slots = empty_slots
        self.condition = condition
        self.money = money
        self.conditions = VendingConditions
        self.logs = Logs
        self.slots = []
        return

    def change_condition(self, new_condition: VendingConditions):
        if conditions_validated(new_condition):
            self.logs.changed_condition(self.condition, new_condition)
            self.condition = new_condition
        return

    def add_product(self, product: Product):
        if self.empty_slots > 0 and vending_product_validated(product):
            self.logs.added_product(product)
            self.slots.append(product)
            self.empty_slots -= 1
        return

    def show_slots(self):
        return self.slots

    def remove_product_by_code(self, product_code):
        for product in self.slots:
            if product.code == product_code:
                self.logs.removed_by_code(product)
                del product
                self.empty_slots += 1
                break
        else:
            print('No such product with that code')
        return

    def get_empty_slots(self):
        return self.empty_slots

    def buy_product(self, product_code, deposit):
        cost = price_list[product_code]
        self.logs.bought_product(product_code)
        self.remove_product_by_code(product_code)
        self.money += cost
        self.give_the_change(deposit - cost)
        return

    @staticmethod
    def give_the_change(change):
        print(f'Take your change ({change})')
        return

    def show_log(self, *args):
        self.logs.show_logs([*args])




