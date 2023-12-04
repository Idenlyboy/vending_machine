from modules.Vending import VendingMachine
from modules.Conditions import VendingConditions, ProductConditions
from modules.Product import Product
from etc.PriceList import price_list


class UIMachine:
    def __init__(self, name, empty_slots, condition_index, money):
        self.vending_conditions = VendingConditions
        self.product_conditions = ProductConditions
        condition = self.vending_conditions.get_condition_by_index(condition_index)
        self.vending_machine = VendingMachine(name, empty_slots, condition, money)
        return

    @staticmethod
    def help():
        print('You can create and add product by function "create_and_add_product()" - '
              'arguments for that function - name, code, condition_index(check documentation)'
              '\nYou can remove product by its code - function remove_product() - only one arg - product code'
              '\nYou can show logs with show_log()'
              '\nYou can buy products with buy_product() - arguments - code, deposit'
              '\nYou can get current condition of vending machine with get_condition()'
              '\nYou can get current amount of empty slots with get_empty_slots()'
              '\nYou can show price-list for easily adding new products with show_price_list()'
              '\nYou can show info about all attributes of the vending machine with show_info(arguments)'
              '\nArguments for show_info(): with/without parameters ("-a" = all, "-l5" = last 5 notes,'
              '"-l20", "-l50", "-l100")')

    def create_and_add_product(self, name, code, condition_index):
        condition = self.product_conditions.get_condition_by_index(condition_index)
        product = Product(name, code, condition)
        self.vending_machine.add_product(product)
        return

    def buy_product(self, code, deposit):
        self.vending_machine.buy_product(code, deposit)
        return

    def remove_product(self, code):
        self.vending_machine.remove_product_by_code(code)
        return

    def show_logs(self, *args):
        self.vending_machine.logs.show_logs([*args])
        return

    def get_condition(self):
        return self.vending_machine.condition

    def get_empty_slots(self):
        return self.vending_machine.get_empty_slots()

    @staticmethod
    def show_price_list():
        print(*price_list)

    def show_info(self):
        print(f'{self.vending_machine.name} in "{self.vending_machine.condition}" condition with {self.vending_machine.money} rubles in.'
              f'positions:\n{self.vending_machine.show_slots()}'
              f'and has {self.vending_machine.get_empty_slots()} empty slots')
        return


