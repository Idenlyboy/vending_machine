from View import UIMachine
from modules.Statuses import VendingStatuses, ProductStatuses

if __name__ == "__main__":
    vending_statuses = VendingStatuses.STATUSES
    product_statuses = ProductStatuses.STATUSES
    vending_machine1 = UIMachine(name='Food', empty_slots=20, status_key=vending_statuses['work'], money=0)
    vending_machine1.help()
    vending_machine1.show_price_list()
    vending_machine1.create_and_add_product(name='Coca-Cola', status_key=product_statuses['released'], code=2261)
    vending_machine1.create_and_add_product(name='Mars', status_key=product_statuses['released'], code=2102)
    vending_machine1.create_and_add_product(name='Twix', status_key=product_statuses['released'], code=2102)
    vending_machine1.create_and_add_product(name='Bounty', status_key=product_statuses['released'], code=2102)
    vending_machine1.create_and_add_product(name='Milky Way', status_key=product_statuses['released'], code=2102)
    vending_machine1.buy_product(2102, 100)
    vending_machine1.get_empty_slots()
    vending_machine1.remove_product_by_code(2102)
    vending_machine1.get_empty_slots()
    vending_machine1.show_info()
    vending_machine1.show_logs('-a')
    