from modules.Statuses import VendingStatuses
from validation.Validations import vending_status_validated, product_status_validated
from modules.Product import Product
from etc.PriceList import price_list
from modules.Logs import Logs


class VendingMachine:

    STATUSES = VendingStatuses.STATUSES

    def __init__(self, name: str, empty_slots: int, status: str, money: int):
        self.name = name
        self.empty_slots = empty_slots
        self.status = status
        self.money = money
        self.logs_service = Logs()
        self.slots = []

    def change_status(self, new_status: str):
        """change status from old to new with validation"""
        if vending_status_validated(new_status):
            self.logs_service.changed_status(self.status, new_status)
            self.status = new_status

    def add_product(self, product: Product):
        """add product to vending machine slots with product validation"""
        if self.empty_slots > 0 and product_status_validated(product):
            self.logs_service.added_product(product)
            self.slots.append(product)
            self.empty_slots -= 1

    def get_slots(self):
        """returns amount of slots"""
        return self.slots

    def remove_product_by_code(self, product_code):
        for product_in_slots in self.slots:
            if product_in_slots.code == product_code:
                self.logs_service.removed_by_code(product_in_slots)
                del product_in_slots
                self.empty_slots += 1
                return
        print('No such product with that code')

    def get_empty_slots(self):
        return self.empty_slots

    def buy_product(self, product_code: int, deposit: int):
        cost = price_list[product_code]
        self.logs_service.bought_product(product_code=product_code)
        self.remove_product_by_code(product_code)
        self.money += cost
        self.give_the_change(deposit - cost)


    @staticmethod
    def give_the_change(change):
        print(f'Take your change ({change})')
        return

    def show_log(self, *args):
        self.logs_service.show_logs(*args)




