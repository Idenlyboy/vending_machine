from Domain.VendingMachine.Models.Vending import VendingMachine
from Domain.VendingMachine.Statuses.Statuses import VendingStatuses
from Domain.Product.Statuses.Statuses import ProductStatuses
from Domain.Product.Models.Product import Product
from Data.PriceList import price_list


class UIMachine:

    def __init__(self, name, empty_slots, status_key, money):
        self.status = VendingStatuses.STATUSES[status_key]
        self.vending_machine = VendingMachine(name, empty_slots, self.status, money)

    @staticmethod
    def help():
        print('You can create and add product by function "create_and_add_product()" - \n'
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

    def create_and_add_product(self, name, code, status_key):
        status = ProductStatuses.STATUSES[status_key]
        product = Product()
        product.set_product_data(name, code, status)
        self.vending_machine.add_product(product)

    def buy_product(self, code: int, deposit: int):
        self.vending_machine.buy_product(code, deposit)

    def remove_product_by_code(self, code):
        self.vending_machine.remove_product_by_code(code)

    def show_logs(self, *args):
        self.vending_machine.logs_service.show_logs([*args])

    def get_status(self):
        return self.vending_machine.status

    def show_empty_slots(self):
        print(self.vending_machine.get_empty_slots(), 'empty slots')

    @staticmethod
    def show_price_list():
        print('code: price\n', price_list, sep='')

    def show_info(self):
        products_in_machine = self.vending_machine.get_products_in()
        print(f'"{self.vending_machine.name}" vending machine in "{self.vending_machine.status}" status with {self.vending_machine.money} rubles in.\n'
              f'positions:\n{[i.name for i in products_in_machine]}\n'
              f'and has {self.vending_machine.get_empty_slots()} empty slots')


