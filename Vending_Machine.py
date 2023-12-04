from UI import UIMachine

if __name__ == "__main__":
    vending_machine1 = UIMachine(name='Food', empty_slots=20, condition_index=0, money=0)
    vending_machine1.help()
    vending_machine1.show_price_list()
    vending_machine1.create_and_add_product(name='Coca-Cola', condition_index=0, code=2261)
    vending_machine1.create_and_add_product(name='Mars', condition_index=0, code=2102)
    vending_machine1.create_and_add_product(name='Twix', condition_index=0, code=2102)
    vending_machine1.create_and_add_product(name='Bounty', condition_index=0, code=2102)
    vending_machine1.create_and_add_product(name='Milky Way', condition_index=0, code=2102)
    vending_machine1.buy_product(2102, 100)
    vending_machine1.get_empty_slots()
    vending_machine1.remove_product(2102)
    vending_machine1.get_empty_slots()
    vending_machine1.show_info()
    vending_machine1.show_logs('-a')