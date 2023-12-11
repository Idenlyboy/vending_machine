from UI.UI import UIMachine
from Domain.VendingMachine.Statuses.Statuses import VendingStatuses
from Domain.Product.Statuses.Statuses import ProductStatuses

if __name__ == "__main__":
    vending_statuses = VendingStatuses.STATUSES
    product_statuses = ProductStatuses.STATUSES
    vending_interface = UIMachine(name='Food', empty_slots=20, status_key=vending_statuses['work'], money=0)
    vending_interface.help()
    vending_interface.show_price_list()
    vending_interface.create_and_add_product(name='Coca-Cola', status_key='released', code=2261)
    vending_interface.create_and_add_product(name='Mars', status_key='released', code=2102)
    vending_interface.create_and_add_product(name='Twix', status_key='released', code=2102)
    vending_interface.create_and_add_product(name='Bounty', status_key='released', code=2102)
    vending_interface.create_and_add_product(name='Milky Way', status_key='released', code=2102)
    vending_interface.buy_product(code=2261, deposit=100)
    vending_interface.show_empty_slots()
    vending_interface.remove_product_by_code(2102)
    vending_interface.show_empty_slots()
    vending_interface.show_info()
    vending_interface.show_logs('-a')
    